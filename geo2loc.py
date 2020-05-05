"""
    Calculates maidenhead locator from geographical position
    Author: 9V1KG Klaus D Goepel
    https://klsin.bpmsg.com
    https://github.com/9V1KG/Maiden
    Created: 2020-05-02
    License: http://www.fsf.org/copyleft/gpl.html
"""
import re
from maiden import Maiden, Geodg2dms
from openlocationcode import openlocationcode as olc


maiden = Maiden()
print("Convert geographic location to Maidenhead locator")
ll = None
lat: float = 0.
lon: float = 0.
while not ll:
    line = input("Input Lat,Lon (dec): ")
    #  ll = re.findall(r'([-0-9.]+)[\s,]+([-0-9.]+)', line)
    ll = re.findall(r'(-?\d{1,3}\.?\d*)\s*,\s*(-?\d{1,3}\.?\d*)', line)
    if ll:
        lat = float(ll[0][0])
        lon = float(ll[0][1])
        if -90 >= lat >= 90 and -180 >= lon >= 180:
            break
        break
    print("Invalid input, Lat,Lon (dec): ")
print(f"Position:    {lat} {lon}")
p = Geodg2dms((lat, lon))
print( 13 * " "
       + f"{p.lat_deg} {p.lat_min}'{p.lat_sec}\" {p.lat_dir}, "
         f"{p.lon_deg} {p.lon_min}'{p.lon_sec}\" {p.lon_dir}"
)
loc = maiden.latlon2maiden((lat, lon), 10)
print(f"QTH Locator: {loc[:6]} {loc[6:]}")
opl = olc.encode(lat, lon)
print(f"Plus code:   {opl}")
