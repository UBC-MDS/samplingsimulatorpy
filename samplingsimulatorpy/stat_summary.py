import numpy as np
import pandas as pd
def stat_summary(population, samples, parameter):
    """
    This function creates a summary stats for population, samples and parameter(s) of interest
    Parameters
    ----------
    population : pd.DataFrame
        The virtual population
    samples : pd.DataFrame
        The drawed samples
    parameter : list
        The list of parameters
    Returns
    -------
    pd.DataFrame
        The summary stats as a dataframe
    Examples
    --------
    >>> from samplingsimulatorpy import stat_summary
    >>> stat_summary(pop, samples, parameter)
    """

    new_dict = {'data' : ['pop', 'samples']}

    for i in range(0, len(parameter)):

        new_dict[parameter[i]] = [eval(parameter[i])(population)[0], eval(parameter[i])(samples)[0]]

    return(pd.DataFrame(new_dict).set_index('data'))