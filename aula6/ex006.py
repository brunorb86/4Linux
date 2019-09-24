## Herança
## Reaproveitamento de codigo
## Herança mũltipla
        
class Pai:
    def __init__(self):
        self.nome="João"
        self.nacionalidade="Bra"

    def falar_PTBR(self):
        print("Eu falo portugues")
#        return "Eu falo portugues" 

class Mae:
    def __init__(self):
        self.nome="Alice"
        self.nacionalidade="Ale"
    
    def falar_ALE(self):
        print("Eu falo alemao")
    
class Filha(Pai,Mae):
    def __init__(self):
        self.nome="Ana"
        self.nacionalidade="Bra"

def main():
#    print("teste")
    pessoa = Filha()
    pessoa.falar_PTBR()
    pessoa.falar_ALE()

if __name__ == "__main__":
    main()
