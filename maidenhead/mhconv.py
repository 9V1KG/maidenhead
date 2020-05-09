"""
    Main program for Module maidenhead
    Input geographical position, locator or Google plus code
    Author: 9V1KG Klaus D Goepel
    https://klsin.bpmsg.com
    https://github.com/9V1KG/maidenhead
    Created On      : 2020-05-02
    Last Modified On: 2020-05-08
    License: http://www.fsf.org/copyleft/gpl.html
"""
from openlocationcode import openlocationcode as olc
import maidenhead.maiden

COL = maidenhead.maiden.COL
SWITCH = ["none", "Position: ", "Locator: ", "Plus code: "]


def main():
    """
    Main program to convert position, olc or locator
    """
    mhl = maidenhead.maiden.Maiden()
    print("""
Maidenhead locator program by 9V1KG

Input geographical position, maidenhead locator or Google plus code
to convert. Locator is calculated with 10 characters.
https://github.com/9V1KG/mqaidenhead
        """)
    get_in = maidenhead.maiden.line_input()
    if get_in[0] == 1:
        print(
            f"\r\n{COL.green}Convert geographic location to Maidenhead locator{COL.end}"
        )
        print(SWITCH[get_in[0]], get_in[1])
        p_dms = maidenhead.maiden.Geodg2dms(get_in[1])
        print(10 * " " +
              f" {p_dms.lat_deg} {p_dms.lat_min}'{p_dms.lat_sec}\" {p_dms.lat_dir},"
              f" {p_dms.lon_deg} {p_dms.lon_min}'{p_dms.lon_sec}\" {p_dms.lon_dir}"
              )
        loc = mhl.latlon2maiden(get_in[1], 10)
        print(f"Locator:   {COL.yellow}{loc[:6]} {loc[6:]}{COL.end}")
        opl = olc.encode(get_in[1][0], get_in[1][1])
        print(f"Plus code: {COL.yellow}{opl}{COL.end}")
    elif get_in[0] == 2:
        print(f"\r\n{COL.green}Convert Maidenhead locator to geographic location{COL.end}")
        print(SWITCH[get_in[0]], get_in[1])
        pos_b = mhl.maiden2latlon(get_in[1])
        print(f"Result: {pos_b} Lat/Lon")
        pdms_b = maidenhead.Geodg2dms(pos_b)
        print(f"Result:  {COL.yellow}"
              f"{pdms_b.lat_deg} {pdms_b.lat_min}'{pdms_b.lat_sec}\"{pdms_b.lat_dir}, "
              f"{pdms_b.lon_deg} {pdms_b.lon_min}'{pdms_b.lon_sec}\"{pdms_b.lon_dir}{COL.end}"
              )
        opl = olc.encode(pos_b[0], pos_b[1])
        print(f"Plus code: {COL.yellow}{opl}{COL.end}")
    elif get_in[0] == 3:
        print(f"\r\n{COL.green}Calculate Maidenhead locator from Google plus code{COL.end}")
        print(SWITCH[get_in[0]], get_in[1])
        res = olc.decode(get_in[1])
        print(
            f"Lat: {round(res.latitudeCenter, 6)}, "
            f"Lon: {round(res.longitudeCenter, 6)}")
        pdms_b = maidenhead.Geodg2dms((res.latitudeCenter, res.longitudeCenter))
        print(f"Result:  {COL.yellow}"
              f"{pdms_b.lat_deg} {pdms_b.lat_min}'{pdms_b.lat_sec}\"{pdms_b.lat_dir}, "
              f"{pdms_b.lon_deg} {pdms_b.lon_min}'{pdms_b.lon_sec}\"{pdms_b.lon_dir}{COL.end}"
              )
        loc = mhl.latlon2maiden((res.latitudeCenter, res.longitudeCenter), 10)
        print(f"Locator: {COL.yellow}{loc[:6]} {loc[6:]}{COL.end}")


if __name__ == "__main__":
    main()
