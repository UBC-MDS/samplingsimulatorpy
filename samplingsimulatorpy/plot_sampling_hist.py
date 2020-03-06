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
        The samples as a dataframe
        
    Returns
    -------
    altair.vegalite.v3.api.FacetChart
        A facet chart of the sampling distribution plots
        
    Examples
    --------
    >>> pop = generate_virtual_pop(1000, "Variable", normal, 0, 1)
    >>> samples = draw_samples(pop, 100, [5, 10, 15, 20])
    >>> plot_sampling_hist(samples)
    """
    
    summary = samples.groupby(['replicate', 'size', 'rep_size']).mean()
    summary = summary.reset_index()
    p = alt.Chart(summary).mark_bar().encode(
        x=alt.X('values:Q', title = "mean of sampling distribution", bin = True),
        y=alt.Y('count()')).facet(
        facet='size', columns = 2)
    return p