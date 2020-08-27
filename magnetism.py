'''
This file contains functions that assist with problems related to the Earth's magnetism.
'''

def __sanitize_direction(val):
  '''
  Private function to fix a given direction.

  params:
  val: float
  '''
  if val > 360:
    return val - 360
  
  if val < 0:
    return 360 + val
  
  return val

def true_to_magnetic(true, var_val, var_is_east):
  '''
  This function converts a true heading to its magnetic heading based on the given variation.

  params:
  true: True heading value (float)
  var_val: Variation value (float)
  var_is_east: Is variation in east direction (bool)

  return:
  magnetic: float
  '''
  if var_is_east:
   return __sanitize_direction(true - var_val)

  return __sanitize_direction(true + var_val)

def magnetic_to_true(magnetic, var_val, var_is_east):
  '''
  This function converts a magnetic heading to its true heading based on the given variation.

  params:
  magnetic: Magnetic heading value (float)
  var_val: Variation value (float)
  var_is_east: Is variation in east direction (bool)

  return:
  true: float
  '''
  if var_is_east:
    return __sanitize_direction(magnetic + var_val)

  return __sanitize_direction(magnetic - var_val)

def compass_to_magnetic(compass, dev_val, dev_is_east):
  '''
  This function converts a compass heading to its magnetic heading based on the given deviation.

  params:
  compass: Compass heading value (float)
  dev_val: Deviation value (float)
  dev_is_east: Is deviation in east direction (bool)

  return:
  magnetic: float
  '''
  if dev_is_east:
    return __sanitize_direction(compass + dev_val)

  return __sanitize_direction(compass - dev_val)

def magnetic_to_compass(magnetic, dev_val, dev_is_east):
  '''
  This function converts a magnetic heading to its compass heading based on the given deviation.

  params:
  magnetic: Compass heading value (float)
  dev_val: Deviation value (float)
  dev_is_east: Is deviation in east direction (bool)

  return:
  compass: float
  '''
  if dev_is_east:
    return __sanitize_direction(magnetic - dev_val)
  
  return __sanitize_direction(magnetic + dev_val)