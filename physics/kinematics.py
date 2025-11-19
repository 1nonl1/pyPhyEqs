#Vf = Vi + at
#Vf = sqrt(Vi^2 + 2as)
#s= Vit + ((at^2)/2)
#Vaverage = s/t

def VelAT(a, t, Vi):
  """
  Calculates the final velocity if you know the acceleration, time, and initial velocity
  Args:
    a (float): Acceleration in m/s^2
    t (float): Time in seconds
    Vi (float): Initial velocity in m/s
  Returns:
    float: Final velocity of the object
  """
  finalVelocity = Vi + (a*t)
  return finalVelocity

def VelAS(a, s, Vi): 
  """
  Calculates the final velocity if you know the acceleration, initial velocity, and displacement
  Args:
    a (float): Acceleration in m/s^2
    s (float): Displacement of object in m
    Vi (float): Initial velocity in m/s
  Returns:
    float: Final velocity of the object
  """
  finalVelocity = (Vi + (2 * (a * s))) ** 0.5
  return finalVelocity

def displacment(Vi, t, a):
  """
  Calculates the displacement of an object in meters.
  Args:
    Vi (float): Inital velocity in m/s
    t (float): Time in seconds
    a (float): Acceleration of the object in m/s^2
  Returns:
    float: Displacement in meters
  """
  dis = (Vi * t) + ((a * (t ** 2)) / 2)
  return dis

def VelAvg(s, t):
  """
  Calculates the average velocity
  Args:
    s (float): Displacement in meters
    t (float): Time in seconds
  Returns:
    float: Average velocity in m/s
  """
  avg = s / t
  return avg