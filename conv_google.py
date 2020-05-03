from maiden import Maiden
from openlocationcode import openlocationcode as olc

my_loc = "OJ11xi"
maiden = Maiden()
print(f"My locator {my_loc}")
pos_a = maiden.maiden2latlon(my_loc)
print(f"My pos: {maiden.dgdec2dgmn(pos_a)}")

line = input("Input Google olc: ")
fc = olc.recoverNearest(line, pos_a[0],pos_a[1])
print(fc)
res = olc.decode(fc)
print(res)