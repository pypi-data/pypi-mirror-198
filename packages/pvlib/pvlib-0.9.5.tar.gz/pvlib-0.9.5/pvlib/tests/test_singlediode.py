"""
testing single-diode methods using JW Bishop 1988
"""

import numpy as np
import pandas as pd
import scipy
from pvlib import pvsystem
from pvlib.singlediode import (bishop88_mpp, estimate_voc, VOLTAGE_BUILTIN,
                               bishop88, bishop88_i_from_v, bishop88_v_from_i)
import pytest
from .conftest import DATA_DIR

POA = 888
TCELL = 55


@pytest.mark.parametrize('method', ['brentq', 'newton'])
def test_method_spr_e20_327(method, cec_module_spr_e20_327):
    """test pvsystem.singlediode with different methods on SPR-E20-327"""
    spr_e20_327 = cec_module_spr_e20_327
    x = pvsystem.calcparams_desoto(
        effective_irradiance=POA, temp_cell=TCELL,
        alpha_sc=spr_e20_327['alpha_sc'], a_ref=spr_e20_327['a_ref'],
        I_L_ref=spr_e20_327['I_L_ref'], I_o_ref=spr_e20_327['I_o_ref'],
        R_sh_ref=spr_e20_327['R_sh_ref'], R_s=spr_e20_327['R_s'],
        EgRef=1.121, dEgdT=-0.0002677)
    il, io, rs, rsh, nnsvt = x
    pvs = pvsystem.singlediode(*x, method='lambertw')
    out = pvsystem.singlediode(*x, method=method)
    isc, voc, imp, vmp, pmp, ix, ixx = out.values()
    assert np.isclose(pvs['i_sc'], isc)
    assert np.isclose(pvs['v_oc'], voc)
    # the singlediode method doesn't actually get the MPP correct
    pvs_imp = pvsystem.i_from_v(rsh, rs, nnsvt, vmp, io, il, method='lambertw')
    pvs_vmp = pvsystem.v_from_i(rsh, rs, nnsvt, imp, io, il, method='lambertw')
    assert np.isclose(pvs_imp, imp)
    assert np.isclose(pvs_vmp, vmp)
    assert np.isclose(pvs['p_mp'], pmp)
    assert np.isclose(pvs['i_x'], ix)
    pvs_ixx = pvsystem.i_from_v(rsh, rs, nnsvt, (voc + vmp)/2, io, il,
                                method='lambertw')
    assert np.isclose(pvs_ixx, ixx)


@pytest.mark.parametrize('method', ['brentq', 'newton'])
def test_newton_fs_495(method, cec_module_fs_495):
    """test pvsystem.singlediode with different methods on FS495"""
    fs_495 = cec_module_fs_495
    x = pvsystem.calcparams_desoto(
        effective_irradiance=POA, temp_cell=TCELL,
        alpha_sc=fs_495['alpha_sc'], a_ref=fs_495['a_ref'],
        I_L_ref=fs_495['I_L_ref'], I_o_ref=fs_495['I_o_ref'],
        R_sh_ref=fs_495['R_sh_ref'], R_s=fs_495['R_s'],
        EgRef=1.475, dEgdT=-0.0003)
    il, io, rs, rsh, nnsvt = x
    x += (101, )
    pvs = pvsystem.singlediode(*x, method='lambertw')
    out = pvsystem.singlediode(*x, method=method)
    isc, voc, imp, vmp, pmp, ix, ixx, i, v = out.values()
    assert np.isclose(pvs['i_sc'], isc)
    assert np.isclose(pvs['v_oc'], voc)
    # the singlediode method doesn't actually get the MPP correct
    pvs_imp = pvsystem.i_from_v(rsh, rs, nnsvt, vmp, io, il, method='lambertw')
    pvs_vmp = pvsystem.v_from_i(rsh, rs, nnsvt, imp, io, il, method='lambertw')
    assert np.isclose(pvs_imp, imp)
    assert np.isclose(pvs_vmp, vmp)
    assert np.isclose(pvs['p_mp'], pmp)
    assert np.isclose(pvs['i_x'], ix)
    pvs_ixx = pvsystem.i_from_v(rsh, rs, nnsvt, (voc + vmp)/2, io, il,
                                method='lambertw')
    assert np.isclose(pvs_ixx, ixx)


def build_precise_iv_curve_dataframe(file_csv, file_json):
    """
    Reads a precise IV curve parameter set CSV and JSON to create a DataFrame.
    The CSV contains the parameters of the single diode equation which are used
    to generate the JSON data. The data are calculated using [1]_ with 40
    decimal digits of precision in order have at least 16 decimal digits of
    precision when they are stored in JSON. The precision is sufficient for the
    difference between the left and right side of the single diode equation to
    be less than :math:`1 \times 10^{-16}` when the numbers from the JSON are
    read as mpmath floats. The code to generate these IV curve data is from
    [2]_. The data and tests that use this function were added in :pull:`1573`.

    Parameters
    ----------
    file_csv: str
        Path to a CSV file of IV curve parameter sets.

    file_json: str
        Path to a JSON file of precise IV curves.

    Returns
    -------
        A DataFrame with these columns: ``Index``, ``photocurrent``,
        ``saturation_current``, ``resistance_series``, ``resistance_shunt``,
        ``n``, ``cells_in_series``, ``Voltages``, ``Currents``,
        ``diode_voltage``, ``v_oc``, ``i_sc``, ``v_mp``, ``i_mp``, ``p_mp``,
        ``i_x``, ``i_xx`, ``Temperature``, ``Irradiance``, ``Sweep Direction``,
        ``Datetime``, ``Boltzmann``, ``Elementary Charge``, and ``Vth``. The
        columns ``Irradiance``, ``Sweep Direction`` are None or empty strings.

    References
    ----------
    .. [1] The mpmath development team. (2023). mpmath: a Python library for
       arbitrary-precision floating-point arithmetic (version 1.2.1).
       `mpmath <mpmath.org>`_

    .. [2] The ivcurves development team. (2022). Code to generate precise
       solutions to the single diode equation.
       `ivcurves <github.com/cwhanse/ivcurves>`_
    """
    params = pd.read_csv(file_csv)
    curves_metadata = pd.read_json(file_json)
    curves = pd.DataFrame(curves_metadata['IV Curves'].values.tolist())
    curves['cells_in_series'] = curves_metadata['cells_in_series']
    joined = params.merge(curves, on='Index', how='inner',
                          suffixes=(None, '_drop'), validate='one_to_one')
    joined = joined[(c for c in joined.columns if not c.endswith('_drop'))]

    # parse strings to np.float64
    is_array = ['Currents', 'Voltages', 'diode_voltage']
    joined[is_array] = joined[is_array].applymap(
        lambda a: np.asarray(a, dtype=np.float64)
    )
    is_number = ['v_oc', 'i_sc', 'v_mp', 'i_mp', 'p_mp', 'i_x', 'i_xx',
                 'Temperature']
    joined[is_number] = joined[is_number].applymap(np.float64)

    joined['Boltzmann'] = scipy.constants.Boltzmann
    joined['Elementary Charge'] = scipy.constants.elementary_charge
    joined['Vth'] = (
        joined['Boltzmann'] * joined['Temperature']
        / joined['Elementary Charge']
    )

    return joined


@pytest.fixture(scope='function', params=[
    {
        'csv': f'{DATA_DIR}/precise_iv_curves_parameter_sets1.csv',
        'json': f'{DATA_DIR}/precise_iv_curves1.json'
    },
    {
        'csv': f'{DATA_DIR}/precise_iv_curves_parameter_sets2.csv',
        'json': f'{DATA_DIR}/precise_iv_curves2.json'
    }
], ids=[1, 2])
def precise_iv_curves(request):
    file_csv, file_json = request.param['csv'], request.param['json']
    pc = build_precise_iv_curve_dataframe(file_csv, file_json)
    params = ['photocurrent', 'saturation_current', 'resistance_series',
              'resistance_shunt']
    singlediode_params = pc.loc[:, params]
    singlediode_params['nNsVth'] = pc['n'] * pc['cells_in_series'] * pc['Vth']
    return singlediode_params, pc


@pytest.mark.parametrize('method', ['lambertw', 'brentq', 'newton'])
def test_singlediode_precision(method, precise_iv_curves):
    """
    Tests the accuracy of singlediode. ivcurve_pnts is not tested.
    """
    x, pc = precise_iv_curves
    outs = pvsystem.singlediode(method=method, **x)

    assert np.allclose(pc['i_sc'], outs['i_sc'], atol=1e-10, rtol=0)
    assert np.allclose(pc['v_oc'], outs['v_oc'], atol=1e-10, rtol=0)
    assert np.allclose(pc['i_mp'], outs['i_mp'], atol=7e-8, rtol=0)
    assert np.allclose(pc['v_mp'], outs['v_mp'], atol=1e-6, rtol=0)
    assert np.allclose(pc['p_mp'], outs['p_mp'], atol=1e-10, rtol=0)
    assert np.allclose(pc['i_x'], outs['i_x'], atol=1e-10, rtol=0)

    # This test should pass with atol=9e-8 on MacOS and Windows.
    # The atol was lowered to pass on Linux when the vectorized umath module
    # introduced in NumPy 1.22.0 is used.
    assert np.allclose(pc['i_xx'], outs['i_xx'], atol=1e-6, rtol=0)


@pytest.mark.parametrize('method', ['lambertw'])
def test_ivcurve_pnts_precision(method, precise_iv_curves):
    """
    Tests the accuracy of the IV curve points calcuated by singlediode. Only
    methods of singlediode that linearly spaced points are tested.
    """
    x, pc = precise_iv_curves
    pc_i, pc_v = np.stack(pc['Currents']), np.stack(pc['Voltages'])
    ivcurve_pnts = len(pc['Currents'][0])
    outs = pvsystem.singlediode(method=method, ivcurve_pnts=ivcurve_pnts, **x)

    assert np.allclose(pc_i, outs['i'], atol=1e-10, rtol=0)
    assert np.allclose(pc_v, outs['v'], atol=1e-10, rtol=0)


@pytest.mark.parametrize('method', ['lambertw', 'brentq', 'newton'])
def test_v_from_i_i_from_v_precision(method, precise_iv_curves):
    """
    Tests the accuracy of pvsystem.v_from_i and pvsystem.i_from_v.
    """
    x, pc = precise_iv_curves
    pc_i, pc_v = pc['Currents'], pc['Voltages']
    for i, v, (_, x_one_curve) in zip(pc_i, pc_v, x.iterrows()):
        out_i = pvsystem.i_from_v(voltage=v, method=method, **x_one_curve)
        out_v = pvsystem.v_from_i(current=i, method=method, **x_one_curve)

        assert np.allclose(i, out_i, atol=1e-10, rtol=0)
        assert np.allclose(v, out_v, atol=1e-10, rtol=0)


def get_pvsyst_fs_495():
    """
    PVsyst parameters for First Solar FS-495 module from PVSyst-6.7.2 database.

    I_L_ref derived from Isc_ref conditions::

        I_L_ref = (I_sc_ref + Id + Ish) / (1 - d2mutau/(Vbi*N_s - Vd))

    where::

        Vd = I_sc_ref * R_s
        Id = I_o_ref * (exp(Vd / nNsVt) - 1)
        Ish = Vd / R_sh_ref

    """
    return {
        'd2mutau': 1.31, 'alpha_sc': 0.00039, 'gamma_ref': 1.48,
        'mu_gamma': 0.001, 'I_o_ref': 9.62e-10, 'R_sh_ref': 5000,
        'R_sh_0': 12500, 'R_sh_exp': 3.1, 'R_s': 4.6, 'beta_oc': -0.2116,
        'EgRef': 1.5, 'cells_in_series': 108, 'cells_in_parallel': 2,
        'I_sc_ref': 1.55, 'V_oc_ref': 86.5, 'I_mp_ref': 1.4, 'V_mp_ref': 67.85,
        'temp_ref': 25, 'irrad_ref': 1000, 'I_L_ref': 1.5743233463848496
    }

# DeSoto @(888[W/m**2], 55[degC]) = {Pmp: 72.71, Isc: 1.402, Voc: 75.42)


@pytest.mark.parametrize(
    'poa, temp_cell, expected, tol', [
        # reference conditions
        (
            get_pvsyst_fs_495()['irrad_ref'],
            get_pvsyst_fs_495()['temp_ref'],
            {
                'pmp': (get_pvsyst_fs_495()['I_mp_ref'] *
                        get_pvsyst_fs_495()['V_mp_ref']),
                'isc': get_pvsyst_fs_495()['I_sc_ref'],
                'voc': get_pvsyst_fs_495()['V_oc_ref']
            },
            (5e-4, 0.04)
        ),
        # other conditions
        (
            POA,
            TCELL,
            {
                'pmp': 76.262,
                'isc': 1.3868,
                'voc': 79.292
            },
            (1e-4, 1e-4)
        )
    ]
)
@pytest.mark.parametrize('method', ['newton', 'brentq'])
def test_pvsyst_recombination_loss(method, poa, temp_cell, expected, tol):
    """test PVSst recombination loss"""
    pvsyst_fs_495 = get_pvsyst_fs_495()
    # first evaluate PVSyst model with thin-film recombination loss current
    # at reference conditions
    x = pvsystem.calcparams_pvsyst(
        effective_irradiance=poa, temp_cell=temp_cell,
        alpha_sc=pvsyst_fs_495['alpha_sc'],
        gamma_ref=pvsyst_fs_495['gamma_ref'],
        mu_gamma=pvsyst_fs_495['mu_gamma'], I_L_ref=pvsyst_fs_495['I_L_ref'],
        I_o_ref=pvsyst_fs_495['I_o_ref'], R_sh_ref=pvsyst_fs_495['R_sh_ref'],
        R_sh_0=pvsyst_fs_495['R_sh_0'], R_sh_exp=pvsyst_fs_495['R_sh_exp'],
        R_s=pvsyst_fs_495['R_s'],
        cells_in_series=pvsyst_fs_495['cells_in_series'],
        EgRef=pvsyst_fs_495['EgRef']
    )
    il_pvsyst, io_pvsyst, rs_pvsyst, rsh_pvsyst, nnsvt_pvsyst = x
    voc_est_pvsyst = estimate_voc(photocurrent=il_pvsyst,
                                  saturation_current=io_pvsyst,
                                  nNsVth=nnsvt_pvsyst)
    vd_pvsyst = np.linspace(0, voc_est_pvsyst, 1000)
    pvsyst = bishop88(
        diode_voltage=vd_pvsyst, photocurrent=il_pvsyst,
        saturation_current=io_pvsyst, resistance_series=rs_pvsyst,
        resistance_shunt=rsh_pvsyst, nNsVth=nnsvt_pvsyst,
        d2mutau=pvsyst_fs_495['d2mutau'],
        NsVbi=VOLTAGE_BUILTIN*pvsyst_fs_495['cells_in_series']
    )
    # test max power
    assert np.isclose(max(pvsyst[2]), expected['pmp'], *tol)

    # test short circuit current
    isc_pvsyst = np.interp(0, pvsyst[1], pvsyst[0])
    assert np.isclose(isc_pvsyst, expected['isc'], *tol)

    # test open circuit voltage
    voc_pvsyst = np.interp(0, pvsyst[0][::-1], pvsyst[1][::-1])
    assert np.isclose(voc_pvsyst, expected['voc'], *tol)

    # repeat tests as above with specialized bishop88 functions
    y = dict(d2mutau=pvsyst_fs_495['d2mutau'],
             NsVbi=VOLTAGE_BUILTIN*pvsyst_fs_495['cells_in_series'])

    mpp_88 = bishop88_mpp(*x, **y, method=method)
    assert np.isclose(mpp_88[2], expected['pmp'], *tol)

    isc_88 = bishop88_i_from_v(0, *x, **y, method=method)
    assert np.isclose(isc_88, expected['isc'], *tol)

    voc_88 = bishop88_v_from_i(0, *x, **y, method=method)
    assert np.isclose(voc_88, expected['voc'], *tol)

    ioc_88 = bishop88_i_from_v(voc_88, *x, **y, method=method)
    assert np.isclose(ioc_88, 0.0, *tol)

    vsc_88 = bishop88_v_from_i(isc_88, *x, **y, method=method)
    assert np.isclose(vsc_88, 0.0, *tol)


@pytest.mark.parametrize(
    'brk_params, recomb_params, poa, temp_cell, expected, tol', [
        # reference conditions without breakdown model
        (
            (0., -5.5, 3.28),
            (get_pvsyst_fs_495()['d2mutau'],
             VOLTAGE_BUILTIN * get_pvsyst_fs_495()['cells_in_series']),
            get_pvsyst_fs_495()['irrad_ref'],
            get_pvsyst_fs_495()['temp_ref'],
            {
                'pmp': (get_pvsyst_fs_495()['I_mp_ref'] *  # noqa: W504
                        get_pvsyst_fs_495()['V_mp_ref']),
                'isc': get_pvsyst_fs_495()['I_sc_ref'],
                'voc': get_pvsyst_fs_495()['V_oc_ref']
            },
            (5e-4, 0.04)
        ),
        # other conditions with breakdown model on and recombination model off
        (
            (1.e-4, -5.5, 3.28),
            (0., np.Inf),
            POA,
            TCELL,
            {
                'pmp': 79.723,
                'isc': 1.4071,
                'voc': 79.646
            },
            (1e-4, 1e-4)
        )
    ]
)
@pytest.mark.parametrize('method', ['newton', 'brentq'])
def test_pvsyst_breakdown(method, brk_params, recomb_params, poa, temp_cell,
                          expected, tol):
    """test PVSyst recombination loss"""
    pvsyst_fs_495 = get_pvsyst_fs_495()
    # first evaluate PVSyst model with thin-film recombination loss current
    # at reference conditions
    x = pvsystem.calcparams_pvsyst(
        effective_irradiance=poa, temp_cell=temp_cell,
        alpha_sc=pvsyst_fs_495['alpha_sc'],
        gamma_ref=pvsyst_fs_495['gamma_ref'],
        mu_gamma=pvsyst_fs_495['mu_gamma'], I_L_ref=pvsyst_fs_495['I_L_ref'],
        I_o_ref=pvsyst_fs_495['I_o_ref'], R_sh_ref=pvsyst_fs_495['R_sh_ref'],
        R_sh_0=pvsyst_fs_495['R_sh_0'], R_sh_exp=pvsyst_fs_495['R_sh_exp'],
        R_s=pvsyst_fs_495['R_s'],
        cells_in_series=pvsyst_fs_495['cells_in_series'],
        EgRef=pvsyst_fs_495['EgRef']
    )
    il_pvsyst, io_pvsyst, rs_pvsyst, rsh_pvsyst, nnsvt_pvsyst = x

    d2mutau, NsVbi = recomb_params
    breakdown_factor, breakdown_voltage, breakdown_exp = brk_params

    voc_est_pvsyst = estimate_voc(photocurrent=il_pvsyst,
                                  saturation_current=io_pvsyst,
                                  nNsVth=nnsvt_pvsyst)
    vd_pvsyst = np.linspace(0, voc_est_pvsyst, 1000)
    pvsyst = bishop88(
        diode_voltage=vd_pvsyst, photocurrent=il_pvsyst,
        saturation_current=io_pvsyst, resistance_series=rs_pvsyst,
        resistance_shunt=rsh_pvsyst, nNsVth=nnsvt_pvsyst,
        d2mutau=d2mutau, NsVbi=NsVbi,
        breakdown_factor=breakdown_factor, breakdown_voltage=breakdown_voltage,
        breakdown_exp=breakdown_exp
    )
    # test max power
    assert np.isclose(max(pvsyst[2]), expected['pmp'], *tol)

    # test short circuit current
    isc_pvsyst = np.interp(0, pvsyst[1], pvsyst[0])
    assert np.isclose(isc_pvsyst, expected['isc'], *tol)

    # test open circuit voltage
    voc_pvsyst = np.interp(0, pvsyst[0][::-1], pvsyst[1][::-1])
    assert np.isclose(voc_pvsyst, expected['voc'], *tol)

    # repeat tests as above with specialized bishop88 functions
    y = {'d2mutau': recomb_params[0], 'NsVbi': recomb_params[1],
         'breakdown_factor': brk_params[0], 'breakdown_voltage': brk_params[1],
         'breakdown_exp': brk_params[2]}

    mpp_88 = bishop88_mpp(*x, **y, method=method)
    assert np.isclose(mpp_88[2], expected['pmp'], *tol)

    isc_88 = bishop88_i_from_v(0, *x, **y, method=method)
    assert np.isclose(isc_88, expected['isc'], *tol)

    voc_88 = bishop88_v_from_i(0, *x, **y, method=method)
    assert np.isclose(voc_88, expected['voc'], *tol)

    ioc_88 = bishop88_i_from_v(voc_88, *x, **y, method=method)
    assert np.isclose(ioc_88, 0.0, *tol)

    vsc_88 = bishop88_v_from_i(isc_88, *x, **y, method=method)
    assert np.isclose(vsc_88, 0.0, *tol)
