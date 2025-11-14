import math
import matplotlib.pyplot as plt

g = 9.807 #m/s^2
def calculateDistance(Vi, a, h):
    Viy = Vi * (math.sin(math.radians(a)))
    Vix = Vi * (math.cos(math.radians(a)))
    totalTime = ((Viy + (((Viy ** 2) + (2 * (g * h))) ** 0.5)) / g)
    distance = Vix * totalTime
    return distance

def calculateTotalTime(Vi, a, h):
    Viy = Vi * (math.sin(math.radians(a)))
    totalTime = ((Viy + (((Viy ** 2) + (2 * (g * h))) ** 0.5)) / g)
    return totalTime

v = float(input("Enter initial velocity (m/s): "))
a = int(input("Enter angle (degrees): "))
h = float(input("Enter initial height (m): "))

print(f"Distance: {calculateDistance(v, a, h)} m")
print(f"Total Time: {calculateTotalTime(v, a, h)} s")


x = []
y = []
dist = calculateDistance(v, a, h)
i = 0
while ((v * (math.cos(math.radians(a)))) * i) <= dist:
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