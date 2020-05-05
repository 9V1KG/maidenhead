"""
    Calculate Maidenhead locator from Google plus code
    Author: 9V1KG Klaus D Goepel
    https://klsin.bpmsg.com
    https://github.com/9V1KG/Maiden
    Created: 2020-05-02
    License: http://www.fsf.org/copyleft/gpl.html

"""
import re
from openlocationcode import openlocationcode as olc
from maiden import Maiden, Geodg2dms

MY_LOC = "PK04lc"
g_plus_full = re.compile(  # Google full plus code input validation
    r"(^|\s)([23456789C][23456789CFGHJMPQRV][23456789CFGHJMPQRVWX]{6}"
    r"\+[23456789CFGHJMPQRVWX]{2,3})(\s|$)"
)
g_plus_short = re.compile(  # Google short plus code validation
    r"(^|\s)([23456789CFGHJMPQRVWX]{4,6}"
    r"\+[23456789CFGHJMPQRVWX]{2,3})(\s|$)"
)
maiden = Maiden()

print("Calculate Maidenhead locator from Google plus code")
print(f"My locator {MY_LOC}")
pos_a = maiden.maiden2latlon(MY_LOC)
print(f"My pos: {Geodg2dms(pos_a)}")

line = input("Input Google full olc: ")
if not g_plus_full.match(line):
    print("Invalid olc")
    exit(1)
fc = olc.recoverNearest(line, pos_a[0], pos_a[1])
print(f"Google full code: {fc}")
res = olc.decode(fc)
print(f"Lat: {res.latitudeCenter}, Lon: {res.longitudeCenter}")
pdms_b = Geodg2dms((res.latitudeCenter, res.longitudeCenter))
print(f"Result: "
      f"{pdms_b.lat_deg} {pdms_b.lat_min}'{pdms_b.lat_sec}\"{pdms_b.lat_dir}, "
      f"{pdms_b.lon_deg} {pdms_b.lon_min}'{pdms_b.lon_sec}\"{pdms_b.lon_dir}"
      )

loc = maiden.latlon2maiden((res.latitudeCenter, res.longitudeCenter), 10)
print(f"Locator: {loc[:6]} {loc[6:]}")
