def func_incorrect1(x, y, z):
if x < y:    # wrong indentation --> error!
  return z
return 0

def func_incorrect2(x, y, z):
  if x < y:
  return z  # wrong indentation --> error!
  return 0

def func_correct(x, y, z):
  if x < y:
    return z
  return 0

