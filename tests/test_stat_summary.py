import numpy as np
from samplingsimulatorpy.stat_summary import stat_summary
import pytest
import pandas as pd

new_dict = {'data': ['pop', 'samples'],
            'np.mean': [np.mean([1, 1, 1, 1, 1]), 1.0],
            'np.std': [0.0, 0.0]
            }

excepted_df = pd.DataFrame(new_dict).set_index('data')


def test_pop():
    with pytest.raises(TypeError):
        stat_summary([], [], ['np.mean', 'np.std'])
    with pytest.raises(TypeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     [], ['np.mean', 'np.std'])
    with pytest.raises(TypeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     pd.DataFrame({"A": [12, 4, 5, 44, 1]}), 'np.mean')


def test_value():
    pd.testing.assert_frame_equal(stat_summary
                                  (pd.DataFrame({"A": [1, 1, 1, 1, 1]}),
                                   pd.DataFrame({"A": [1, 1, 1, 1, 1]}),
                                   ['np.mean', 'np.std']), excepted_df)


def test_not_func():
    with pytest.raises(AttributeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     pd.DataFrame({"A": [12, 4, 5, 44, 1]}), ['np.mea'])
    with pytest.raises(AttributeError):
        stat_summary(pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     pd.DataFrame({"A": [12, 4, 5, 44, 1]}),
                     ['np.mean', 'np.sd'])
