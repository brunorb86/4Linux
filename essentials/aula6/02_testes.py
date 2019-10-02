import unittest
from 01_classes import ContaCorrente, ContaSalario

# Objetos globais - funcoes globais
cc = ContaCorrente()
cs = ContaSalario()
class testaConta (unittest.TestCase):
    def test_construtorCC(self):
        self.assertEqual(0,cc.ag)
        self.assertEqual(0,cc.conta)
        self.assertEqual(0,cc.saldo)
        self.assertEqual(0,cc.titular)
        self.assertEqual(0,cc.n_saques)
        self.assertEqual(0,cc.taxa_manutencao)


if __name__ == "__main__":
    unittest.main()
