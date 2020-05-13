'''Module to hold functionality related to aviation weather reports.'''

from datetime import datetime

from parser import tokenize_text
from keywords import TYPE_KEYWORDS

# TO DO: Validating a weather report.

def categorize_report(report):
  '''
  This function is used to categorize a weather report to either a METAR, SPECI or a TAF.

  params:
  report: string (Needs to be a valid weather report)
  
  return:
  ['METAR', 'SPECI', 'TAF']
  '''
  tokens = tokenize_text(report)
  if tokens[0] in TYPE_KEYWORDS:
    return tokens[0]
  
  return 'Invalid start to the weather report. Weather report must be in the METAR/SPECI/TAF format.'

def get_airport_code(report):
  '''
  This function is used to extract the 4-digit ICAO airport code from the weather report. Note that this
  function does not explicitly check if the report or the airport code is valid. However, if the provided
  report is valid, then it guarantees the correct airport code.

  params:
  report: string

  return:
  Airport code if it is found.
  '''
  tokens = tokenize_text(report)
  if len(tokens[1]) == 4:
    return tokens[1]

  return 'Did not find a 4-digit code at the second position of the report.'

def get_time(report):
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
  tokens = tokenize_text(report)
  time = tokens[2]
  if len(time) == 7:
    return {
      'day': int(time[:2]),
      'hour': int(time[2:4]),
      'minute': int(time[4:6])
    }
  
  return 'Did not find a 7-digit time in the weather report.'

def is_auto(report):
  '''
  This function determines if a weather report is automated or manual.

  params:
  report: string

  return:
  is_auto: boolean.
  '''
  tokens = tokenize_text(report)
  is_auto = tokens[3]

  return is_auto == 'AUTO'