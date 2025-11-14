from physics.importantConstants import Constant as const
pi = const.PI

def revolutionTime(g, r):
    """
    Calculates the time it takes to complete one rotation in a centrifuge given gravity and radius

    Args:
        g (float): Gravitational acceleration in m/s^2
        r (float): Radius in meters
    
    Returns:
        float: Time in seconds to complete 1 revolution
    """
    time = 2 * pi * ((r / g) ** 0.5)
    return time

def centriGrav(t, r):
    """
    Calculates the time it takes to complete one rotation in a centrifuge given gravity and radius

    Args:
        t (float): Time in seconds to complete 1 revolution
        r (float): Radius in meters
    
    Returns:
        float: Gravitational acceleration in m/s^2
    """
    g = (((2 * pi) / t) ** 2) * r
    return g