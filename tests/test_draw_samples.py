from samplingsimulatorpy.generate_virtual_pop import generate_virtual_pop
from samplingsimulatorpy.draw_samples import draw_samples
import numpy as np
from pytest import raises

def test_draw_samples():
    
    pop = generate_virtual_pop(10, np.random.normal, 0, 1)
    pop1 = generate_virtual_pop(100000, np.random.exponential, 0)
    pop2 = generate_virtual_pop(100, np.random.normal, 0, 1)
    pop3 = generate_virtual_pop(10, np.random.poisson, 0)
    
    assert(all(draw_samples(pop1, 1, [1]).columns.values == (["replicate", "exponential", "size", "rep_size"])))
    assert(len(draw_samples(pop2, 2, [2, 3, 4])) == 18)
    assert(len(draw_samples(pop3, 2, [2, 3]).columns) == 4)
    
    with raises(TypeError, match = "Population input is not a valid data frame"):
        draw_samples(np.array([1, 2, 3]), 1, [2, 3])

    with raises(TypeError, match = "Number of replications input must be an integer value"):
        draw_samples(pop, 1.5, [2, 3])
        
    with raises(ValueError, match = "Number of replications must be greater than 0"):
        draw_samples(pop, 0, [2, 3])

    with raises(TypeError, match = "At least one value in sample size array is not an integer value"):
        draw_samples(pop, 3, [2, 3, 4.5])