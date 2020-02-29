def plot_sample_hist(pop, samples, var_name, n_s):

    """
    Create a sample histogram from a population

    Parameters
    ----------
    pop : pd.DataFrame
        The virtual population as a dataframe
    samples : pd.DataFrame
        The samples as a dataframe
    var_name : string
        The name of a variable of interest
    var_name : list
        A list of sample sizes to try

    Returns
    -------
    altair.vegalite.v3.api.Chart
        A grid of the sample distribution plots

    Examples
    --------
    >>> from convertempPy import convertempPy as tmp
    >>> pop = generate_virtual_pop(100, "Variable", normal, 0, 1)
    >>> samples = draw_samples(pop, 3, [5, 10, 15, 20])
    >>> plot_sample_hist(pop, samples, var_name, [5, 10, 15, 20])
    """
    
def draw_samples(pop, reps, n_s):

    """
    Draws samples of various sizes from a population

    Parameters
    ----------
    pop : pd.DataFrame
        The virtual population as a dataframe
    reps : integer
        The number of replication for each sample size as an integer
    n_s : list
        The sample size for each one of the samples as a list

    Returns
    -------
    pd.DataFrame
        A two column dataframe containing the sample numbers and sample values

    Examples
    --------
    >>> from convertempPy import convertempPy as tmp
    >>> pop = generate_virtual_pop(100, "Variable", normal, 0, 1)
    >>> samples = draw_samples(pop, 3, [5, 10, 15, 20])
    """

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
    >>> from convertempPy import convertempPy as tmp
    >>> stat_summary(pop, samples, parameter)
    """

def generate_virtual_pop(size, distribution_func, *para):

    """
    Create a virtual population

    Parameters
    ----------
    size : int
        The size of the virtual population 
    distribution_func : func
        The function that 
    *para : int
        The parameters the distribution_func is using

    Returns
    -------
    pd.DataFrame
        The virtual population as a dataframe

    Examples
    --------
    >>> from convertempPy import convertempPy as tmp
    >>> pop = generate_virtual_pop(100, "Variable", normal, 0, 1)
    """