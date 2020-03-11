from samplingsimulatorpy.generate_virtual_pop import generate_virtual_pop
import numpy as np
import pytest


def test_pop():
    assert len(generate_virtual_pop(100, "Height",
                                    np.random.normal, 0, 1)) == 100
    assert len(generate_virtual_pop(200, "Height",
                                    np.random.poisson, 10)) == 200
    assert len(generate_virtual_pop(50, "Height", np.random.gamma, 2, 2)) == 50


def test_neg_size():
    with pytest.raises(ValueError):
        generate_virtual_pop(-100, "Height", np.random.normal, 0, 1)
    with pytest.raises(ValueError):
        generate_virtual_pop(-10, "Height", np.random.normal, 0, 1)
    with pytest.raises(ValueError):
        generate_virtual_pop(-1, "Height", np.random.normal, 0, 1)


def test_not_int():
    with pytest.raises(TypeError):
        generate_virtual_pop(10.5, "Height", np.random.normal, 0, 1)
    with pytest.raises(TypeError):
        generate_virtual_pop(100.5, "Height", np.random.normal, 0, 1)
    with pytest.raises(TypeError):
        generate_virtual_pop(20.5, "Height", np.random.normal, 0, 1)


def test_not_func():
    with pytest.raises(AttributeError):
        generate_virtual_pop(100, "Height", np.random.nomal, 0, 1)
    with pytest.raises(AttributeError):
        generate_virtual_pop(100, "Height", np.random.norma, 0, 1)
    with pytest.raises(AttributeError):
        generate_virtual_pop(200, "Height", np.random.ormal, 0, 1)


def test_not_right_number():
    with pytest.raises(TypeError):
        generate_virtual_pop(100, "Height", np.random.normal, 0, 1, 2)
    with pytest.raises(TypeError):
        generate_virtual_pop(200, "Height", np.random.poisson, 10, 10)
    with pytest.raises(TypeError):
        generate_virtual_pop(50, "Height", np.random.gamma, 2, 2, 3)
