import unittest
from decimal import Decimal
from domain import convert

class TestConvert(unittest.TestCase):
    def test_valor_medio(self):
        self.assertEqual(convert(100, 6.96), Decimal("685.96"))

    def test_redondeo_bancario_borde(self):
        self.assertEqual(convert(10.5, 6.96), Decimal("71.76"))

    def test_bajo_minimo(self):
        with self.assertRaises(ValueError) as ctx:
            convert(1.0, 1.05)
        self.assertEqual(str(ctx.exception), "Below minimum payout")

    def test_fx_diferentes(self):
        self.assertGreater(convert(100, 7.10), convert(100, 6.90))

    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            convert(0, 6.96)
        with self.assertRaises(ValueError):
            convert(100, 0)

if __name__ == '__main__':
    unittest.main()
