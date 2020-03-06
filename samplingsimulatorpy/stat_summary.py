import numpy as np

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
    print(np.mean(population))
