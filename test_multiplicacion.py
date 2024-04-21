#test multiplicacion.py

import unittest
from multiplicacion import multiplicar
class TestMultiplicar(unittest.TestCase):
    def test_multipicar(self):
        self.assertEqual(multiplicar(3,2),6)
        self.assertEqual(multiplicar(-1,1),-1)
        self.assertEqual(multiplicar(-1,-1),1)

if __name__ == '__main__':
    unittest.main()

    