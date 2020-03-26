from samplingsimulatorpy.generate_virtual_pop import generate_virtual_pop
import numpy as np
import pytest


def test_pop():
    # Check if the length of the dataframe is as expected
    assert len(generate_virtual_pop(100, "Height",
                                    np.random.normal, 0, 1)) == 100
    assert len(generate_virtual_pop(200, "Height",
                                    np.random.poisson, 10)) == 200
    assert len(generate_virtual_pop(50, "Height", np.random.gamma, 2, 2)) == 50


def test_neg_size():
    # Check if the negative size will give a ValueError
    with pytest.raises(ValueError):
        generate_virtual_pop(-100, "Height", np.random.normal, 0, 1)
    with pytest.raises(ValueError):
        generate_virtual_pop(-10, "Height", np.random.normal, 0, 1)
    with pytest.raises(ValueError):
        generate_virtual_pop(-1, "Height", np.random.normal, 0, 1)


def test_not_int():
    # Check if the float number size will give a ValueError
    with pytest.raises(TypeError, match='Size of population must be a positive integer'):
        generate_virtual_pop(10.5, "Height", np.random.normal, 0, 1)
    with pytest.raises(TypeError, match='Size of population must be a positive integer'):
        generate_virtual_pop(100.5, "Height", np.random.normal, 0, 1)
    with pytest.raises(TypeError, match='Size of population must be a positive integer'):
        generate_virtual_pop(20.5, "Height", np.random.normal, 0, 1)


def test_not_func():
    # Check if the not exist function will give a AttributeError
    with pytest.raises(AttributeError):
        generate_virtual_pop(100, "Height", np.random.nomal, 0, 1)
    with pytest.raises(AttributeError):
        generate_virtual_pop(100, "Height", np.random.norma, 0, 1)
    with pytest.raises(AttributeError):
        generate_virtual_pop(200, "Height", np.random.ormal, 0, 1)


def test_not_right_number():
    # Check if the incorrect number of parameters will give a TypeError
    with pytest.raises(TypeError, match='Please enter a valid distribution '+
              'function with correct number of parameters for ' +
              'the distribution function'):
        generate_virtual_pop(100, "Height", np.random.normal, 0, 1, 2)
    with pytest.raises(TypeError, match='Please enter a valid distribution '+
              'function with correct number of parameters for ' +
              'the distribution function'):
        generate_virtual_pop(200, "Height", np.random.poisson, 10, 10)
    with pytest.raises(TypeError, match='Please enter a valid distribution '+
              'function with correct number of parameters for ' +
              'the distribution function'):
        generate_virtual_pop(50, "Height", np.random.gamma, 2, 2, 3)
