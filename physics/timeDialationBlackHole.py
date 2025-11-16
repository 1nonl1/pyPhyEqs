from physics.importantConstants import Constant as const
c = const.c
g = const.G

def calculate(M, r, timeNearBlackHole):
    """
    Calculates the time passed for someone observing someone else near a black hole.

    Args:
        M (int): Mass of the black hole in Kg
        r (int): Distance from the center of the black hole in m
        timeNearBlackHole (int): Time spent near the black hole in seconds

    Returns:
        float: Time passed from someone not near the blackhole based on the time someone near a black hole experiences.
    """
    hi = (2 * (g * M)) / (r * pow(c, 2))
    tDistantObserver = timeNearBlackHole / (1 - hi) ** 0.5
    return abs(tDistantObserver)

mass = int(input("Enter mass of Black Hole (kg): "))
radius = int(input("Enter the distance from the center of the Black Hole (m): "))
timeNearBH = int(input("Enter the time near the Black Hole (s): "))

print(f"Time passed from distant observer: {calculate(mass, radius, timeNearBH)} seconds")
