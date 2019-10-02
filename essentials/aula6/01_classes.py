class ContaCorrente:
    
    def __init__(self): ### Construtor
        self.ag = 0
        self.conta = 0
        self.saldo = 0
        self.titular = "Bruno Bonfim"
        self.n_saques = 10
        self.taxa_manutencao = 12.50
        
class ContaSalario (ContaCorrente):
    def __init__(self): ### Construtor
    self.ag = 0
    self.conta = 0
    self.saldo = 0
    self.titular = "Bruno Bonfim"
    self.n_saques = 2
    self.taxa_manutencao = 0
    
'''
## Comportamentos
    def verificar_saldo(self):
        print(saldo)
        
    def saque(self,valor):
        self.saldo -= valor
    
    def deposito(self,valor):
        self.saldo += valor
        
    def tranferencia(self, valor, cc):
        self.saldo -= valor
        cc.saldo += valor


def main():
    dados = ContaCorrente()

    print(dados.saque)
    dados.saque()
    print(dados.saldo)
    

if __name__ == "__main__":
    main()


# Objeto da classe

#   dados = ContaCorrente()
    dados.ag = ""
    dados.conta = ""
    dados.saldo = ""
    dados.titular = ""

    print(saldo)
'''
