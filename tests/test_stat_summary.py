import numpy as np
from samplingsimulatorpy.stat_summary import stat_summary
import pytest
import pandas as pd

# Get the helper data
new_dict = {'data': ['pop', 'samples'],
            'np.mean': [np.mean([1, 1, 1, 1, 1]), np.mean([1, 1, 1, 1, 1])],
            'np.std': [np.std([1, 1, 1, 1, 1]), np.std([1, 1, 1, 1, 1])]
            }

excepted_df = pd.DataFrame(new_dict).set_index('data')


def test_pop():
    # Test if empty dataframes will get a TypeError
    with pytest.raises(TypeError):
        stat_summary([], [], ['np.mean', 'np.std'])
    # Test if a empty dataframe will get a TypeError
    with pytest.raises(TypeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     [], ['np.mean', 'np.std'])
    # Test if not a list will get a TypeError
    with pytest.raises(TypeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     pd.DataFrame({"A": [12, 4, 5, 44, 1]}), 'np.mean')


def test_value():
    # Test if the output of the dataframe is as expected
    pd.testing.assert_frame_equal(stat_summary
                                  (pd.DataFrame({"A": [1, 1, 1, 1, 1]}),
                                   pd.DataFrame({"A": [1, 1, 1, 1, 1]}),
                                   ['np.mean', 'np.std']), excepted_df)


def test_not_func():
    # Test if passed in a not exist function will get a AttributeError
    with pytest.raises(AttributeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     pd.DataFrame({"A": [12, 4, 5, 44, 1]}), ['np.mea'])
    # Test if passed in a not exist function will get a AttributeError
    with pytest.raises(AttributeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     ['np.mean', 'np.sd'])
