from samplingsimulatorpy.plot_sample_hist import plot_sample_hist
from samplingsimulatorpy.draw_samples import draw_samples
import pandas as pd
import altair as alt
import numpy as np
import pytest

def test_plot_sample_hist():
    """
    This function tests the plot_sample_hist function.
    
    Returns:
    --------
    None
        The test should pass and no asserts should be displayed. 
    """
    
    # get helper data
    pop = pd.DataFrame(np.random.normal(0, 1, 1000), columns=["var_name"])
    samples = draw_samples(pop, 3, [5, 10, 15, 20])
    p_non_num =  pd.DataFrame({'values': [1, 2, 3, 'a', 5]})
    
    test = plot_sample_hist(pop, samples)
    test_dict = test.to_dict()
    
    # tests exception is raised when 'pop' or 'samples' is not a dataframe
    with pytest.raises(TypeError) as e:
      assert plot_sample_hist([1, 2, 3], samples)
      # assert str(e.value) == "'pop' should be input as a dataframe"
      
    with pytest.raises(TypeError) as e:
      assert plot_sample_hist(pop, [1, 2, 3])
      # assert str(e.value) == "'samples' should be input as a dataframe"
      
    # tests exception is raised when 'pop' is an empty dataframe
    with pytest.raises(TypeError) as e:
      assert plot_sample_hist(pd.DataFrame(), samples)
      # assert str(e.value) == "'pop' appears to be an empty dataframe"
      
    # tests exception is raised when 'pop' or 'samples' have non-numeric values
    with pytest.raises(ValueError) as e:
      assert plot_sample_hist(p_non_num, samples)
      # assert str(e.value) == "'pop' should only contain numeric values"
      
    with pytest.raises(ValueError) as e:
      assert str(e.value) == "'samples' should only contain numeric values"
      assert plot_sample_hist(pop, p_non_num)
      
    # Check plot is correct type
    assert "altair" in str(type(test)), "the plot should be an Altair object"
    assert "altair" in str(type(test)), "the plot is not facetted"
    
    # Check facet label is correct
    assert test_dict['facet']['column']['field'] == 'Sample Distribution Histograms', "Facet label is incorrect"
    
    # Check x-axis is mapped to the correct variable and plotting correctly
    assert test_dict['spec']['encoding']['x']['type'] == 'quantitative', "x-axis should have quantitivate values"
    assert test_dict['spec']['encoding']['x']['field'] == 'var_name', "x-axis is mapped to the wrong variable"
    assert test_dict['spec']['encoding']['x']['bin'] == True, "x-axis should be binned for histogram plots"
    
    # Check y-axis is mapped to the correct variable and plotting correctly
    assert test_dict['spec']['encoding']['y']['type'] == 'quantitative', "y-axis should have quantitivate values"
    assert test_dict['spec']['encoding']['y']['aggregate'] == 'count', "y-axis should represent aggregate count data"
    assert test_dict['spec']['encoding']['y']['title'] == 'Count', "y-axis title is incorrect"