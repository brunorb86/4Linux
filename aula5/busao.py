#Classes
class Busao:
    
    def __init__(self):
        self.ano = ""
        self.linha = ""
        self.lugares = ""
        self.capacidade_atual = 80
        self.pegar_passageiros = 0
        self.deixar_passageiros = 0

    #comportamentos
    def pegar(self):
        self.pegar_passageiros += 3 
       
    def despachar(self):
        self.deixar_passageiros -= 2
        
def main():
# Objeto da classe
    onibus = Busao()
    onibus.ano = "2010"
    onibus.linha = "Barra Funda"
    onibus.lugares = "45"

    onibus.pegar()
    onibus.pegar()
    onibus.pegar()
    onibus.pegar()
    print(onibus.pegar_passageiros)
    onibus.despachar()
    print(onibus.deixar_passageiros)
    x = self.pegar_passageiros - self.deixar_passageiros
        print(x)
if __name__ == "__main__":
    main()
