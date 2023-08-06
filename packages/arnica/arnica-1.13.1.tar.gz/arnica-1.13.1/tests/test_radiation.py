"""
Functional Testing of the p1 radiation solver
"""
from copy import deepcopy
import numpy as np
import pytest

from arnica.solvers_2d.radiation import main_p1_solver
# from tests_scripts.parameters_tests import (DATA_DIR,
#                                             OUT_DIR)
from tests.parameters_tests import (DATA_DIR, OUT_DIR)

GENERATE_TEST_DATA = False
#GENERATE_TEST_DATA = True


@pytest.fixture
def test_case_cyl():
    """
    Computational setup corresponding to the test case used for validation:
        >   2 concentric cylinder with grey gas
        >   (Modest's book, 2nd edition, p. 477)

    """
    t_west = 500.
    t_east = 1500.

    mesh_cyl = {"kind": 'cyl',
                "r_min": 1.,
                "r_max": 2.,
                "theta_min": 0.,
                "theta_max": 2. * np.pi,
                "n_pts_rad": 5
                }

    # Boundary conditions
    # Default values
    boundary = {"North": {"type": "Periodic", 'Values': {}},
                "West": {"type": "Periodic", 'Values': {}},
                "South": {"type": "Periodic", 'Values': {}},
                "East": {"type": "Periodic", 'Values': {}}}

    # Overwrite WE BCs with Robin conditions
    boundary["West"]["type"] = "Robin"
    boundary["West"]["Values"] = {"Emissivity": 1.,
                                  "Wall_temperature": 500.}

    boundary["East"]["type"] = "Robin"
    boundary["East"]["Values"] = {"Emissivity": 1.,
                                  "Wall_temperature": 1500.}

    # Input fields: Temperature, pressure, etc.
    field = {"absorption_coefficient": 1.,
             "temperature": [t_west, t_east]}

    return {"boundaries": boundary, "field": field, "mesh": mesh_cyl}


def test_p1_solver_is_running(test_case_cyl):
    """
    Test if the solver is running
    """
    # params = deepcopy(test_case_cyl)
    params = test_case_cyl
    q_inner, _ = main_p1_solver(params)
    assert q_inner


def test_p1_solver_q_inner_is_correct(test_case_cyl):
    """
    Test if the solver is giving good results for q_inner at several optical
    lengths
    """
    params = deepcopy(test_case_cyl)
    abs_coeff = np.linspace(1, 6, 10)
    data_path = "%s/p1/q_inner_test_data.npz" %DATA_DIR

    q_inner_res = []
    for kappa in abs_coeff:
        params['field']['absorption_coefficient'] = kappa
        q_inner, _ = main_p1_solver(params)
        q_inner_res.append(q_inner)

    if GENERATE_TEST_DATA:
        np.savez(data_path, q_inner=q_inner_res)
    else:
        data = np.load(data_path)
        q_inner_saved = data["q_inner"]
        print(q_inner_saved)
        print(q_inner_res)
        
        assert np.allclose(q_inner_saved, np.array(q_inner_res), atol=1e-5)


def test_p1_solver_fields_are_correct(test_case_cyl):
    """
    Test if the solver is giving good results for all the fields!
    """
    params = deepcopy(test_case_cyl)
    # data_path = "%s/p1/fields_test_data.npz" %DATA_DIR
    data_path = DATA_DIR +  "/p1/fields_%s_test_data.npz"
    params['field']['absorption_coefficient'] = 3.
    _, results = main_p1_solver(params)

    if GENERATE_TEST_DATA:
        for key in results.keys():
            try:
                np_data = results[key].toarray()
            except AttributeError:
                np_data = results[key]

            np.savez(data_path % key, data=np_data)
    else:
        for key in results.keys():
            data = np.load(data_path % key)
            res_saved = data['data']
            res = np.array(results[key])
            assert np.allclose(res, res_saved)
