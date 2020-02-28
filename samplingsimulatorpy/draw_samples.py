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