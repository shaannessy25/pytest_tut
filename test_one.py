# test_one.py
import math
import pytest



def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless). 
    """

    T_HALF = 5730
    DECAY_CONSTANT = -0.693
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF

def test_get_age_carbon_14_dating():
    with pytest.raises(TypeError):
        get_age_carbon_14_dating('0.35')
        get_age_carbon_14_dating([0.35])
        get_age_carbon_14_dating(0)

    assert round(get_age_carbon_14_dating(0.35), 2) == 8680.35







def calculate_kinetic_energy(mass, velocity): 
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2

def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average():
    numbers = [1, 2, 3, 4, 5, 6]
    assert get_average(numbers) == 3.5

def test_calculate_kinetic_energy():
    mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80
