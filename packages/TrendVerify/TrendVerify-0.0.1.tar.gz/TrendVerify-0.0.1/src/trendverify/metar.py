'''
'''

from collections import namedtuple
import regex as re
from datetime import datetime, timedelta
from .project_utils import timeroundabout, MetarTimeError, NilMetarException

BaseMetar = namedtuple('BaseMetar', ['station_code', 'issuedatetime', 'wind_dir', 'wind_speed',\
					 'visibility', 'wx', 'clouds', 'trend'])

class Metar(BaseMetar):
	'''
		This class extends the BaseMetar class which is a namedtuple type
		to deterministically add hashable routines.
	'''
	def __hash__(self):
		return hash(self.station_code + self.issuedatetime.isoformat())

	def __eq__(self, other):
		return hash(self) == hash(other)


def parsemetar(metarmsg, issuemonthyear=None):
		'''
			metarmsg 			:str
			issuemonthyear		:str

			issuemonthyear examples: jan2022, feb2023
		'''
		assert issuemonthyear is not None
		metar_only 	= re.search(r'(.*?)(?>NOSIG|TEMPO|BECMG|\=)', metarmsg).group(1)
		_x 			= re.search(r'(?P<dt>\d{6})Z', metar_only)
		_m 			= re.search(r"(\w{3})(\d{4})", issuemonthyear)
		_month 		= _m.group(1).capitalize()
		_year  		= _m.group(2)
		_daytime   	= _x.group('dt')
		_station_code \
					= re.search(r'(?<=METAR\s)(?>COR\s)?(.*?)\s', metar_only).group(1)

		_metartime 	= datetime.strptime(_daytime + _month + _year, "%d%H%M%b%Y")
		_metartime	= timeroundabout(_metartime)

		if re.search(r'NIL', metarmsg): raise NilMetarException(_metartime)
		if _metartime.minute not in (0, 30): raise MetarTimeError(_metartime)

		_x 			= re.search(r'(?P<wind_dir>\d{3}|VRB)?(?P<wind_speed>P?\d{2})(?>G\d{2})?KT',\
								 metar_only)
		_parsed_wind_dir 	= _x.group('wind_dir')
		_parsed_wind_speed 	= _x.group('wind_speed')
		
		_parsed_visibility 	= re.search(r'(?<=KT\s)(?>\d{3}V\d{3}\s)?(?P<vis>\d{4})\s', metar_only)
		if _parsed_visibility: _parsed_visibility = _parsed_visibility.group('vis')
		
		_wx_regex			= r'\s(?>\+|\-|VC)?(?>MI|BC|PR|DR|BL|SH|TS|FZ)?' + \
								r'(?>DZ|RA|SN|SG|IC|PL|GR|GS|BR|FG|FU|VA|DU|SA|HZ|PO|SQ|FC|SS|DS)\b|\s(?>\+|\-|VC)?TS\b'
		
		_parsed_wx			= [_.strip() for _ in re.findall(_wx_regex, metar_only)]
		
		_parsed_clouds		= re.findall(r'(?>(?>FEW|SCT|BKN|OVC)\d{3})(?>CB|TCU)?|VV\/\/\/|NSC', metar_only)
		
		_parsed_trend		= re.search(r'(?>TEMPO|BECMG).*+', metarmsg)
		if _parsed_trend: _parsed_trend = _parsed_trend.group(0)

		return Metar(_station_code, _metartime, _parsed_wind_dir, _parsed_wind_speed,\
						_parsed_visibility, _parsed_wx, _parsed_clouds, _parsed_trend)


def parseManyMetars(*metar_msgs, issuemonthyear=None):
	'''
		Convenience function to parse metar msgs many at once
	'''
	match metar_msgs:
		case [*metars]:
			for metarmsg in metars:
				# print(metarmsg)
				# print(type(metarmsg))
				try:
					yield parsemetar(metarmsg, issuemonthyear=issuemonthyear)
				except (MetarTimeError, NilMetarException):
					pass
			#raise NotImplementedError
		case str(metarmsg):
			return parsemetar(metarmsg)