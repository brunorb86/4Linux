#arquivos

with open("arquivo.txt", "r") as x:
    conteudo = x.read()
    
print(conteudo)

dic = {"ID":'', "NOME":'', "IDADE":'', "SEXO":'', "PAIS":''}

exit()
dic["ID"] = input("Digite o seu ID: ")
dic["NOME"] = input("Digite o seu nome: ")
dic["IDADE"] = input("Digite a sua idade: ")
dic["SEXO"] = input("INFOME SEXO (M/F): ")
dic["PAIS"] = input("INFORME PAIS ORIGEM:")

for value in dic.values():
    conteudo += value + ';'

conteudo += "\n"    
print(conteudo)

exit()
busca = input("Digite o ID para busca:")

for elemento in conteudo:
    if busca in elemento:
        lista = elemento.split(';')
        print(lista[0])
        print(lista[1])
        print(lista[2])
    
### inserir registros
