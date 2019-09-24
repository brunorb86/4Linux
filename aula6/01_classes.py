class ContaCorrente:
    
    def __init__(self):
        self.ag = 7348
        self.conta = 19212
        self.saldo = 1000
        self.titular = "Bruno Bonfim"

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

'''
# Objeto da classe

#   dados = ContaCorrente()
    dados.ag = ""
    dados.conta = ""
    dados.saldo = ""
    dados.titular = ""

    print(saldo)
'''
