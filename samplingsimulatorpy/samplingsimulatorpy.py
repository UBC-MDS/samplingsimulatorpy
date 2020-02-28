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