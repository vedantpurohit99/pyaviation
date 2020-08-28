'''
This file contains functions that help with unit conversions.
'''

def nautical_to_statute(nautical):
  '''
  This function converts the given nautical miles (knots) to statute miles (mph).

  params:
  nautical: float

  return:
  statute: float
  '''
  return nautical * 1.15

def statute_to_nautical(statute):
  '''
  This function converts the given statute miles (mph) to nautical miles (knots).

  params:
  statute: float

  return:
  nautical: float
  '''
  return statute / 1.15

def kph_to_nautical(kph):
  '''
  This function converts the given kilometers per hour (kph) to nautical miles (knots).

  params:
  kph: float

  return:
  nautical: float
  '''
  return kph * 0.54

def kph_to_statute(kph):
  '''
  This function converts the given kilometers per hour (kph) to statute miles (knots).

  params:
  kph: float

  return:
  statute: float
  '''
  return kph * 0.62

def mins_to_hour(minutes):
  '''
  This function converts the given minutes to hours.

  params:
  minutes: float

  return:
  hours: float
  '''
  return minutes / 60

def hour_to_mins(hours):
  '''
  This function converts the given hours to minutes.

  params:
  hours: float

  return:
  minutes: float
  '''
  return hours * 60