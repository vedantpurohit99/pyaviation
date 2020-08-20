'''File to store keywords used in METAR/TAF.'''

TYPE_KEYWORDS = [
  'METAR',
  'SPECI'
  'TAF'
]

DESCRIPTOR_KEYWORDS = [
  'MI',
  'BC',
  'DR',
  'BL',
  'SH',
  'TS',
  'PR',
  'FZ'
]

DESCRIPTOR_MAP = {
  'MI': 'Shallow',
  'BC': 'Patches',
  'DR': 'Drifting',
  'BL': 'Blowing',
  'SH': 'Shower(s)',
  'TS': 'Thunderstorm',
  'PR': 'Partial',
  'FZ': 'Freezing'
}

PHENOMENA_KEYWORDS = [
  'DZ',
  'RA',
  'SN',
  'SG',
  'PL',
  'GR',
  'GS',
  'IC',
  'UP',
  'HZ',
  'FU',
  'SA',
  'DU',
  'FG',
  'BR',
  'VA',
  'PO',
  'SS',
  'DS',
  'SQ',
  '+FC',
  'FC'
]

PHENOMENA_MAP = {
  'DZ': 'Drizzle',
  'RA': 'Rain',
  'SN': 'Snow',
  'SG': 'Snow Grains',
  'PL': 'Ice Pellets',
  'GR': 'Hail',
  'GS': 'Snow Pellets',
  'IC': 'Ice Crystals',
  'UP': 'Unknown Precipitation',
  'HZ': 'Haze',
  'FU': 'Smoke',
  'SA': 'Sand',
  'DU': 'Dust',
  'FG': 'Fog',
  'BR': 'Mist',
  'VA': 'Volcanic Ash',
  'PO': 'Dust/Sand Whirls',
  'SS': 'Sandstorm',
  'DS': 'Duststorm',
  'SQ': 'Squalls',
  '+FC': 'Tornado/Watersprout',
  'FC': 'Funnel Cloud'
}

SKY_KEYWORDS = [
  'SKC',
  'FEW',
  'SCT',
  'BKN',
  'OVC'
]

SKY_MAP = {
  'SKC': 'Sky Clear',
  'FEW': 'Trace to 2 oktas',
  'SCT': '3 to 4 oktas',
  'BKN': '5 to less than 8 oktas',
  'OVC': '8 oktas'
}

CLOUD_KEYWORDS = [
  'CI',
  'ST',
  'CS',
  'SF',
  'CC',
  'SC',
  'AS',
  'CU',
  'AC',
  'CF',
  'ACC',
  'TCU',
  'NS',
  'CB'
]

CLOUD_MAP = {
  'CI': 'Cirrus',
  'ST': 'Stratus',
  'CS': 'Cirrostratus',
  'SF': 'Stratus Fractus',
  'CC': 'Cirrocumulus',
  'SC': 'Stratocumulus',
  'AS': 'Altostratus',
  'CU': 'Cumulus',
  'AC': 'Altocumulus',
  'CF': 'Cumulus Fractus',
  'ACC': 'Altocumulus Castellanus',
  'TCU': 'Towering Cumulus',
  'NS': 'Nimbostratus',
  'CB': 'Cumulonimbus'
}
