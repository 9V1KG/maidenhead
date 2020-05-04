import re
from maiden import Maiden, Geopos
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
p = Geopos((lat, lon))
print( 13 * " "
       + f"{p.latDeg} {p.latMin}'{p.latSec}\" {p.latDir}, "
         f"{p.lonDeg} {p.lonMin}'{p.lonSec}\" {p.lonDir}"
)
loc = maiden.latlon2maiden((lat, lon), 10)
print(f"QTH Locator: {loc[:6]} {loc[6:]}")
opl = olc.encode(lat, lon)
print(f"Plus code:   {opl}")
