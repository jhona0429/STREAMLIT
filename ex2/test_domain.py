import unittest
from domain import reorder_point

class TestROP(unittest.TestCase):
    def test_tipico(self):
        self.assertEqual(reorder_point(50, 2, 10, 1.65), 124)

    def test_lead_time_decimal(self):
        self.assertEqual(reorder_point(40, 2.2, 8, 1.65), 143)

    def test_demanda_cero(self):
        self.assertEqual(reorder_point(0, 3.5, 12, 1.96), 48)

    def test_sigma_cero(self):
        self.assertEqual(reorder_point(30, 1.2, 0, 1.65), 60)

    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            reorder_point(-1, 2, 10, 1.65)
        with self.assertRaises(ValueError):
            reorder_point(50, -2, 10, 1.65)
        with self.assertRaises(ValueError):
            reorder_point(50, 2, -10, 1.65)
        with self.assertRaises(ValueError):
            reorder_point(50, 2, 10, -1.65)

if __name__ == '__main__':
    unittest.main()
