from tests.testmaiden import TestMaiden

if __name__ == "__main__":
    tests = TestMaiden()
    tests.setUp()
    tests.test_init_ok()
    tests.test_is_class()
    tests.test_latlon2maiden()
    tests.test_maiden2latlon()
    tests.test_dg2dms()
    tests.test_dist_az()
    tests.test_f_10_24()
    tests.test_geodg2dms()
