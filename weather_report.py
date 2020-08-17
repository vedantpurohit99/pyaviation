'''Weather Report class to describe an aviation weather report (Currently has METAR/SPECI/TAF).'''

from datetime import datetime

from gen_parser import tokenize_text
from keywords import TYPE_KEYWORDS

from fractions import Fraction

class WeatherReport():
  def __init__(self, report):
    '''
    Initialize the Weather Report. For the class to work as expected, a
    valid weather report must be provided.

    params:
    report: string
    '''
    self.tokens = tokenize_text(report)
    self.report_type = self.categorize_report()
    

  # TO DO: Validating a weather report.

  def categorize_report(self):
    '''
    This function categorizes the report as either a METAR, SPECI or a TAF.
    
    return:
    type: string
    '''
    if self.tokens[0] in TYPE_KEYWORDS:
      return self.tokens[0]
    
    return 'Invalid start to the weather report. Weather report must be in the METAR/SPECI/TAF format.'
  
  def airport_code(self):
    '''
    This function is used to extract the 4-digit ICAO airport code from the weather report. Note that this
    function does not explicitly check if the report or the airport code is valid. However, if the provided
    report is valid, then it guarantees the correct airport code.

    return:
    Airport code if it is found.
    '''
    if len(self.tokens[1]) == 4:
      return self.tokens[1]

    return 'Did not find a 4-digit code at the second position of the report.'

  def time(self):
    '''
    This function finds and parses the date in the weather report. Function assumes that the 3rd position
    is the date position

    return:
    {
      'day': int,
      'hour': int,
      'minute': int
    }
    '''
    time = self.tokens[2]
    if len(time) == 7:
      return {
        'day': int(time[:2]),
        'hour': int(time[2:4]),
        'minute': int(time[4:6])
      }
    
    return 'Did not find a 7-digit time in the weather report.'

  def is_auto(self):
    '''
    This function determines if a weather report is automated or manual.

    return:
    is_auto: boolean.
    '''
    is_auto = self.tokens[3]

    return is_auto == 'AUTO'

  def __offset(self, auto, var):
    '''
    Private function to return offset for optional entries.
    '''
    offset = 0
    if auto:
      if self.is_auto():
        offset += 1
      
    if var:
      has_var, val = self.has_variable_wind()
      if has_var:
        offset += 1

    return offset
  
  def wind(self):
    '''
    This function finds and parses the wind data in the weather report. Function assumes that the 
    4th or 5th position is the wind position.

    return:
    {
      'direction': int,
      'speed': int,
      'gust': int
    }
    '''
    offset = self.__offset(True, False)
    info = self.tokens[3 + offset]

    if len(info) != 7 and len(info) != 10:
      return 'Did not find a 7 or 10 digit wind entry in the weather report.'
    
    direction = info[:3]
    w_speed = info[3:5]
    gust = 0

    if len(info) == 10:
      gust = info[6:8]

    return {
      'direction': int(direction),
      'speed': int(w_speed),
      'gust': int(gust)
    }

  def has_variable_wind(self):
    '''
    This function checks whether variable wind direction is provided in the weather report.
    If it is provided, then it return true and the range, otherwise false.

    return:
    has_var: boolean,
    range: [int, int]
    '''
    offset = self.__offset(True, False)
    info = self.tokens[4 + offset]
    
    if 'V' in info:
      lohi = [int(info[:3]), int(info[4:])]

      return True, lohi
    
    return False, []

  def visibility(self):
    '''
    This function returns the prevailing visibility provided in the weather report.

    return:
    visibility: float (in SM)
    '''
    offset = self.__offset(True, True)
    info = self.tokens[4 + offset]

    return Fraction(info[:-2]) * 1.0

# TESTING

report = 'METAR CYYZ 162200Z 26010KT 210V280 15SM BKN035 BKN100 24/16 A2989 RMK CU6AC1 SLP121 DENSITY ALT 1900FT='
wr = WeatherReport(report)