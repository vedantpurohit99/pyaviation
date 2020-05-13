'''Module to hold functionality related to aviation weather reports.'''

from parser import tokenize_text
from keywords import TYPE_KEYWORDS

def categorize_report(text):
  tokens = tokenize_text(text)
  if tokens[0] in TYPE_KEYWORDS:
    return tokens[0]
  
  return 'Invalid start to the weather report. Weather report must be in the METAR/TAF format.'
