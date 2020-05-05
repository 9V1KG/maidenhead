"""
    Module with functions for maidenhead locator calculations
    Author: 9V1KG Klaus D Goepel
    https://klsin.bpmsg.com
    https://github.com/9V1KG/Maiden
    Created On      : 2020-05-02
    Last Modified On: 2020-05-03
    License: http://www.fsf.org/copyleft/gpl.html
"""
import re
import math


class Maiden:
    """
    Maidenhead locator functions
    latlon2maiden: lat/lon position to locator
    maiden2latlon: locator to lat/long position
    Geodg2dms (class) dec deg to deg, min, sec

    """

    def __init__(self):
        pass

    @staticmethod
    def latlon2maiden(latlon: tuple, loc_len: int) -> str:
        """
        Calculates maiden locator based on position
        :param latlon: latitude/longitude decimal
        :param loc_len: precision 4 to 10
        :return: Maidenhead locator string or empty string
        """
        if not 4 <= loc_len <= 10:
            return ""  # between 4 to 10 chars
        if divmod(loc_len, 2)[1] > 0:  # must be even
            loc_len = 2 * divmod(loc_len, 2)[0]
        # main square 20 dg by 10 deg
        l_a = divmod(latlon[0] + 90, 10)
        l_o = divmod(latlon[1] + 180, 20)
        a_str = chr(ord("A") + int(l_o[0])) + chr(ord("A") + int(l_a[0]))
        lon = l_o[1] / 2
        lat = l_a[1]
        for i in range(1, int(loc_len / 2)):
            l_o = divmod(lon, 1)
            l_a = divmod(lat, 1)
            if (i + 1) % 2:
                a_str += chr(ord("a") + int(l_o[0])) + chr(ord("a") + int(l_a[0]))
                lon = 10 * l_o[1]
                lat = 10 * l_a[1]
            else:
                a_str += str(int(l_o[0])) + str(int(l_a[0]))
                lon = 24 * l_o[1]
                lat = 24 * l_a[1]
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
        for i, (x_1, x_2) in enumerate(pairs):
            lon += self.f_10_24(i) * x_1
            lat += self.f_10_24(i) * x_2
        lon *= 2
        lon += self.f_10_24(i) / 2  # Centre of the field
        lat += self.f_10_24(i) / 2
        return round(lat, 6), round(lon, 6)

    @staticmethod
    def dist_az(pos1: tuple, pos2: tuple) -> tuple:
        """
        Calculates distance and compass direction between pos1 and 2
        :param pos1: Latitude, Longitude position 1
        :param pos2: Latitude, Longitude position 2
        :return: distance and azimuth
        """
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
        x_1 = math.sin(dlon) * math.cos(lat2)
        x_2 = math.cos(lat1) * math.sin(lat2) \
            - (math.sin(lat1) * math.cos(lat2) * math.cos(dlon))

        azimuth = math.atan2(x_1, x_2)
        azimuth = math.degrees(azimuth)
        azimuth = round((azimuth + 360) % 360)
        return dist, azimuth


class Geodg2dms():
    def __init__(self, pos: tuple):
        pos_dms = self.dg2dms(pos)
        self.lat_deg = pos_dms[0][0]
        self.lat_min = pos_dms[0][1]
        self.lat_sec = pos_dms[0][2]
        self.lat_dir = pos_dms[0][3]
        self.lon_deg = pos_dms[1][0]
        self.lon_min = pos_dms[1][1]
        self.lon_sec = pos_dms[1][2]
        self.lon_dir = pos_dms[1][3]

    @staticmethod
    def dg2dms(latlon: tuple) -> tuple:
        """
        Convert decimal degrees in (deg min sec dir)
        :param latlon: latitude and longitude in degree
        :return: latitude and longitude in (deg min dir)
        """
        latitude: tuple = (
            round(divmod(abs(latlon[0]), 1)[0]),
            round(60 * divmod(abs(latlon[0]), 1)[1]),
            round(divmod(3600 * divmod(abs(latlon[0]), 1)[1], 60)[1]),
            "N" if latlon[0] > 0 else "S"
        )
        longitude: tuple = (
            round(divmod(abs(latlon[1]), 1)[0]),
            round(60 * divmod(abs(latlon[1]), 1)[1]),
            round(divmod(3600 * divmod(abs(latlon[1]), 1)[1], 60)[1]),
            "E" if latlon[1] > 0 else "W"
        )
        return latitude, longitude

    def __repr__(self):
        return str(
            [self.lat_deg, self.lat_min, self.lat_sec, self.lat_dir,
             self.lon_deg, self.lon_min, self.lon_sec, self.lon_dir]
        )
