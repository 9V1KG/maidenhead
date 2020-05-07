import Maiden
from Maiden import Geodg2dms
from openlocationcode import openlocationcode as olc

switch = ["none", "Position: ", "Locator: ", "Plus code: "]

if __name__ == "__main__":
    maiden = Maiden.Maiden
    print("""
Maidenhead locator program by 9V1KG

Input geographical position, maidenhead locator or Google plus code
to convert. Locator is calculated with 10 characters.
https://github.com/9V1KG/Maiden
        """)
    get_in = Maiden.maiden.line_input()
    if get_in[0] == 1:
        print("\r\nConvert geographic location to Maidenhead locator")
        print(switch[get_in[0]], get_in[1])
        p = Geodg2dms(get_in[1])
        print(f"{p.lat_deg} {p.lat_min}'{p.lat_sec}\" {p.lat_dir},"
              f" {p.lon_deg} {p.lon_min}'{p.lon_sec}\" {p.lon_dir}"
              )
        loc = maiden.latlon2maiden(get_in[1], 10)
        print(f"QTH Locator: {loc[:6]} {loc[6:]}")
        opl = olc.encode(get_in[1][0], get_in[1][1])
        print(f"Plus code:   {opl}")
    elif get_in[0] == 2:
        print("\r\nConvert Maidenhead locator to geographic location")
        print(switch[get_in[0]], get_in[1])
        pos_b = maiden.maiden2latlon(maiden(), get_in[1])
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
        loc = maiden.latlon2maiden((res.latitudeCenter, res.longitudeCenter), 10)
        print(f"Locator: {loc[:6]} {loc[6:]}")
