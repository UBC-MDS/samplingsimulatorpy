import numpy as np
import pandas as pd

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
    >>> from samplingsimulatorpy import generate_virtual_pop
    >>> pop = generate_virtual_pop(100, "Variable", normal, 0, 1)
    """
    
    if (size <= 0) :
        raise ValueError("Size of population must be a positive integer")

    if (not isinstance(size, int)) :
        raise TypeError("Size of population must be a positive integer")

    try:
        distribution_func()
    except AttributeError:
        print('Please enter a valid distribution function')
        raise

    try:
        distribution_func(*para, size)
    except TypeErro:
        print('Please enter correct number of parameters for the  distribution function')
        raise

    print(distribution_func(*para, size))

generate_virtual_pop(100, np.random.normal, 0, 0.1)