import math

'''
Convert a dictionary of spherical coordinates to a dictionary of
cylindrical coordinates.

coords is a dictionary with string keys 'r', 'theta', and 'phi' with
       corresponding values as spherical coordinate values
return value is a dictionary with keys 'r', 'theta', and 'z'  with
       corresponding values as cylindrical coordinate values
'''
def sphere2cyl(coords):
  # IMPLEMENT THIS FUNCTION


  # REMOVE THIS
  return {}


'''
Convert a dictionary of spherical coordinates to a dictionary of
cartesian coordinates.

coords is a dictionary with string keys 'r', 'theta', and 'phi' with
       corresponding values as spherical coordinate values
return value is a dictionary with keys 'x', 'y', and 'z'  with
       corresponding values as cartesian coordinate values
'''
def sphere2cart(coords):
  # IMPLEMENT THIS FUNCTION


  # REMOVE THIS
  return {}


'''
Convert a dictionary of cylindrical coordinates to a dictionary of
spherical coordinates.

coords is a dictionary with string keys 'r', 'theta', and 'z' with
       corresponding values as cylindrical coordinate values
return value is a dictionary with keys 'r', 'theta', and 'phi'  with
       corresponding values as spherical coordinate values
'''
def cyl2sphere(coords):
  # IMPLEMENT THIS FUNCTION


  # REMOVE THIS
  return {}


'''
Convert a dictionary of cylindrical coordinates to a dictionary of
cartesian coordinates.

coords is a dictionary with string keys 'r', 'theta', and 'z' with
       corresponding values as cylindrical coordinate values
return value is a dictionary with keys 'x', 'y', and 'z'  with
       corresponding values as cartesian coordinate values
'''
def cyl2cart(coords):
  # IMPLEMENT THIS FUNCTION


  # REMOVE THIS
  return {}


'''
Convert a dictionary of cartesian coordinates to a dictionary of
spherical coordinates.

coords is a dictionary with string keys 'x', 'y', and 'z' with
       corresponding values as cartesian coordinate values
return value is a dictionary with keys 'r', 'theta', and 'phi'  with
       corresponding values as spherical coordinate values
'''
def cart2sphere(coords):
  # IMPLEMENT THIS FUNCTION


  # REMOVE THIS
  return {}


'''
Convert a dictionary of cartesian coordinates to a dictionary of
cylindrical coordinates.

coords is a dictionary with string keys 'x', 'y', and 'z' with
       corresponding values as cartesian coordinate values
return value is a dictionary with keys 'r', 'theta', and 'z'  with
       corresponding values as cylindrical coordinate values
'''
def cart2cyl(coords):
  # From lecture 2 slides

  # initialize empty dictionary
  cart_points = {}
  x = coords['x']
  y = coords['y']
  z = coords['z']

  cart_points['r'] = math.sqrt(x ** 2 + y ** 2 + z ** 2)
  cart_points['theta'] = math.acos(z / cart_points['r'])
  cart_points['phi'] = math.acos(y / cart_points['r'])

  return cart_points


'''
Determine the type of the coordinate dictionary.

coords is a dictionary representing a point in either cartesian,
       spherical, or cylindrical coordinates
return value is a string of either 'cart', 'sphere', or 'cyl'

As an example:
  point1 = {'x': 1, 'y': 2, 'z': 3}
  point2 = cart2cyl(point1)
  print detect_type(point1) # should print 'cart'
  print detect_type(point2) # should print 'cyl'
'''
def detect_type(coords):
  # IMPLEMENT THIS FUNCTION

  
  # REMOVE THIS
  return 'cart'
