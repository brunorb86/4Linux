while True:
    try:
        n1= float(input("Digite N1: "))
        n2= float(input("Digite N2: "))
    except ValueError as err:
        print ("Digite apenas 1,2,3,4 ou 5")
        #break
    else:
        print("Escolha sua opcao:")
        print(" 1 - SOMA")
        print(" 2 - SUBTRACAO")
        print(" 3 - DIVISAO")
        print(" 4 - MULTIPLICACAO")
        print(" 5 - SAIR")

        opcao= int(input("Digite a opcao:"))

        if opcao == 1:
            print("{0:.2f} + {1:.2f} = {2:.2f}".format(n1,n2,n1+n2))
        elif opcao == 2:
            print("{0:.2f} + {1:.2f} = {2:.2f}".format(n1,n2,(n1-n2)))
        elif opcao == 3:
            print("{0:.2f} + {1:.2f} = {2:.2f}".format(n1,n2,(n1/n2)))
        elif opcao == 4:
            print("{0:.2f} + {1:.2f} = {2:.2f}".format(n1,n2,(n1*n2)))
        elif opcao == 5:
            print("Obrigado!")
            break
        else:
            print("Opcao Invalida!")
    #except Exception as err:




'''
############################################################
def div(x,y):
    try:
        return x/y
    except ZeroDivisionError as err:
        print('Nao divisivel por 0')
        
    else:
        return x/y
div(4,0)


print('Escolha uma opção:\n1 - Banana\n2 - Melancia\n3 - Sair')
try:
    opcao = int(input(""))
except ValueError as err:
    print("Digite apenas números")
else:
    print(opcao)

############################################################


try:
    with open("arquivoinexistente") as f:
        conteudo= f.read()
        
except  FileNotFoundError as err:
    print("Arquivo não encontrado")
    #print(err)

else:
    print(conteudo)

############################################################

while True:
    try:
        x = int(input('Digite um numero: '))
        y = int(input('Digite outro numero: '))
        print( x + y )
    except Exception as e:
        print("Digite apenas numeros")
'''
