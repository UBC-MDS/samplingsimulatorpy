from samplingsimulatorpy.generate_virtual_pop import generate_virtual_pop
from samplingsimulatorpy.draw_samples import draw_samples
import numpy as np
from pytest import raises


def test_draw_samples():
    """
    This function tests the draw_samples function.
    Returns:
    --------
    None
        All tests should pass and no asserts or errors should be raised.
    """

    # Create helper data
    pop = generate_virtual_pop(10, "Height", np.random.normal, 0, 1)
    pop1 = generate_virtual_pop(100000, "Height", np.random.exponential, 0)
    pop2 = generate_virtual_pop(100, "Height", np.random.normal, 0, 1)
    pop3 = generate_virtual_pop(10, "Height", np.random.poisson, 0)
    pop4 = generate_virtual_pop(100, 42, np.random.normal, 0, 1)

    # Check that column names are as expected
    assert(all(draw_samples(pop1, 1, [1]).columns.values == (["replicate",
                                                             "Height",
                                                              "size",
                                                              "rep_size"])))
    # Check that data frame has correct row and column length
    assert(len(draw_samples(pop2, 2, [2, 3, 4])) == 18)
    assert(len(draw_samples(pop3, 2, [2, 3]).columns) == 4)

    # Check that non valid data frame will raise TypeError
    with raises(TypeError, match="Population input is not a valid data frame"):
        draw_samples(np.array([1, 2, 3]), 1, [2, 3])

    # Check that if pop input is not string TypeError will be raised
    with raises(TypeError, match="Population input name "
                "is not a valid string"):
        draw_samples(pop4, 2, [5, 10, 15, 20])

    # Check that if rep input is non-integer TypeError is raised
    with raises(TypeError, match="Number of replications "
                "input must be an integer value"):
        draw_samples(pop, 1.5, [2, 3])

    # Check that if rep input is 0 or less ValueError is raised
    with raises(ValueError, match="Number of replications "
                "must be greater than 0"):
        draw_samples(pop, 0, [2, 3])

    # Check if not all sample array values are integers raise TypeError
    with raises(TypeError, match="At least one value in sample "
                "size array is not an integer value"):
        draw_samples(pop, 3, [2, 3, 4.5])
