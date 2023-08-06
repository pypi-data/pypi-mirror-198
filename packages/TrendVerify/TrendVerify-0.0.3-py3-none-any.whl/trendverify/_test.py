from .metar import parsemetar, parseManyMetars
from .trend import Trend
from .project_utils import MetarTimeError
import csv

metar_set = set()
def read_metars(file=r"C:\Users\Trideep Biswas.DESKTOP-HRMS22M\Desktop\IMD\TrendForecast\test_control.txt"):
	with open(file) as file:
		# prinetar)
			
		for p in parseManyMetars(*[line for line in file], issuemonthyear="jun2022"):
			print(p)
			metar_set.add(p)
	
read_metars()
metar_list = [_ for _ in metar_set]
metar_list.sort(key= lambda o: o.issuedatetime)
metar_with_trends = [_ for _ in filter(lambda o: o.trend, metar_list)]

with open(r"C:\Users\Trideep Biswas.DESKTOP-HRMS22M\Desktop\IMD\TrendForecast\output.txt", "a") as file:
	csvfile = csv.writer(file)
	csvfile.writerow(['issuedatetime', 'station_code', 'trend', 'wind_dir', \
						'wind_speed', 'visibility', 'precipitation', 'cloud_amount',\
						'cloud_height'])
	for metar in metar_with_trends:
		trend = Trend(metar)
		csvfile.writerow([trend.issuedatetime, trend.metar_obj.station_code,\
					 trend.trend_msg, *[_.name for _ in trend.verify_trend(*metar_list)]])
		

# print(x.verify_trend(*metar_list[0:50]))

