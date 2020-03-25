import pandas as pd
import numpy as np


def draw_samples(pop, reps, sample_size):

    """
    Draws samples of various sizes from a population

    Parameters
    ----------
    pop : pd.DataFrame
        The virtual population as a dataframe
    reps : integer
        The number of replications for each sample size as an integer
    sample_size : list
        The sample size for each one of the samples as a list

    Returns
    -------
    pd.DataFrame
        A dataframe containing the sample numbers and sample values

    Raises
    -------
    TypeError
        pop input is a valid data frame
    TypeError
        pop name input is a valid string
    TypeError
        reps input is an integer
    ValueError
        reps input is greater than 0
    TypeError
        sample_size array contains only integers

    Examples
    --------
    >>> pop = generate_virtual_pop(100, np.random.normal, 0, 1)
    >>> samples = draw_samples(pop, 3, [5, 10, 15, 20])
    """

    # Check population input is a date frame with at least one value
    if (len(pop) <= 0 or not isinstance(pop, pd.DataFrame)):
        raise TypeError("Population input "
                        "is not a valid data frame")

    # Check that population input has a string column name
    if (not isinstance(list(pop.columns)[0], str)):
        raise TypeError("Population input name "
                        "is not a valid string")

    # Check number of reps is an integer
    if not isinstance(reps, int):
        raise TypeError("Number of replications "
                        "input must be an integer value")

    # Check number of reps is positive
    if reps <= 0:
        raise ValueError("Number of replications must be greater than 0")

    # Check all values in sample size array are integers
    for i in sample_size:
        if not isinstance(i, int):
            raise TypeError("At least one value in sample size "
                            "array is not an integer value")

    samples = []
    rep_list = []

    for i in range(reps):
        for j in sample_size:
            value = pop[list(pop.columns)[0]].tolist()
            sample = np.random.choice(value, size=j)
            samples.append(sample)

    samples = np.concatenate(samples)
    s = [n for n in sample_size for i in range(n) for j in range(reps)]

    for i in sample_size:
        rep_list = rep_list + [j for j in range(1, reps + 1) for k in range(i)]

    return(pd.DataFrame({"replicate": rep_list, list(pop.columns)[0]: samples,
                        "size": s, "rep_size": np.full(len(samples), reps)}))
