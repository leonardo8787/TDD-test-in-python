import unittest
from arquivos.src.calcula import soma, subtrai

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5), 10)

    def test_subtrai_5_e_5_deve_retornar_0(self):
        self.assertEqual(subtrai(5,5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        )

        for x_y_saidas in x_y_saidas:
            x, y, saidas = x_y_saidas
            self.assertEqual(soma(x,y), saidas)

        def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
            with self.assertRaises(AssertionError):
                soma('11', 0)

        #def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        #    with self.assertRaises(AssertionError):
        #        soma(11, '0')

unittest.main(verbosity=2)