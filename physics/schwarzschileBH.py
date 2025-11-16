from importantConstants import Constant as const

def areaOfBH(mass):
    """
    Calculates the surface area of a Schwarzschild black hole.
    Args:
        mass (float): Mass of black hole in kg
    
    Returns:
        float: Surface area of the black hole in square meters
    """
    area = (mass ** 2) * ((16 * const.PI * (const.G ** 2)) / (const.c ** 4))
    return area
def effectiveDensity(mass):
    """
    Calculates the effective density of a Schwarzschild black hole.
    Args:
        mass (float): Mass of black hole in kg
    
    Returns:
        float: Effective density of the black hole in kg/m^3
    """
    density = (1 / (mass ** 2)) * ((3 * (const.c ** 6)) / (32 * const.PI * (const.G ** 3)))
    return density