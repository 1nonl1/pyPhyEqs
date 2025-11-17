import math
import matplotlib.pyplot as plt

g = 9.807 #m/s^2
def calcDistanceNoAirFric(Vi, a, h):
    """
    Calculates the distance traveled by a projectile without air friction.
    Args:
        Vi (float): Initial velocity in m/s
        a (float): Angle of launch in degrees
        h (float): Inital height in meters
    Returns: 
        float: Distance traveled in meters
    """
    Viy = Vi * (math.sin(math.radians(a)))
    Vix = Vi * (math.cos(math.radians(a)))
    totalTime = ((Viy + (((Viy ** 2) + (2 * (g * h))) ** 0.5)) / g)
    distance = Vix * totalTime
    return distance

def calcTimeNoAirFric(Vi, a, h):
    Viy = Vi * (math.sin(math.radians(a)))
    totalTime = ((Viy + (((Viy ** 2) + (2 * (g * h))) ** 0.5)) / g)
    return totalTime

v = float(input("Enter initial velocity (m/s): "))
a = int(input("Enter angle (degrees): "))
h = float(input("Enter initial height (m): "))


def graphTra(distance):
    """
    Graphs the trajectory of a projectile without air friction.
    Args:
        distance (float): Distance traveled in meters
    """
    x = []
    y = []
    i = 0
    while ((v * (math.cos(math.radians(a)))) * i) <= distance:
        x.append((v * (math.cos(math.radians(a)))) * i)
        y.append(h + ((v * (math.sin(math.radians(a)))) * i) - ((g * (i ** 2)) / 2))
        i += 0.01


    plt.ylim((0), (max(y) * 1.1))
    plt.xlim((0), (max(x) * 1.1))
    plt.plot(x, y)
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.title("Distance (x) vs Height (y) trajectory")
    plt.show()