import sys
import re
from maiden import Maiden
from openlocationcode import openlocationcode as olc

my_loc = "PK04lc68dj"
# my_loc = "OJ11XI21dc"
maiden = Maiden()
print(f"My locator {my_loc}")
pos_a = maiden.maiden2latlon(my_loc)
print(f"My pos: {maiden.dgdec2dgmn(pos_a)}")
opl = olc.encode(pos_a[0], pos_a[1])
print(f"Google map: {opl}")

print("Input locator:")
line = sys.stdin.readline()
if not re.match(r"([A-Ra-r]{2}\d\d)(([A-Za-z]{2})(\d\d)?){0,2}", line):
    print("Locator has 2 to 5 character/number pairs, like PK04oj")
    sys.exit(1)
pos_b = maiden.maiden2latlon(line)
print(maiden.dgdec2dgmn(pos_b))
opl = olc.encode(pos_b[0], pos_b[1])
print(f"Google map: {opl}")
betw = maiden.dist_az(pos_a, pos_b)
print(f"Distance: {betw[0]} km Azimuth: {betw[1]} deg")
