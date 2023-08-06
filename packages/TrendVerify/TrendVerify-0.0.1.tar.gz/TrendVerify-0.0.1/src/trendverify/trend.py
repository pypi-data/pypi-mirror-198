from datetime import datetime, timedelta
import regex as re
from .metar import Metar
from .verificationcodes import verify_as
from collections import namedtuple
from .project_utils import metar_time_range, verify_each

class BaseChangeGroup:
	'''
		BASE CLASS OF TEMPO | BECMG | NOSIG
	'''
	def __init__(self, issuedatetime :datetime = None, change_group_text = None, /, *args, **kwargs):
		if issuedatetime is None:
			if 'issuedatetime' in kwargs.keys():
				issuedatetime = kwargs['issuedatetime']
			else:
				assert issuedatetime is not None

		self.change_group_text      = change_group_text
		
		self.change_indicator 		=	type(self).__name__
		self.valid_from				= 	issuedatetime
		self.valid_until			=	issuedatetime + timedelta(hours = 2)
		self.__repr__				= 	change_group_text

		if (__ := re.search(r"FM(\d{2})(\d{2})", change_group_text)):
			self.valid_from			= self.valid_from.replace(hour = int(__.group(1))\
															, minute = int(__.group(2)))
		if (__ := re.search(r"TL(\d{2})(\d{2})", change_group_text)):
			self.valid_until		= self.valid_until.replace(hour = int(__.group(1))\
															, minute = int(__.group(2)))

		...
		# PARSING ROUTINES GO HERE...
		...
		_x 							= re.search(r'(?P<wind_dir>\d{3}|VRB)?(?P<wind_speed>P?\d{2})(?>G\d{2})?KT'\
												, change_group_text)
		if _x:
			self.wind_dir			= _x.group('wind_dir')
			self.wind_speed 		= _x.group('wind_speed')
		else:
			self.wind_dir, self.wind_speed \
									= None, None

		self.visibility 			= re.search(r'\b(?P<vis>\d{4})\b'\
												, change_group_text)
		if self.visibility:
			self.visibility 		= self.visibility.group('vis')

		_wx_regex					= r'\s(?>\+|\-|VC)?(?>MI|BC|PR|DR|BL|SH|TS|FZ)?' + \
											r'(?>DZ|RA|SN|SG|IC|PL|GR|GS|BR|FG|FU|VA|DU|SA|HZ|PO|SQ|FC|SS|DS)\b|\s(?>\+|\-|VC)?TS\b'
		self.wx  					= [_.strip() for _ in re.findall(_wx_regex, change_group_text)]
		self.clouds					= re.findall(r'(?>(?>FEW|SCT|BKN|OVC)\d{3})(?>CB|TCU)?|VV\/\/\/|NSC'\
												, change_group_text)

		if all(_ == None for _ in [self.wind_dir, self.wind_speed, self.visibility, *self.wx, *self.clouds]):
			self.illegal_syntax		= True
		else:
			self.illegal_syntax 	= False

	def __repr__(self):
		return f"{type(self).__name__} object: '{self.change_group_text}'"


class TEMPO(BaseChangeGroup):
	def __init__(self, issuedatetime :datetime = None, change_group_text = None, /, *args, **kwargs):
		
		super(type(self), self).__init__(issuedatetime, change_group_text,\
										 *args, **kwargs)
		if (__ := re.search(r"AT(\d{2})(\d{2})", self.change_group_text)):
			self.valid_until		= self.valid_until.replace(hour = int(__.group(1))\
															, minute = int(__.group(2)))

class BECMG(BaseChangeGroup):
	def __init__(self, *args, **kwargs):
		super(type(self), self).__init__(*args, **kwargs)

class NOSIG(BaseChangeGroup):
	def __init__(self, *args, **kwargs):
		super(type(self), self).__init__(*args, **kwargs)

Accuracy = namedtuple('Accuracy', 'wind_dir wind_speed '\
										+ 'visibility precipitation cloud_amount cloud_height',\
					defaults = (None,)*6)

class Trend:
	def __init__(self, metar_obj :Metar, *args, **kwargs):
		self.issuedatetime :datetime = metar_obj.issuedatetime
		self.trend_msg	   :str		 = metar_obj.trend
		_change_grps	   :[str]	 = re.findall(r'(?>TEMPO|BECMG).*?(?=\sBECMG|\sTEMPO|=)'\
													 , metar_obj.trend)
		self.metar_obj				 = metar_obj
		self.accuracy_report 		 = None
		self.change_groups 	= []
		for _g in _change_grps:
			if re.search(r'\bTEMPO\b', _g):
				self.change_groups.append(TEMPO(self.issuedatetime\
											, _g))
			elif re.search(r'\bBECMG\b', _g):
				self.change_groups.append(BECMG(self.issuedatetime\
											, _g))
			elif re.search(r'\bNOSIG\b', _g):
				self.change_groups.append(NOSIG(self.issuedatetime\
											, _g))

	def __repr__(self):
		return f"Trend object at {id(self)}: '{self.trend_msg}'"
	
	def verify_trend(self, *metars : Metar):
		'''
			::: VERIFICATION PRINCIPLES :::


		'''
		metars = list(metars)
		metars.sort(key=lambda x: x.issuedatetime)

		_x = min(__.valid_from for __ in self.change_groups)
		_y = max(__.valid_until for __ in self.change_groups)
		if any(_cg.illegal_syntax for _cg in self.change_groups):
			print("Illegible trend syntax")
			return verify_as.ILLEGAL_TREND_SYNTAX

		testables = []
		for metar in metars:
			if metar.issuedatetime == self.issuedatetime:
				continue
			elif _x <= metar.issuedatetime <= _y:
				testables.append(metar)

		if any(_ not in map(lambda o: o.issuedatetime, [self.metar_obj] + testables) \
															for _ in metar_time_range(\
															_x, _y)):
			__ = verify_as.NOT_ENOUGH_OBSERVATION_DATA
		else:
			__ = None
		
		_sufficiency = __ == None

		_temp_acc = {k:None for k in Accuracy._fields}
		for element in _temp_acc.keys():
			_acc = None
			for _g in self.change_groups:
				if _acc is verify_as.NOT_WITHIN_ACCURACY_LIMITS:
					continue
				if (_temp := verify_each(element, _g, _sufficiency, *testables)) in \
									 (_ for _ in verify_as):
					if _acc is not None and _temp.value > _acc.value:
						_acc = _temp
					elif _acc is None:
						_acc = _temp
			else:
				_temp_acc[element] = _acc

		else:
			self.accuracy_report = Accuracy(*(v for k,v in _temp_acc.items()))
			return self.accuracy_report

	def pretty_verify(self, *args, **kwargs):
		return self.issuedatetime.strftime("%Y%m%d %H%MZ"), self.metar_obj.station_code,\
				self.trend_msg, *[_.name for _ in verify_trend(*args, **kwargs)] 
