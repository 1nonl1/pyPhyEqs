import matplotlib.pyplot as plt
from physics.importantConstants import Constant as const
c = const.c


def calculateTime(velocity, observerTime):
    """
    Calculates the time experienced by the stationary observer given the velocity and time experienced by the moving observer
    Args:
        velocity (float): Velocity as a percent of the speed of light (0-99.99)
        observerTime (float): Time experienced by the moving observer in years

    Returns:
        float: Time passed by someone stationary watching the moving person
    """
    #Observer time is the one who is actually moving
    #t is how much time someone from the stationary frame would observe like earthians
    velocity = (velocity / 100) * c
    t = observerTime / (1 - (pow(velocity, 2)/ pow(c, 2))) ** 0.5
    return t