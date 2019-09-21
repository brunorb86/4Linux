#Classes
class Carro:
    
    def __init__(self):
        self.cor = ""
        self.modelo = ""
        self.ano = 0
        self.velocidade = 0
    

    #comportamentos
    def acelerar(self):
        self.velocidade += 10
#       pass -> para pular o bloco
        
    def frear(self):
        self.velocidade /= 2
        
def main():
# Objeto da classe

    fusca = Carro()
    fusca.cor = "Amarelo"
    #fusca.cor = input("Qual a cor? ")
    fusca.modelo = "VW Fusca"
    fusca.ano = "1975"

    print(fusca.velocidade)
    fusca.acelerar()
    print(fusca.velocidade)
    fusca.frear()
    print(fusca.velocidade)
    fusca.frear()
    print(fusca.velocidade)


if __name__ == "__main__":
    main()
#print(fusca.cor)
