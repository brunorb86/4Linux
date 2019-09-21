with open("arquivo.txt", "r") as xx:
    conteudo = xx.read() + "\n"

dic = {"ID":"", "NOME":"", "IDADE":"", "SEXO":"", "PAIS":""}

#print(conteudo)

dic["ID"] = input("Digite o seu ID: ")
dic["NOME"] = input("Digite o seu nome: ")
dic["IDADE"] = input("Digite a sua idade: ")
dic["SEXO"] = input("INFOME SEXO (M/F): ")
dic["PAIS"] = input("INFORME PAIS ORIGEM:")

for dados in dic.values():
    conteudo += dados + ";"

print(conteudo)
print(dic)

for lista in dic:
    conteudo += ";" (conteudo) 
    


exit()
# Passo 1 - Abrir o arquivo

with open("arquivo.txt", "r") as cadastro: 
    conteudo = cadastro.readlines()
#    texto = cadastro.read()

print(conteudo)
# Passo 2 - Consultar pelo ID

#id = input ("Digite o ID para busca: ")

dic = {"ID":'', "NOME":'', "IDADE":'', "SEXO":'', "PAIS":''}

# Passo 3 - Busca

exit ()

for linha in conteudo:
    if id in linha:
        lista = linha.split(";")
        print("ID : {}".format(lista[0]))
        print("Nome : {}".format(lista[1]))
        print("Idade : {}".format(lista[2]))
        print("Sexo : {}".format(lista[3]))
        print("Nac : {}".format(lista[4]))

exit()





##Funcional
with open("numeros.txt") as numeros:
    total = 0
    texto = numeros.read()
print(texto.split())
resultado = texto.split()

for num in resultado:
    total += int(num)
print(total)
    

exit()
#with open("arquivo_novo.txt") as arquivo:

#Para criar novo arquivo
#with open("conteudo_novo2.txt", "a+") as newfile:
#    newfile.write(frase)
#    texto = newfile.read()
#    print(texto)  


#Para dar print
frase = 4 * "Conteudo do novo arquivo \n"
with open("conteudo_novo2.txt") as newfile:
#with open("conteudo_novo2.txt", "a+") as newfile:
#    newfile.write(frase)

    texto = newfile.read()
    print(texto)    
    

exit()

# Modo 1

#arquivo = open("arquivo.txt")
#print(arquivo)

#arquivo.close()

# Modo 2
##end_arquivo = (/home/xxxx)
## with open ("end_arquivo")
#File have just read permission, "w" to write, "a" to append

with open("arquivo.txt") as arquivo:
    texto = arquivo.read()
#    texto = arquivo.read(';') delimiter
print(texto.split())

frase = "Novo arquivo"
#frase = text + "Novo arquivo" -> Adicionando novo conteudo

with open("arquivo_novo.txt", "a+") as novoArquivo:
    novoArquivo.write(frase)
