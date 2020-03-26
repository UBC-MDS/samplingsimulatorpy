import numpy as np
import pandas as pd


def stat_summary(population, samples, parameter):
    """
    This function creates a summary stats for population,
    samples and parameter(s) of interest

    Parameters
    ----------
    population : pd.DataFrame
        The virtual population
    samples : pd.DataFrame
        The drawed samples
    parameter : list
        The list of parameters

    Raises
    -------
    TypeError
        population input should be a dataframe contains value
    TypeError
        samples input should be a dataframe contains value
    TypeError
        parameter input should be a list contains value
    AttributeError
        parameter is interest for the summary stats

    Returns
    -------
    pd.DataFrame
        The summary stats as a dataframe

    Examples
    --------
    >>> from samplingsimulatorpy.stat_summary import stat_summary
    >>> stat_summary(pop, samples, [np.mean, np.std])
    """

    if (len(population) <= 0 or not isinstance(population, pd.DataFrame)):
        raise TypeError("Population input is not a valid data frame")

    if (len(samples) <= 0 or not isinstance(samples, pd.DataFrame)):
        raise TypeError("Samples input is not a valid data frame")

    if (len(parameter) <= 0 or not isinstance(parameter, list)):
        raise TypeError("Parameter input is not a valid list")

    new_dict = {'data': ['pop', 'samples']}

    for func in parameter:

        try:
            pop_para = func(population)[0]
            samples_para = func(samples.iloc[:, 1])
        except AttributeError:
            raise AttributeError

        new_dict[func.__name__] = [pop_para, samples_para]

    return(pd.DataFrame(new_dict).set_index('data'))
