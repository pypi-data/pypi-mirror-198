import pathlib
from datetime import datetime
import re
from .metar import parseManyMetars
from .trend import Trend
import csv
import argparse
import sys, uuid


def find_metar_files(path, file_match_string):
    _metar_file_paths = []
    for file in path.iterdir():
        if not file.is_dir() and \
            re.match(file_match_string,file.name):
            _metar_file_paths.append(file)
        elif file.is_dir():
            _metar_file_paths += find_metar_files(path/file, file_match_string)
    else:
        return _metar_file_paths


def entry_point():

    local_dir = pathlib.Path.cwd()
    file_match_string = r'METAR(\d{6})'
    outputfile = local_dir/f"outputfile_{uuid.uuid4()}.txt"


    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="full path to directory containing metar files")
    parser.add_argument("-o","--outputfile", help="full file path to output file")
    args = parser.parse_args()

    if args.directory:
        _l = pathlib.WindowsPath(args.directory)
        if _l.exists():
            local_dir = _l
        elif not _l.exists():
            print(f"{_l} does not exist.")
            sys.exit()

    if args.outputfile:
        _l = pathlib.WindowsPath(args.outputfile)
        if _l.parent.exists():
            outputfile = _l
        elif not _l.parent.exists():
            print(f"{_l.parent} does not exist.")
            sys.exit()



    metar_file_paths = [_ for _ in find_metar_files(local_dir, file_match_string) if \
                        re.search(file_match_string, _.name)]

    metar_set = set()
    for metar_file in metar_file_paths:
        _ = re.match(r'METAR(\d{6})', metar_file.name).group(1)                    
        _issuemonthyear = datetime.strptime(_, "%Y%m").strftime("%b%Y")
        with open(metar_file) as file:
                print(file)
                for m in parseManyMetars(*[line for line in file], issuemonthyear=_issuemonthyear):
                    metar_set.add(m)

    station_codes   = set(_.station_code for _ in metar_set)
    ...

    with open(outputfile, "w+") as file:
        csvfile = csv.writer(file)
        csvfile.writerow(['issuedatetime', 'station_code', 'trend', 'wind_dir', \
                                'wind_speed', 'visibility', 'precipitation', 'cloud_amount',\
                                'cloud_height'])
    for station in station_codes:
        metar_list = [_ for _ in metar_set if _.station_code == station]

        metar_list.sort(key = lambda o: o.issuedatetime)
        metar_with_trends = [_ for _ in filter(lambda o: o.trend, metar_list)]

        with open(outputfile, "a+") as file:
            csvfile = csv.writer(file)
            for metar in metar_with_trends:
                print(f"processing {metar}")
                trend = Trend(metar)
                csvfile.writerow([trend.issuedatetime, trend.metar_obj.station_code,\
                             trend.trend_msg, *[_.name for _ in trend.verify_trend(*metar_list)]])



if __name__ == '__main__':
    local_dir = pathlib.Path.cwd()
    file_match_string = r'METAR(\d{6})'
    outputfile = local_dir/f"outputfile_{uuid.uuid4()}.txt"


    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="full path to directory containing metar files")
    parser.add_argument("-o","--outputfile", help="full file path to output file")
    args = parser.parse_args()

    if args.directory:
        _l = pathlib.WindowsPath(args.directory)
        if _l.exists():
            local_dir = _l
        elif not _l.exists():
            print(f"{_l} does not exist.")
            sys.exit()

    if args.outputfile:
        _l = pathlib.WindowsPath(args.outputfile)
        if _l.parent.exists():
            outputfile = _l
        elif not _l.parent.exists():
            print(f"{_l.parent} does not exist.")
            sys.exit()



    metar_file_paths = [_ for _ in find_metar_files(local_dir, file_match_string) if \
                        re.search(file_match_string, _.name)]

    metar_set = set()
    for metar_file in metar_file_paths:
        _ = re.match(r'METAR(\d{6})', metar_file.name).group(1)                    
        _issuemonthyear = datetime.strptime(_, "%Y%m").strftime("%b%Y")
        with open(metar_file) as file:
                print(file)
                for m in parseManyMetars(*[line for line in file], issuemonthyear=_issuemonthyear):
                    metar_set.add(m)

    station_codes   = set(_.station_code for _ in metar_set)
    ...

    with open(outputfile, "w+") as file:
        csvfile = csv.writer(file)
        csvfile.writerow(['issuedatetime', 'station_code', 'trend', 'wind_dir', \
                                'wind_speed', 'visibility', 'precipitation', 'cloud_amount',\
                                'cloud_height'])
    for station in station_codes:
        metar_list = [_ for _ in metar_set if _.station_code == station]

        metar_list.sort(key = lambda o: o.issuedatetime)
        metar_with_trends = [_ for _ in filter(lambda o: o.trend, metar_list)]

        with open(outputfile, "a+") as file:
            csvfile = csv.writer(file)
            for metar in metar_with_trends:
                print(f"processing {metar}")
                trend = Trend(metar)
                csvfile.writerow([trend.issuedatetime, trend.metar_obj.station_code,\
                             trend.trend_msg, *[_.name for _ in trend.verify_trend(*metar_list)]])

