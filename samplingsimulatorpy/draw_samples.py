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
    >>> pop = generate_virtual_pop(100, "Variable", normal, 0, 1)
    >>> samples = draw_samples(pop, 3, [5, 10, 15, 20])
    """
    samples = pd.DataFrame(index=range(sum(n_s) * reps), columns=["replicate", list(pop.columns)[0], "size", "rep_size"])
    
    for i in (0, (len(n_s)-1)):
        for j in range(0, (sum(n_s) * reps)):
            samples["replicate"][j] = i
            samples[list(pop.columns)[0]][j] = np.random.choice(np.squeeze(pop.values))
            samples["size"][j] = n_s[i]
            
    samples["rep_size"] = reps
    
    return(samples)