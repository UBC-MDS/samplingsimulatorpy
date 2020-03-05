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
        A dataframe containing the sample numbers and sample values
    Examples
    --------
    >>> pop = generate_virtual_pop(100, "Variable", normal, 0, 1)
    >>> samples = draw_samples(pop, 3, [5, 10, 15, 20])
    """
    samples = []
    rep_list = []

    for i in range(reps):
        for j in n_s:
            sample = np.random.choice(np.squeeze(pop.values), size=j)
            samples.append(sample)
        
    samples = np.concatenate(samples)
    sizes = [n for n in n_s for i in range(n) for j in range(reps)]
    
    for i in n_s:
        rep_list = rep_list + [j for j in range(1, reps+1) for k in range(i)]
    
    return(pd.DataFrame({"replicate":rep_list, list(pop.columns)[0]:samples, "size":sizes, "rep_size":np.full(len(samples), reps)}))