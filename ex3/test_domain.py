import unittest
from domain import is_strong_password

class TestPwd(unittest.TestCase):
    def test_valida(self):
        self.assertTrue(is_strong_password("Abcdef1!xy", "jose"))

    def test_contiene_usuario(self):
        self.assertFalse(is_strong_password("xxJOSEyy1!", "José"))

    def test_falta_simbolo(self):
        self.assertFalse(is_strong_password("Abcdefg12x", "ana"))

    def test_repeticiones(self):
        self.assertFalse(is_strong_password("Ab111cdef!", "ana"))
        self.assertFalse(is_strong_password("AAAbcdef1!", "ana"))

    def test_espacios(self):
        self.assertFalse(is_strong_password(" Abcdef1!xy", "ana"))
        self.assertFalse(is_strong_password("Abcdef1!xy ", "ana"))

    def test_longitud_minima(self):
        self.assertTrue(is_strong_password("A1!bcdefgh", "ana"))

    def test_tipos_invalidos(self):
        self.assertFalse(is_strong_password(1234567890, "ana"))
        self.assertFalse(is_strong_password("Abcdef1!xy", None))

if __name__ == '__main__':
    unittest.main()
