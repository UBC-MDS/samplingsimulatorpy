def generate_virtual_pop(size, distribution_func, *para):

    """
    Create a population

    Parameters
    ----------
    size : int
        The number of population 
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