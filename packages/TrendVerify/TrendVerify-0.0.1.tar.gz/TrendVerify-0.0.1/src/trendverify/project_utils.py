'''

'''

from datetime import timedelta, datetime
from .verificationcodes import verify_as
import regex as re

Clouds = {
            "FEW" : 2,
            "SCT" : 4,
            "BKN" : 7,
            "OVC" : 8
}

Clouds_inv_map = {v:k for k,v in Clouds.items()}

PRECIPITATION_REGEX     = r'^(?>\+|\-)?(?>MI|BC|PR|DR|BL|SH|TS|FZ)?' + \
                                            r'(?>DZ|RA|SN|SG|IC|PL|GR|GS)'

def timeroundabout(dt :datetime, minutes = 15):
    _median = timedelta(minutes=round(minutes/2))
    if (_x := (dt - datetime.min)%timedelta(minutes = minutes)) > _median:
        return dt + (-1*_x)%timedelta(minutes = minutes)
    else:
        return dt - _x

def metar_time_range(start, stop, step = timedelta(minutes = 30), /, *\
                    , end_inclusive = True): 
    _start = start + (datetime.min - start)%timedelta(minutes = 30)
    _stop  = stop  - (stop - datetime.min)%timedelta(minutes = 30)
    while(_stop >= _start):
        yield _start
        _start += step
        if _start == _stop and not end_inclusive: raise StopIteration

class MetarSequenceError(Exception):
    ...

class MetarTimeError(Exception):
    def __init__(self, metartime :datetime, *args, **kwargs):
        self.metartime = metartime
        print(f"Incorrect metar time for metar with datetime: {metartime}")
        super(MetarTimeError, self).__init__(*args, **kwargs)

class NilMetarException(Exception):
    def __init__(self, metartime, *args, **kwargs):
        print(f"Nil metar for metar with datetime: {metartime}")
        super(NilMetarException, self).__init__(*args, **kwargs)

def num_of_metars_in_timerange(start, stop, step = timedelta(minutes = 30), /, *\
                    , end_inclusive = True):
    _ = 0
    for __ in metar_time_range(start, stop, step = step,\
                     end_inclusive = end_inclusive):
        _ += 1
    return _

def verify_each(element :str, change_group, sufficient = None, *metars):
    assert None not in (element, change_group, metars)

    match element:
        case "wind_dir":
            '''
                Caveats:
                Ignoring metars with VRB directions.
            '''
            if change_group.wind_dir is None:
                return verify_as.NOT_FORECASTED
            elif change_group.wind_dir != "VRB":
                _w = int(change_group.wind_dir)
                _v = [v.wind_dir for v in metars if v.wind_dir != "VRB"]
                if any(abs(int(v) - _w) <= 20 for v in _v):
                    return verify_as.WITHIN_ACCURACY_LIMITS
                else:
                    return verify_as.NOT_WITHIN_ACCURACY_LIMITS if sufficient else \
                    verify_as.NOT_ENOUGH_OBSERVATION_DATA
            elif change_group.wind_dir == "VRB":
                raise NotImplementedError

            ...
        case "wind_speed":
            if change_group.wind_speed is None:
                return verify_as.NOT_FORECASTED
            if any(abs(int(v.wind_speed) - int(change_group.wind_speed)) <= 5 for v in metars):
                return verify_as.WITHIN_ACCURACY_LIMITS
            else:
                return verify_as.NOT_WITHIN_ACCURACY_LIMITS if sufficient else \
                        verify_as.NOT_ENOUGH_OBSERVATION_DATA
            ...
        case "visibility":
            if change_group.visibility is None:
                return verify_as.NOT_FORECASTED
            _range      = 200 if int(change_group.visibility) <= 800 else\
                            round(int(change_group.visibility)*0.3)
            
            if any(abs(int(change_group.visibility) - int(m.visibility)) <= _range for \
                        m in metars):
                return verify_as.WITHIN_ACCURACY_LIMITS
            else:
                return verify_as.NOT_WITHIN_ACCURACY_LIMITS if sufficient else \
                        verify_as.NOT_ENOUGH_OBSERVATION_DATA
            ...
        case "precipitation":
            '''
                Guiding principles:
                -------------------------------------------------
                |               |                    |          |
                | Precipitation |  Whether Observed? |  Return  |
                |               |                    |          |
                -------------------------------------------------
                |  Forecasted   |     Yes            |   True   |
                |  Forecasted   |     No             |   False  |
                | Not Forecasted|     Yes            |   False  |
                | Not Forecasted|     No             |   None   |               
                |-----------------------------------------------|
                Additionally, if the change group does not have 
                any associated weather, NOT_FORECASTED is returned.
                The rationale is that the weatherless change group
                does not imply precipitation (or lack thereof) in
                any explicit sense. This is in contrast to non-pre-
                cipitative weather like BR whose presence vis-à-vis
                absence of any precipitative wx invariably gives a-
                way the fact that precipitative wx are not forecas-
                ted to commence or continue.    
            '''
            if not metars:
                return verify_as.NOT_ENOUGH_OBSERVATION_DATA
            
            _wx         = change_group.wx

            if not change_group.wx:
                return verify_as.NOT_FORECASTED

            _prec       = any(__ for __ in map(lambda o: re.search(PRECIPITATION_REGEX, o), _wx))
            for metar in metars:
                _mw = metar.wx
                _mprec  = any(__ for __ in map(lambda o: re.search(PRECIPITATION_REGEX, o), _mw))
                if _mprec: break
        
            if sufficient:
                if not (_prec ^ _mprec):
                    return verify_as.WITHIN_ACCURACY_LIMITS if _prec else \
                            verify_as.NOT_FORECASTED
                else:
                    return verify_as.NOT_WITHIN_ACCURACY_LIMITS
            elif not sufficient:
                if _prec and _mprec:
                    return verify_as.WITHIN_ACCURACY_LIMITS
                elif _prec and not _mprec:
                    return verify_as.NOT_ENOUGH_OBSERVATION_DATA
                elif not _prec and _mprec:
                    return verify_as.NOT_WITHIN_ACCURACY_LIMITS
                elif not _prec and not _mprec:
                    return verify_as.NOT_ENOUGH_OBSERVATION_DATA

        case "cloud_height":
            '''
                Caveats:
                Cloud height is assumed to be the lowest height for which cloud report
                has been made. This is, however, not specifically mentioned anywhere 
                as such.
            '''
            _cld        = change_group.clouds
            if not len(_cld):
                return verify_as.NOT_FORECASTED
            _concat_cld = ' '.join(_cld)
            _cld_ht     = min(int(__) for __ in re.findall(r'(?>(?<=FEW|SCT|BKN|OVC)(\d{3})(?=CB|TCU)?)', \
                            _concat_cld))

            _cld_hts_metar \
                        = set()
            for metar in metars:
                _concat_metar_cld \
                        = ' '.join(metar.clouds)
                _mcld   = min(int(__) for __ in re.findall(r'(?>(?<=FEW|SCT|BKN|OVC)(\d{3})(?=CB|TCU)?)', \
                            _concat_metar_cld))
                _cld_hts_metar.add(_mcld)
            if _cld_ht  <= 10:
                _cld_ht_range \
                        = set(range(_cld_ht - 1, _cld_ht + 2))
            elif _cld_ht > 10:
                _cld_ht_range \
                        = set(range(int(_cld_ht*(1 - 0.3)), \
                                int(_cld_ht*(1 + 0.3)) + 1))
            if not _cld_ht_range.isdisjoint(_cld_hts_metar):
                return verify_as.WITHIN_ACCURACY_LIMITS
            else:
                return verify_as.NOT_WITHIN_ACCURACY_LIMITS if sufficient else \
                        verify_as.NOT_ENOUGH_OBSERVATION_DATA
            ...

        case "cloud_amount":
            '''
                FEW020 : tuple of (upper bound of FEW, height); likewise for others.
                Represented as complex number with the real part denoting amount;
                the imaginary part as height.
                Motivation: A tuple can very well suffice for the use-case here. While
                true, but the fact remains that a tuple may or may not contain Number.
                A complex number on the other hand therefore ensures type safety apart
                from being a convenient single composite number as sentinel.
                ---------------------------------------------------------------------
                Caveats:
                The ICAO annex III prescribes two categories of conditions. As to what
                were to happen if both the conditions were to be held simultaneously 
                applicable, no objective criterion could be caused to be interpreted 
                despite efforts. In the interest of positivity of results, the current
                implementation returns True if either of the conditions returns True.

            '''
            _cld        = change_group.clouds
            if not len(_cld):
                return verify_as.NOT_FORECASTED
            def _pairify(o):
                _ = re.search(r'(?>((?>FEW|SCT|BKN|OVC))(\d{3})(?>CB|TCU)?)',o)
                return _.group(1), _.group(2)


            _cld        = map(_pairify, _cld)
            _complex_cloud \
                        = set(complex(Clouds[_], int(__)) for _, __ in _cld)

            _m          = map(lambda o: o.clouds, metars)
            _complex_cloud_from_metars \
                        = set()

            for _ind_cld in _m:
                _ind_complex_clouds = map(_pairify, _ind_cld)
                for _, __ in _ind_complex_clouds:
                    _complex_cloud_from_metars.add(complex(Clouds[_], int(__)))
            
            _max_amount_forecasted \
                        = max(__.real for __ in _complex_cloud)

            if any(__.imag < 15 for __ in _complex_cloud):
                if any(__.imag < 15 for __ in _complex_cloud_from_metars):
                    return verify_as.WITHIN_ACCURACY_LIMITS
                elif all(__.imag >= 15 for __ in _complex_cloud_from_metars) and sufficient:
                    return verify_as.NOT_WITHIN_ACCURACY_LIMITS

            if _max_amount_forecasted >= 7:
                if any(_max_amount_forecasted >= __.real for __ in _complex_cloud_from_metars):
                    return verify_as.WITHIN_ACCURACY_LIMITS
            elif not _max_amount_forecasted >= 7:
                if any(7 <= __.real for __ in _complex_cloud_from_metars):
                    return verify_as.NOT_WITHIN_ACCURACY_LIMITS

            if _max_amount_forecasted < 7 and not any(__.imag < 15 for __ in _complex_cloud):
                return verify_as.NOT_FORECASTED if sufficient else \
                        verify_as.NOT_ENOUGH_OBSERVATION_DATA