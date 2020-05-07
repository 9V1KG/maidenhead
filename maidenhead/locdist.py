"""
    Calculate distance and azimuth from to locator positions
    Author: 9V1KG Klaus D Goepel
    https://klsin.bpmsg.com
    https://github.com/9V1KG/Maiden
    Created: 2020-05-02
    License: http://www.fsf.org/copyleft/gpl.html
"""
import sys
import re
from openlocationcode import openlocationcode as olc
from maidenhead.maiden import Maiden, Geodg2dms

MY_LOC = "PK04lc68dj"

maiden = Maiden()  # Initialize class
print("""
Maidenhead locator program by 9V1KG
https://github.com/9V1KG/Maiden
        """)
print("Calculates distance and azimuth from your locator (\"MY_LOC\")")
print(f"My locator: {MY_LOC}")
pos_a = maiden.maiden2latlon(MY_LOC)
print(f"My pos: {pos_a} Lat/Lon")
pdms_a = Geodg2dms(pos_a)
print(f"My pos: "
      f"{pdms_a.lat_deg} {pdms_a.lat_min}'{pdms_a.lat_sec}\"{pdms_a.lat_dir}, "
      f"{pdms_a.lon_deg} {pdms_a.lon_min}'{pdms_a.lon_sec}\"{pdms_a.lon_dir}"
      )
opl = olc.encode(pos_a[0], pos_a[1])
print(f"Google map: {opl}\r\n")

line = input("Input Maidenhead Locator (4 to 10 char): ")
if not re.match(r"([A-Ra-r]{2}\d\d)(([A-Za-z]{2})(\d\d)?){0,2}", line):
    print("Locator has 2 to 5 character/number pairs, like PK04lc")
    sys.exit(1)
pos_b = maiden.maiden2latlon(line)
print(f"Result: {pos_b} Lat/Lon")
pdms_b = Geodg2dms(pos_b)
print(f"Result: "
      f"{pdms_b.lat_deg} {pdms_b.lat_min}'{pdms_b.lat_sec}\"{pdms_b.lat_dir}, "
      f"{pdms_b.lon_deg} {pdms_b.lon_min}'{pdms_b.lon_sec}\"{pdms_b.lon_dir}"
      )
opl = olc.encode(pos_b[0], pos_b[1])
print(f"Google map: {opl}")
betw = maiden.dist_az(pos_a, pos_b)
print(f"Distance: {betw[0]} km Azimuth: {betw[1]} deg")
