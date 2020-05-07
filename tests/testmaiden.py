"""
Unit tests for module maiden
Maidenhead locator funtions
"""
from unittest import TestCase
from maidenhead.maiden import Maiden, Geodg2dms


class TestMaiden(TestCase):

    def setUp(self) -> None:
        self.lcl_maiden = Maiden()

    def test_init_ok(self):
        self.assertTrue(self.lcl_maiden)

    def test_is_class(self):
        self.assertIsInstance(self.lcl_maiden, Maiden)

    def test_f_10_24(self):
        self.assertEqual(Maiden.f_10_24(0), 10)
        self.assertEqual(Maiden.f_10_24(1), 1)
        self.assertEqual(Maiden.f_10_24(2), 1/24)
        self.assertEqual(Maiden.f_10_24(3), 1/240)
        self.assertEqual(Maiden.f_10_24(4), 1/240/24)
        self.assertEqual(Maiden.f_10_24(5), 1/240/240)

    def test_latlon2maiden(self):
        lat_lon = 48.058247, 11.623698
        res_str = "JN58tb43ux"
        for llen in range(4, 12, 2):
            self.assertEqual(Maiden.latlon2maiden(lat_lon, llen), res_str[:llen])
        self.assertEqual(Maiden.latlon2maiden(lat_lon, 12), "")
        self.assertEqual(Maiden.latlon2maiden(lat_lon, 7), "JN58tb")

    def test_maiden2latlon(self):
        loc = "JN58tb43ux"
        lat_lon = 48.058247, 11.623698
        self.assertEqual(Maiden.maiden2latlon(Maiden(), loc), lat_lon)
        loc = "JN58"
        lat_lon = 48.5, 10.5
        self.assertEqual(Maiden.maiden2latlon(Maiden(), loc), lat_lon)

    def test_dist_az(self):
        self.assertEqual(Maiden.dist_az((0., 0.), (0., 180.)), (20012, 90))
        self.assertEqual(Maiden.dist_az((-90., 0.), (90., 0.)), (20012, 0))

    def test_dg2dms(self):
        self.assertEqual(Geodg2dms.dg2dms((14.5+3/360, 120.5)), ((14, 30, 30, 'N'), (120, 30, 0, 'E')))
        self.assertEqual(Geodg2dms.dg2dms((-14.5-3/360, 120.5+3/360)), ((14, 30, 30, 'S'), (120, 30, 30, 'E')))
        self.assertEqual(Geodg2dms.dg2dms((-14.5+3/360, 120.5-3/360)), ((14, 29, 30, 'S'), (120, 29, 30, 'E')))
        self.assertEqual(Geodg2dms.dg2dms((14.5, -120.5)), ((14, 30, 0, 'N'), (120, 30, 0, 'W')))
        self.assertEqual(Geodg2dms.dg2dms((-14.5, -120.5)), ((14, 30, 0, 'S'), (120, 30, 0, 'W')))

    def test_geodg2dms(self):
        self.assertEqual(Geodg2dms((14.5, 120.5)).lat_deg, 14)
        self.assertEqual(Geodg2dms((14.5, 120.5)).lat_min, 30)
        self.assertEqual(Geodg2dms((14.5+3/360, 120.5)).lat_sec, 30)
        self.assertEqual(Geodg2dms((14.5, 120.5)).lat_dir, "N")
        self.assertEqual(Geodg2dms((-14.5, 120.5)).lat_dir, "S")
        self.assertEqual(Geodg2dms((14.5, 120.5)).lon_deg, 120)
        self.assertEqual(Geodg2dms((14.5, 120.5)).lon_min, 30)
        self.assertEqual(Geodg2dms((14.5, 120.5+3/360)).lon_sec, 30)
        self.assertEqual(Geodg2dms((14.5, 120.5)).lon_dir, "E")
        self.assertEqual(Geodg2dms((14.5, -120.5)).lon_dir, "W")






