"""
    Main program for Module maidenhead
    Input geographical position, locator or Google plus code
    Author: 9V1KG Klaus D Goepel
    https://klsin.bpmsg.com
    https://github.com/9V1KG/Maiden
    Created On      : 2020-05-02
    Last Modified On: 2020-05-07
    License: http://www.fsf.org/copyleft/gpl.html
"""
from openlocationcode import openlocationcode as olc
import maidenhead
from maidenhead import Geodg2dms
from maidenhead import mhconv

switch = ["none", "Position: ", "Locator: ", "Plus code: "]


def main():
    """
    Main program to convert position, olc or locator
    """
    mhl = maidenhead.Maiden()
    print("""
Maidenhead locator program by 9V1KG

Input geographical position, maidenhead locator or Google plus code
to convert. Locator is calculated with 10 characters.
https://github.com/9V1KG/Maiden
        """)
    get_in = maidenhead.maiden.line_input()
    if get_in[0] == 1:
        print("\r\nConvert geographic location to Maidenhead locator")
        print(switch[get_in[0]], get_in[1])
        p_dms = Geodg2dms(get_in[1])
        print(f"{p_dms.lat_deg} {p_dms.lat_min}'{p_dms.lat_sec}\" {p_dms.lat_dir},"
              f" {p_dms.lon_deg} {p_dms.lon_min}'{p_dms.lon_sec}\" {p_dms.lon_dir}"
              )
        loc = mhl.latlon2maiden(get_in[1], 10)
        print(f"QTH Locator: {loc[:6]} {loc[6:]}")
        opl = olc.encode(get_in[1][0], get_in[1][1])
        print(f"Plus code:   {opl}")
    elif get_in[0] == 2:
        print("\r\nConvert Maidenhead locator to geographic location")
        print(switch[get_in[0]], get_in[1])
        pos_b = mhl.maiden2latlon(get_in[1])
        print(f"Result: {pos_b} Lat/Lon")
        pdms_b = Geodg2dms(pos_b)
        print(f"Result: "
              f"{pdms_b.lat_deg} {pdms_b.lat_min}'{pdms_b.lat_sec}\"{pdms_b.lat_dir}, "
              f"{pdms_b.lon_deg} {pdms_b.lon_min}'{pdms_b.lon_sec}\"{pdms_b.lon_dir}"
              )
        opl = olc.encode(pos_b[0], pos_b[1])
        print(f"Plus code: {opl}")
    elif get_in[0] == 3:
        print("\r\nCalculate Maidenhead locator from Google plus code")
        print(switch[get_in[0]], get_in[1])
        # pos_a = maiden.maiden2latlon(MY_LOC)
        # fc = olc.recoverNearest(get_in[1], pos_a[0], pos_a[1])
        # print(f"Google full code: {fc}")
        res = olc.decode(get_in[1])
        print(f"Lat: {res.latitudeCenter}, Lon: {res.longitudeCenter}")
        pdms_b = Geodg2dms((res.latitudeCenter, res.longitudeCenter))
        print(f"Result: "
              f"{pdms_b.lat_deg} {pdms_b.lat_min}'{pdms_b.lat_sec}\"{pdms_b.lat_dir}, "
              f"{pdms_b.lon_deg} {pdms_b.lon_min}'{pdms_b.lon_sec}\"{pdms_b.lon_dir}"
              )
        loc = mhl.latlon2maiden((res.latitudeCenter, res.longitudeCenter), 10)
        print(f"Locator: {loc[:6]} {loc[6:]}")


if __name__ == "__main__":
    mhconv.main()
