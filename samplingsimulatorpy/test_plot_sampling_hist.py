from samplingsimulatorpy.draw_samples import draw_samples
from samplingsimulatorpy.plot_sampling_hist import plot_sampling_hist
import pandas as pd
import altair as alt
import numpy as np
import pytest

def test_plot_sampling_hist():
    """
    This function tests the plot_sampling_hist function.
    
    Returns:
    --------
    None
        The test should pass and no asserts should be displayed. 
    """
    
    # get helper data
    pop = pd.DataFrame(np.random.normal(0, 1, 1000), columns=["var_name"])
    samples = draw_samples(pop, 100, [5, 20, 50, 100])
    non_num =  pd.DataFrame({'values': [1, 2, 3, 'a', 5]})
    
    test = plot_sampling_hist(samples)
    test_dict = test.to_dict()
    
    # tests exception is raised when 'samples' is not a dataframe
    with pytest.raises(TypeError) as e:
      assert plot_sampling_hist([1, 2, 3])
      assert str(e.value) == "'samples' should be input as a dataframe"
      
    # tests exception is raised when 'samples' have non-numeric values
    with pytest.raises(ValueError) as e:
      assert plot_sampling_hist(non_num)
      assert str(e.value) == "'samples' should only contain numeric values"
        
    # Check samples datafram has correct columns
    assert "replicate" in samples.columns.to_list()
    assert "size" in samples.columns.to_list()
    assert "rep_size" in samples.columns.to_list()
      
    # Check plot is correct type
    assert "altair" in str(type(test)), "the plot should be an Altair object"
    assert "Facet" in str(type(test)), "the plot is facetted"
    
    # Check facet label is correct
    assert test_dict['facet']['field'] == 'size', "Facet label is incorrect"
    
    # Check x-axis is mapped to the correct variable and plotting correctly
    assert test_dict['spec']['mark'] == 'bar', "the plot type is correct"
    assert test_dict['spec']['encoding']['x']['type'] == 'quantitative', "x-axis should have quantitivate values" 
    assert test_dict['spec']['encoding']['x']['field'] == 'var_name', "x-axis is mapped to the wrong variable"
    
    
    # Check y-axis is mapped to the correct variable and plotting correctly
    assert test_dict['spec']['encoding']['y']['type'] == 'quantitative', "y-axis should have quantitivate values"
    assert test_dict['spec']['encoding']['y']['aggregate'] == 'count', "y-axis should represent aggregate count data"
    