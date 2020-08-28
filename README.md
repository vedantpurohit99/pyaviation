# pyaviation

This library is built to provide functionalities and solutions to problems related to aviation.

## Dependencies

Python 3 is required to run the library.

### Python Modules
- datetime
- fractions
- json

## Installation

Working on creating a python package that can be easily downloaded using pip. Currently, the files need to be downloaded or forked.

## Functionalities

### Weather Reports

The library provides the `WeatherReport` class to parse an aviation weather report. Currently, there is support for METAR, TAF and SPECI. Other weather report formats will cause errors.

#### `Weather Report` class

#### Methods

`categorize_report`

`airport_code`

`is_auto`

`wind`

`has_variable_wind`

`visibility`

`weather`

`sky`

`temp_and_dewpoint`

`altimeter`

`remark`

`report`

### Navigation

This module provides the functions and classes that assist in solving navigation problems that a pilot may have.

#### `magnetism`

This submodule contains functions that quickly convert headings between compass, magnetic and true. In other words, solve the problem related to variation and deviation.

#### Functions

`true_to_magnetic` - Convert a True heading to its Magnetic heading by providing variation information.

`magnetic_to_true` - Convert a Magnetic heading to its True heading by providing variation information.

`compass_to_magnetic` - Convert a Compass heading to its Magnetic heading by providing deviation information.

`magnetic_to_compass` - Convert a Magnetic heading to its Compass heading by providing deviation information.

#### `conversion`

This submodule contains functions that convert between statute
and nautical miles as well as converting kph. Moreover, there
are also function that convert between hours and minutes.

#### Functions

`nautical_to_statute` - Convert Nautical miles to Statute miles.

`statute_to_nautical` - Convert Statute miles to Nautical miles.

`kph_to_nautical` - Convert Kilometers per hour to Nautical miles.

`kph_to_statute` - Convert Kilometers per hour to Statute miles.

`mins_to_hour` - Convert minutes to hours.

`hour_to_mins` - Convert hours to minutes.