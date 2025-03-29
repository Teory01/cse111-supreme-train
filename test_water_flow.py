from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction

                      
# This function tests the water_column_height function with different inputs
def test_water_column_height():
    # Test with 0.0 for both inputs
    assert water_column_height(0.0, 0.0) == approx(0.0)
    # Test with 0.0 for the first input and 10.0 for the second input
    assert water_column_height(0.0, 10.0) == approx(7.5)
    # Test with 25.0 for the first input and 0.0 for the second input
    assert water_column_height(25.0, 0.0) == approx(25.0)
    # Test with 48.3 for the first input and 12.8 for the second input
    assert water_column_height(48.3, 12.8) == approx(57.9)

# This function tests the pressure_gain_from_water_height function with different water heights
def test_pressure_gain_from_water_height():
    # Test with water height of 0.0
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    # Test with water height of 30.2
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    # Test with water height of 50.0
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

# This function tests the pressure_loss_from_pipe function with different inputs
def test_pressure_loss_from_pipe():
    # Test with flow rate = 0.048692, pipe length = 0.00, pipe diameter = 0.018, fluid velocity = 1.75
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    # Test with flow rate = 0.048692, pipe length = 200.00, pipe diameter = 0.000, fluid velocity = 1.75
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    # Test with flow rate = 0.048692, pipe length = 200.00, pipe diameter = 0.018, fluid velocity = 0.00
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    # Test with flow rate = 0.048692, pipe length = 200.00, pipe diameter = 0.018, fluid velocity = 1.75
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    # Test with flow rate = 0.048692, pipe length = 200.00, pipe diameter = 0.018, fluid velocity = 1.65
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    # Test with flow rate = 0.286870, pipe length = 1000.00, pipe diameter = 0.013, fluid velocity = 1.65
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    # Test with flow rate = 0.286870, pipe length = 1800.75, pipe diameter = 0.013, fluid velocity = 1.65
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)


# This function tests the pressure_loss_from_fittings function with different inputs
def test_pressure_loss_from_fittings():
    # Test with 0.00 as the first input and 3 as the second input
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    # Test with 1.65 as the first input and 0 as the second input
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    # Test with 1.65 as the first input and 2 as the second input
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    # Test with 1.75 as the first input and 2 as the second input
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    # Test with 1.75 as the first input and 5 as the second input
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

# Define a function to test the reynolds_number function
def test_reynolds_number():
    # Test the reynolds_number function with a velocity of 0.048692 and a diameter of 0
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    # Test the reynolds_number function with a velocity of 0.048692 and a diameter of 1.65
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    # Test the reynolds_number function with a velocity of 0.048692 and a diameter of 1.75
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    # Test the reynolds_number function with a velocity of 0.286870 and a diameter of 1.65
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    # Test the reynolds_number function with a velocity of 0.286870 and a diameter of 1.75
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

import pytest
from water_flow import pressure_loss_from_pipe_reduction

def test_pressure_loss_from_pipe_reduction():
    """Test pressure_loss_from_pipe_reduction with predefined values."""
    
    # Test case 1: Zero fluid velocity
    result1 = pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692)
    assert pytest.approx(result1, abs=0.001) == 0.000

    # Test case 2: Fluid velocity = 1.65, Reynolds number = 471729
    result2 = pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    assert pytest.approx(result2, abs=0.001) == -163.744

    # Test case 3: Fluid velocity = 1.75, Reynolds number = 500318
    result3 = pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)
    assert pytest.approx(result3, abs=0.001) == -184.182

# Call pytest to execute the tests
pytest.main(["-v", "--tb=line", "-rN", __file__])

