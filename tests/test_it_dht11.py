import unittest

from stockpi.dht11 import _unpack_dht_data


class Dht11TestCase(unittest.TestCase):
    def test_unpack_dht_data(self):
        raw = [0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0]
        rh, temp = _unpack_dht_data(raw)
        self.assertEqual(0.0, rh)
        self.assertEqual(0.0, temp)


if __name__ == '__main__':
    unittest.main()
