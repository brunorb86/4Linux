for lista in range(9):
    print (lista)

exit () 
## CALCULADORA NAO FUNCIONAL ##
while True:
    n1 = float(input("Digite o numero 1: "))
    n2 = float(input("Digite o numero 2: "))
    calc = int(input("Digite 1 para soma, 2 para sub, 3 para div, 4 para mult ou 5 para sair: "))
#while calc < 4 and calc >= 1:
#while True:
    if calc == 1:
        print ("O resultado da soma {} + {} = {}".format(n1,n2,n1+n2))
    elif calc == 2:
        print ("O resultado da sub {} - {} = {}".format(n1,n2,n1-n2))
    elif calc == 3:
        print ("O resultado da div {} / {} = {}".format(n1,n2,n1/n2))
    elif calc == 4:
        print ("O resultado da sub {} * {} = {}".format(n1,n2,n1*n2))
    elif calc >= 6:
        print ("Wrong!")
    else:
        print ("Tchau")
        break
       
    
exit () 

## CALCULADORA FUNCIONAL ##
n1 = float(input("Digite o numero 1: "))
n2 = float(input("Digite o numero 2: "))
calc = int(input("Digite 1 para soma, 2 para sub, 3 para div, 4 para mult ou 5 para sair: "))
if calc == 1:
print ("O resultado da soma {} + {} = {}".format(n1,n2,n1+n2))
#print ("O resultado da soma {0:.2f} + {1:.2f} = {2:.2f}".format(n1,n2,n1+n2)) #Jeito correto de relacionarclear
elif calc == 2:
    print ("O resultado da sub {} - {} = {}".format(n1,n2,n1-n2))
elif calc == 3:
    print ("O resultado da div {} / {} = {}".format(n1,n2,n1/n2))
elif calc == 4:
    print ("O resultado da sub {} * {} = {}".format(n1,n2,n1*n2))
else:
    print ("Tchau")
    
exit ()    
#Menu
print ("1 - Soma")
print ("2 - Sub")

#Float
# {0:.2f} + {0:.2f}# 2 casas ou algum numero quebrado

exit() 
##Funcional##
nasc = int(input("Digite o ano de nascimento: "))
if nasc <= 1966:
    print("{} Você é um Baby Boomer".format(nasc)) #Como usar o "echo" do bash
elif nasc <= 1980:
    print("Você é da geração X")
elif nasc <= 1999:
    print("Você é da geração Y")
else:
    print("Você é da geraçao Z")
exit() 

#ZUADO
nasc = float(input("Digite o ano de nascimento: "))
if nasc <= 1966:
    print("Você é um Baby Boomer")
elif nasc >= 1967 or nasc <= 1980:
    print("Você é da geração X")
elif nasc >= 1981 or nasc <= 1999:
    print("Você é da geração Y")
#else:
#    print("Você é da geração Z")
#elif nasc >= 2000:
#    print("Você é da geraçao Z")
exit() 

#ZUADO
nasc = float(input("Digite o ano de nascimento: "))
if nasc <= 1966:
    print("Você é um Baby Boomer")
elif nasc < 1967 and nasc == 1980:
    print("Você é da geração X")
elif nasc < 1981 and nasc == 1999:
    print("Você é da geração Y")
else:
    print("Você é da geração Z")
#elif nasc >= 2000:
#    print("Você é da geraçao Z")
exit() 

#ZUADO
nasc = float(input("Digite o ano de nascimento: "))
if nasc <= 1966:
    print("Você é um Baby Boomer")
elif nasc <= 1980:
    print("Você é da geração X")
elif nasc <= 1999:
    print("Você é da geração Y")
else:
    print("Você é da geraçao Z")

exit()  
nota1 = input("Digite a nota 1")
nota1 = input("Digite a nota 1")
nota1 = input("Digite a nota 1")
media = (nota1+nota2+nota3)/3

if media < 4:
    print("Você está reprovado")
elif media < 6:
    print("Recuperacão")
else:
    print("Você está aprovado")
