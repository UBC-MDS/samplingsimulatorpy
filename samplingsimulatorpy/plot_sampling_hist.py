import numpy as np
import pandas as pd
import altair as alt

def plot_sampling_hist(samples):

    """
    Create a gird of sampling distribution histogram of the mean 
    of different sample sizes drawn from a population
    
    Parameters
    ----------
    samples : pd.DataFrame
        The samples as a dataframe. 
        It should be an object created by `draw_samples` function. 
        Otherwise, it should follow the column names of the output of the `draw_samples` function. 
        If not, the function may not work. 
        
    Returns
    -------
    altair.vegalite.v3.api.FacetChart
        A facet chart of the sampling distribution plots
    
    Raises
    -------
    TypeError
        if samples input is not a valid data frame    
    ValueError
        samples input should only contain numeric values
        
    Examples
    --------
    >>> pop = generate_virtual_pop(1000, "Variable", normal, 0, 1)
    >>> samples = draw_samples(pop, 100, [5, 10, 15, 20])
    >>> plot_sampling_hist(samples)
    """
    
    # check the validity of input
    if not isinstance(samples, pd.DataFrame):
        raise TypeError("'samples' should be a dataframe")
    
    if not np.issubdtype(samples.to_numpy().dtype, np.number):
        raise ValueError("'samples' should only contain numeric values")
        
    if not samples.shape[1]==4:
        raise ValueError("""The shape of the input samples dataframe should have the 
                     the same shape with the output of draw_samples function""")

    if "replicate" not in samples.columns.to_list():
        raise ValueError("""The input samples dataframe should have the 
                        the same column names with the output of draw_samples function""")

    if "size" not in samples.columns.to_list():
        raise ValueError("""The input samples dataframe should have the 
                    the same column names with the output of draw_samples function""")

    if "rep_size" not in samples.columns.to_list():
        raise ValueError("""The input samples dataframe should have the 
                    the same column names with the output of draw_samples function""") 
    
    summary = samples.groupby(['replicate', 'size', 'rep_size']).mean()
    summary = summary.reset_index()
    x_max = summary.iloc[:,3].max()
    x_min = summary.iloc[:,3].min()
    p = alt.Chart(summary).mark_bar().encode(
        x=alt.X(f"{summary.columns[3]}:Q", title = "mean of sampling distribution",bin = alt.Bin(extent=[x_min, x_max], step=1/10)),
        y=alt.Y('count()')).facet(
        facet='size', columns = 2)
    return p
