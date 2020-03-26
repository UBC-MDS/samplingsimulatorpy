import numpy as np
from samplingsimulatorpy.generate_virtual_pop import generate_virtual_pop
from samplingsimulatorpy.draw_samples import draw_samples
from samplingsimulatorpy.stat_summary import stat_summary
import pytest
import pandas as pd

# Get the helper data
pop1 = generate_virtual_pop(100, "Height", np.random.normal, 0, 1)
pop2 = generate_virtual_pop(10, "Height", np.random.poisson, 0)
samples1 = draw_samples(pop1, 2, [2, 3, 4])
samples2 = draw_samples(pop2, 2, [2, 3])


def test_pop():
    # Test if empty dataframes will get a TypeError
    with pytest.raises(TypeError,
                       match="Population input is not a valid data frame"):
        stat_summary([], [], [np.mean, np.std])
    # Test if a empty dataframe will get a TypeError
    with pytest.raises(TypeError,
                       match="Samples input is not a valid data frame"):
        stat_summary(pop1, [], [np.mean, np.std])
    # Test if not a wrong function will get a TypeError
    with pytest.raises(TypeError, match="Parameter input is not a valid list"):
        stat_summary(pop1, samples1, 'np.mean')


def test_value():
    # Test if the output of the dataframe is as expected
    assert(len(stat_summary(pop1, samples1, [np.mean, np.std])) == 2)
    assert(len(stat_summary(pop1, samples1, [np.mean, np.std]).columns) == 2)
    assert(len(stat_summary(pop2, samples2, [np.mean, np.std, np.max])) == 2)
    assert(len(stat_summary(pop2, samples2,
           [np.mean, np.std, np.min]).columns) == 3)


def test_not_func():
    # Test if passed in a not exist function will get a AttributeError
    with pytest.raises(AttributeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     samples1, [np.mea])
    # Test if passed in a not exist function will get a AttributeError
    with pytest.raises(AttributeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     samples1, [np.mean, np.sd])
