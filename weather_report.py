'''Weather Report class to describe an aviation weather report (Currently has METAR/SPECI/TAF).'''

from datetime import datetime

from gen_parser import tokenize_text
from keywords import TYPE_KEYWORDS

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

    params:
    report: string

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

    params:
    report: string

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

    params:
    report: string

    return:
    is_auto: boolean.
    '''
    is_auto = self.tokens[3]

    return is_auto == 'AUTO'