#!/usr/bin/python3
"""
Calculate distance and azimuth from to locator positions
"""

import sys
import re
from openlocationcode import openlocationcode as olc
from maiden import Maiden, Geopos

MY_LOC = "PK04lc68dj"

maiden = Maiden()  # Initialize class
print("Calculate distance and azimuth from to locator positions")

print(f"My locator: {MY_LOC}")
pos_a = maiden.maiden2latlon(MY_LOC)
print(f"My pos: {pos_a} Lat/Lon")
pdms_a = Geopos(pos_a)
print(f"My pos: "
      f"{pdms_a.latDeg} {pdms_a.latMin}'{pdms_a.latSec}\"{pdms_a.latDir}, "
      f"{pdms_a.lonDeg} {pdms_a.lonMin}'{pdms_a.lonSec}\"{pdms_a.lonDir}"
      )
opl = olc.encode(pos_a[0], pos_a[1])
print(f"Google map: {opl}\r\n")

line = input("Input Maidenhead Locator: ")
if not re.match(r"([A-Ra-r]{2}\d\d)(([A-Za-z]{2})(\d\d)?){0,2}", line):
    print("Locator has 2 to 5 character/number pairs, like PK04lc")
    sys.exit(1)
pos_b = maiden.maiden2latlon(line)
print(f"Result: {pos_b} Lat/Lon")
pdms_b = Geopos(pos_b)
print(f"Result: "
      f"{pdms_b.latDeg} {pdms_b.latMin}'{pdms_b.latSec}\"{pdms_b.latDir}, "
      f"{pdms_b.lonDeg} {pdms_b.lonMin}'{pdms_b.lonSec}\"{pdms_b.lonDir}"
      )
opl = olc.encode(pos_b[0], pos_b[1])
print(f"Google map: {opl}")
betw = maiden.dist_az(pos_a, pos_b)
print(f"Distance: {betw[0]} km Azimuth: {betw[1]} deg")
