x = 10
while x < 10:
    print ("Numero: {} rodando".format(x))
    x =+1
print("O while acabou!!")

exit()
nota1 = float(input("Digite primeira nota: "))
nota2 = float(input("Digite segunda nota: "))
nota3 = float(input("Digite terceira nota: "))
media = (nota1+nota2+nota3)/3
print (media)
#if nota1+nota2+nota3 > 6:
if media >= 6:
    print ("Você está aprovado")
if media == 4 or 5:
    print ("Voce está de recuperaçâo")
if media < 4:
    print ("Voce está reprovado")
#else:     
#    print ("Você está reprovado!")        

exit()

nome = (input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
CNH = (input("Você tem CNH?: "))
if idade >= 18 and CNH == 'sim' or 'Sim' or 'SIM':
#    if CNH == 'sim':
#        print ("Pode dirigir")
#    else:
    print ("Você pode dirigir, vá em frente.")
else:
    print ("Você não pode dirigir, pegue um ônibus!!")        

exit()


idade = int(input("Digite idade: "))
CNH = (input("Tem CNH?: "))
if idade > 18:
    if CNH == 'sim':
        print ("Pode dirigir")
    else:
        print ("Não pode dirigir")
else:
    print ("Não pode dirigir, pegue um ônibus!!")        

exit()
num2 = 30
if num1 > num2:
    print ("Num1 é maior que o Num2")
else:    
    print ("Num2 é maior que o Num1")
exit()


num1 = 10
num2 = 30
if num1 > num2:
    print ("Num1 é maior que o Num2")
else:    
    print ("Num2 é maior que o Num1")
exit()

num1 = 10
num2 = 30
print (num1 > num2)
exit()

num1 = 10
num2 = 30
print (num1 < num2)
exit()

num1 = 30
num2 = 30
print (num1 == num2)
exit()

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
soma = num1+num2
print(soma)
