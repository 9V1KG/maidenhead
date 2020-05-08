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
import maidenhead.maiden
from maidenhead.maiden import Maiden, Geodg2dms

MY_LOC = "PK04lc68dj"
COL = maidenhead.maiden.COL

MAIDEN = Maiden()  # Initialize class
print("""
Maidenhead locator program by 9V1KG
https://github.com/9V1KG/Maiden
        """)
print(f"{COL.green}Calculates distance and azimuth from your locator (\"MY_LOC\"){COL.end}")
print(f"My locator: {MY_LOC}")
POS_A = MAIDEN.maiden2latlon(MY_LOC)
print(f"My pos: {POS_A} Lat/Lon")
PDMS_A = Geodg2dms(POS_A)
print(f"My pos: "
      f"{PDMS_A.lat_deg} {PDMS_A.lat_min}'{PDMS_A.lat_sec}\"{PDMS_A.lat_dir}, "
      f"{PDMS_A.lon_deg} {PDMS_A.lon_min}'{PDMS_A.lon_sec}\"{PDMS_A.lon_dir}"
      )
opl = olc.encode(POS_A[0], POS_A[1])
print(f"Google map: {opl}\r\n")

line = input("Input Maidenhead Locator (4 to 10 char): ")
if not re.match(r"([A-Ra-r]{2}\d\d)(([A-Za-z]{2})(\d\d)?){0,2}", line):
    print("Locator has 2 to 5 character/number pairs, like PK04lc")
    sys.exit(1)
pos_b = MAIDEN.maiden2latlon(line)
print(f"Result: {COL.yellow}{pos_b}{COL.end} Lat/Lon")
pdms_b = Geodg2dms(pos_b)
print(f"Result: "
      f"{pdms_b.lat_deg} {pdms_b.lat_min}'{pdms_b.lat_sec}\"{pdms_b.lat_dir}, "
      f"{pdms_b.lon_deg} {pdms_b.lon_min}'{pdms_b.lon_sec}\"{pdms_b.lon_dir}"
      )
opl = olc.encode(pos_b[0], pos_b[1])
print(f"Google map: {opl}")
betw = MAIDEN.dist_az(POS_A, pos_b)
print(f"Distance: {COL.yellow}{betw[0]} km{COL.end} "
      f"Azimuth: {COL.yellow}{betw[1]} deg{COL.end}")
