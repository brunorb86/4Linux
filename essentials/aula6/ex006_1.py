from ex05 import Carro
import unittest

class TestaCarro (unittest.TestCase):

    def testeAcelerar (self):
        """ Function doc """
        sentra = Carro()
        sentra.acelerar() # sentra.velocidade = 10
        sentra.acelerar()
        self.assertEqual(20, sentra.velocidade)
        
if __name__ == "__main__":
    unittest.main()
