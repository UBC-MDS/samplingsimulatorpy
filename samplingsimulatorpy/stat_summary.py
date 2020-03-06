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

    if (len(population) <=0 or not isinstance(population, pd.DataFrame)):
        raise TypeError("Population input is not a valid data frame")

    if (len(samples) <=0 or not isinstance(samples, pd.DataFrame)):
        raise TypeError("Samples input is not a valid data frame")

    if (len(parameter) <=0 or not isinstance(parameter, list)):
        raise TypeError("Parameter input is not a valid list")

    new_dict = {'data' : ['pop', 'samples']}

    for i in range(0, len(parameter)):

        new_dict[parameter[i]] = [eval(parameter[i])(population)[0], eval(parameter[i])(samples)[0]]

    return(pd.DataFrame(new_dict).set_index('data'))

print(stat_summary(pd.DataFrame(np.random.normal(0,1,100)), pd.DataFrame(np.random.normal(0,1,100)), ['np.mean', 'np.std']))