import pathlib
from datetime import datetime
import re
from .metar import parseManyMetars
from .trend import Trend
import csv

local_dir = r"C:\Users\Trideep Biswas.DESKTOP-HRMS22M\Desktop\IMD\TrendForecastVerification\Metar2022\METAR_2022\Metar2022\METAR_2022"
for x in (_.name for _ in \
	pathlib.WindowsPath(local_dir).iterdir()
	if _.is_dir()):
	METAR_DATA_FILE_DIR   = fr'C:\Users\Trideep Biswas.DESKTOP-HRMS22M\Desktop\IMD\TrendForecastVerification\Metar2022\METAR_2022\Metar2022\METAR_2022\{x}'
	OUTFILE_PATH		  = r"C:\Users\Trideep Biswas.DESKTOP-HRMS22M\Desktop\IMD\TrendForecast\master_output.txt"
	p = pathlib.WindowsPath(METAR_DATA_FILE_DIR)

	_x 			 = (_ for _ in p.iterdir())
	_metar_files = (_.name for _ in p.iterdir())

	metar_files = [_ for _ in filter(lambda o: o.startswith('METAR'), _metar_files)]

	metar_set = set()

	for x in metar_files:
		_ 				= re.match(r'METAR(\d{6})', x).group(1)
		_issuemonthyear	= datetime.strptime(_, "%Y%m").strftime("%b%Y")

		with open(p/x) as file:
			print(file)
			for m in parseManyMetars(*[line for line in file], issuemonthyear=_issuemonthyear):
				metar_set.add(m)

	metar_list = [_ for _ in metar_set]
	metar_list.sort(key = lambda o: o.issuedatetime)
	metar_with_trends = [_ for _ in filter(lambda o: o.trend, metar_list)]

	with open(OUTFILE_PATH, "a+") as file:
		csvfile = csv.writer(file)
		csvfile.writerow(['issuedatetime', 'station_code', 'trend', 'wind_dir', \
							'wind_speed', 'visibility', 'precipitation', 'cloud_amount',\
							'cloud_height'])
		for metar in metar_with_trends:
			print(f"processing {metar}")
			trend = Trend(metar)
			csvfile.writerow([trend.issuedatetime, trend.metar_obj.station_code,\
						 trend.trend_msg, *[_.name for _ in trend.verify_trend(*metar_list)]])

# x = filter(lambda o: o.issuedatetime >= datetime(2021,5,1,10,0), metar_list)
# y = [_ for _ in x]
# t = Trend(y[0])
# t.verify_trend(*y[:10])