def arith1(x):
  """ Given an integer number x, returns:
      0, if x is negative or 0
      x, if x is strictly positve and less than or equal to 10
      10, otherwise """    
  
  if x <= 0:
    return 0
  elif x <= 10:
    return x

  return 10

def arith2(x, y):
  """ Given two integer numbers x and y, returns:
      
      2x + y, if x is strictly greater than y
      4y - 3, if y is strictly greater than x
      x^3 + xy, if x is equal to y """

  return 0

def arith3(x, y, z):
  """ Given three integer numbers x, y, and z, returns:
      
      0, if any of the two numbers are the same
      1, if the numbers are ordered such that x < y and y < z
      2, otherwise """

  return 0

def arith4(x, y, z, w):
  """ Given four integer numbers x, y, z, and w, returns:
 
      the maximum of arith2(x, y) and arith2(z, w), if x is strictly less than y
      the sum of arith3(z, y, x) and arith1(w), otherwise """
      

  return 0
