'''Module to hold functionality related to aviation weather reports.'''

from parser import tokenize_text
from keywords import TYPE_KEYWORDS

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