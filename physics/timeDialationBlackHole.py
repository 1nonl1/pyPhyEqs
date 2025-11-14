from physics.importantConstants import Constant as const
c = const.SPEED_OF_LIGHT
g = const.GRAVITATIONAL_CONST

def calculate(M, r, timeNearBlackHole):
    """
    
    M: Mass of the black hole (kg)
    c: Speed of light (m/s)
    G: Gravitational constant (m^3 kg^-1 s^-2)
    r: Radial distance from the center of the black hole (m)
    """
    hi = (2 * (g * M)) / (r * pow(c, 2))
    tDistantObserver = timeNearBlackHole / (1 - hi) ** 0.5
    return abs(tDistantObserver)

mass = int(input("Enter mass of Black Hole (kg): "))
radius = int(input("Enter the distance from the center of the Black Hole (m): "))
timeNearBH = int(input("Enter the time near the Black Hole (s): "))
print(f"Time passed from distant observer: {calculate(mass, radius, timeNearBH)} seconds")