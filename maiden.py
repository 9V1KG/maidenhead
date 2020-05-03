#!/usr/bin/python3

import re
import sys
import math
from openlocationcode import openlocationcode as olc


class Maiden:
    """
    Maidenhead locator functions
    License: http://www.fsf.org/copyleft/gpl.html
    9V1KG Klaus D Goepel
    https://klsin.bpmsg.com
    https://github.com/9V1KG/Maiden
    Created On      : 2020-05-02
    Last Modified On: 2020-05-03
    """

    def __init__(self):
        pass

    @staticmethod
    def dgdec2dgmn(latlon: tuple) -> tuple:
        """
        Convert decimal degrees in (deg min dir)
        :param latlon: latitude and longitude in degreed
        :return: latitude and longitude in (deg min dir)
        """
        latitude: tuple = (
            abs(int(latlon[0])),
            round(abs(latlon[0] % int(latlon[0])) * 60, 3),
            "N" if latlon[0] > 0 else "S"
        )
        longitude: tuple = (
            abs(int(latlon[1])),
            round(abs(latlon[1] % int(latlon[1])) * 60, 3),
            "E" if latlon[1] > 0 else "W"
        )
        return latitude, longitude

    @staticmethod
    def latlon2maiden(latlon: tuple, loc_len: int) -> str:
        """
        Calculates maiden locater based on position
        :param latlon: latitude/longitude decimal
        :param loc_len: precision 4 to 10
        :return: Maidenhead locator string or empty string
        """
        if not 4 <= loc_len <= 10:
            return ""  # between 4 to 10 chars
        elif divmod(loc_len, 2)[1] > 0:  # must be even
            loc_len = 2 * divmod(loc_len, 2)[0]
        # main square 20 dg by 10 deg
        la = divmod(latlon[0] + 90, 10)
        lo = divmod(latlon[1] + 180, 20)
        a_str = chr(ord("A") + int(lo[0])) + chr(ord("A") + int(la[0]))
        lon = lo[1] / 2
        lat = la[1]
        for i in range(1, int(loc_len / 2)):
            lo = divmod(lon, 1)
            la = divmod(lat, 1)
            if (i + 1) % 2:
                a_str += chr(ord("a") + int(lo[0])) + chr(ord("a") + int(la[0]))
                lon = 10 * lo[1]
                lat = 10 * la[1]
            else:
                a_str += str(int(lo[0])) + str(int(la[0]))
                lon = 24 * lo[1]
                lat = 24 * la[1]
        return a_str

    @staticmethod
    def f_10_24(j: int) -> float:
        """
        Fractional resolution of latitude
        :param j: index of letter/number pair
        :return: calculated fractional degrees
        """
        return 10 ** (1 - int((j + 1) / 2)) * 24 ** int(-j / 2)

    def maiden2latlon(self, loc: str) -> tuple:
        """
        Calculates latitude, longitude in decimal degrees,
        centre of the field depending on resolution
        :param loc: Maidenhead locator 4 up to 10 characters
        :return: lon, lat (dg decimal) or None, None (invalid input)
        """
        lon = lat = -90
        # check validity of input
        if not re.match(r"([A-Ra-r]{2}\d\d)(([A-Za-z]{2})(\d\d)?){0,2}", loc):
            return None, None
        lets = re.findall(r'([A-Xa-x]{2})', loc)  # all letter pairs
        nums = re.findall(r'(\d)(\d)', loc)  # all number pairs
        vals = [(ord(x[0].upper()) - ord("A"),
                 ord(x[1].upper()) - ord("A")) for x in lets]
        nums = [(int(x[0]), int(x[1])) for x in nums]
        pairs = [tuple] * (len(vals) + len(nums))  # prepare empty list
        pairs[::2] = vals  # letter value pairs 0, 2, 4 ...
        pairs[1::2] = nums  # number value pairs 1, 3, 5 ...
        for i, (x, y) in enumerate(pairs):
            lon += self.f_10_24(i) * x
            lat += self.f_10_24(i) * y
        lon *= 2
        lon += self.f_10_24(i) / 2  # Centre of the field
        lat += self.f_10_24(i) / 2
        return lat, lon

    @staticmethod
    def dist_az(pos1: tuple, pos2: tuple) -> tuple:
        lat1 = math.radians(pos1[0])
        lon1 = math.radians(pos1[1])
        lat2 = math.radians(pos2[0])
        lon2 = math.radians(pos2[1])
        dlon = math.radians(pos2[1]-pos1[1])
        # compare identical inputs
        if lat1 == lat2 and lon1 == lon2:
            return 0., 0.
        dist = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) \
               * math.cos(lat2) * math.cos(dlon)
        dist = round(math.degrees(math.acos(dist)) * 60 * 1.853)
        x = math.sin(dlon) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) \
            - (math.sin(lat1) * math.cos(lat2) * math.cos(dlon))

        azimuth = math.atan2(x, y)
        azimuth = math.degrees(azimuth)
        azimuth = round((azimuth + 360) % 360)
        return dist, azimuth


if __name__ == "__main__":
    my_loc = "PK04lc68dj"
    maiden = Maiden()

    pos_a = maiden.maiden2latlon(my_loc)
    print(f"My locator: {my_loc}")
    print(f"My pos: {maiden.dgdec2dgmn(pos_a)}")
    opl = olc.encode(pos_a[0], pos_a[1])
    print(f"Google map: {opl}")
