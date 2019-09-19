dic = {1:8.50, 2:3.25, 2:4.60}

lista = []

print ("Escolha o seu produto: ")
print (" 1 - Banana\n 2 - Pera\n 3- Melancia")

lista.append(1)
lista.append(2)
lista.append(3)

for elemento in lista:
    total =+ dic[elemento]

print (dic[1])

exit()
#!/usr/bin/python3
print("Calculator")

#def escolhe_op():
#    escolha = int(input("1 soma \n 2 sub \n 3 mult \n 4 div \n:"))
#    while escolha < 1 or escolha > 5:
#        print ("Opção invalida!!")
#        escolha = int(input("1 soma \n 2 sub \n 3 mult \n 4 div \n:"))
#    return escolha
    
def soma(a,b):
    print(a+b)
    
def sub(a,b):
    print(a-b)

def mult(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

dic = {1:soma, 2:sub, 3:mult, 4:div}
#print("1 soma \n 2 sub \n 3 mult \n 4 div")

escolha = int(input("1 soma \n 2 sub \n 3 mult \n 4 div \n:"))
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))

#print(escolha)
#print("Escolha uma opção: ")
#escolha = escolhe_op()

dic[escolha](num1,num2)

#print("1 soma \n 2 sub \n 3 mult \n 4 div")

#if escolha == 1:
#    print(num1+num2)

#elif escolha == 2:
#    print(num1-num2)
    
#elif escolha == 3:
#    print(num1*num2)
    
#elif escolha == 4:
#    print(num1/num2)

exit()
def soma (a,b):
    print(a+b)
    
def sub (a,b):
    print(a-b)
    
num1=10
num2=5
num3=7
num4=2

soma(num1,num2)

exit()
dicionario = {"Nome":"Bruno","Idade" :33}
#print(dicionario["Nome","Idade"])
print(dicionario)

exit()
musica = """
A long long time ago
I can still remember how
That music used to make me smile
And I knew if I had my chance
That I could make those people dance
And maybe they'd be happy for a while
But February made me shiver
With every paper I'd deliver
Bad news on the doorstep
I couldn't take one more step
I can't remember if I cried
When I read about his widowed bride
Something touched me deep inside
The day the music died
So
Bye, bye Miss American Pie
Drove my Chevy to the levee but the levee was dry
And them good ole boys were drinking whiskey and rye
Singin' this'll be the day that I die
This'll be the day that I die
Did you write the book of love
And do you have faith in God above
If the Bible tells you so?
Do you believe in rock and roll?
Can music save your mortal soul?
And can you teach me how to dance real slow?
Well, I know that you're in love with him
'Cause I saw you dancin' in the gym
You both kicked off your shoes
Man, I dig those rhythm and blues
I was a lonely teenage broncin' buck
With a pink carnation and a pickup truck
But I knew I was out of luck
The day the music died
I started singin'
Bye, bye Miss American Pie
Drove my Chevy to the levee but the levee was dry
And them good ole boys were drinking whiskey and rye
Singin' this'll be the day that I die
This'll be the day that I die
Now, for ten years we've been on our own
And moss grows fat on a rolling stone
But, that's not how it used to be
When the jester sang for the king and queen
In a coat he borrowed from James Dean
And a voice that came from you and me
Oh and while the king was looking down
The jester stole his thorny crown
The courtroom was adjourned
No verdict was returned
And while Lennon read a book on Marx
The quartet practiced in the park
And we sang dirges in the dark
The day the music died
We were singin'
Bye, bye Miss American Pie
Drove my Chevy to the levee but the levee was dry
Them good ole boys were drinking whiskey and rye
And singin' this'll be the day that I die
This'll be the day that I die
Helter skelter in a summer swelter
The birds flew off with a fallout shelter
Eight miles high and falling fast
It landed foul on the grass
The players tried for a forward pass
With the jester on the sidelines in a cast
Now the half-time air was sweet perfume
While sergeants played a marching tune
We all got up to dance
Oh, but we never got the chance
'Cause the players tried to take the field
The marching band refused to yield
Do you recall what was revealed
The day the music died?
We started singin'
Bye, bye Miss American Pie
Drove my Chevy to the levee but the levee was dry
Them good ole boys were drinking whiskey and rye
And singin' this'll be the day that I die
This'll be the day that I die
Oh, and there we were all in one place
A generation lost in space
With no time left to start again
So come on Jack be nimble, Jack be quick
Jack Flash sat on a candlestick
'Cause fire is the devil's only friend
Oh and as I watched him on the stage
My hands were clenched in fists of rage
No angel born in Hell
Could break that Satan's spell
And as the flames climbed high into the night
To light the sacrificial rite
I saw Satan laughing with delight
The day the music died
He was singin'
Bye, bye Miss American Pie
Drove my Chevy to the levee but the levee was dry
Them good ole boys were drinking whiskey and rye
Singin' this'll be the day that I die
This'll be the day that I die
I met a girl who sang the blues
And I asked her for some happy news
But she just smiled and turned away
I went down to the sacred store
Where I'd heard the music years before
But the man there said the music wouldn't play
And in the streets the children screamed
The lovers cried, and the poets dreamed
But not a word was spoken
The church bells all were broken
And the three men I admire most
The Father, Son, and the Holy Ghost
They caught the last train for the coast
The day the music died
And they were singing
Bye, bye Miss American Pie
Drove my Chevy to the levee but the levee was dry
And them good ole boys were drinking whiskey and rye
Singin' this'll be the day that I die
This'll be the day that I die
They were singing
Bye, bye Miss American Pie
Drove my Chevy to the levee but the levee was dry
Them good ole boys were drinking whiskey and rye
Singin' this'll be the day that I die
"""

conta_palavra=0
#musica = musica.lower()
#musica = musica.upper()
musica = musica.split()

for palavra in musica:
    if palavra == "bye":
        conta_palavra += 1
        
print (conta_palavra)

exit()
print(musica)
consoantes = "bcdfghklmnpqrstvxwyzBCDFGHKLMNPQRSTVXWYZ"
conta_consoante = 0

for caractere in musica:   
#    if caractere not in consoantes:
    if caractere in consoantes:
        conta_consoante +=1
print("O total de consoantes é {}".format (conta_consoante))

exit()
frutas = ["banana","pera","abacaxi"]
for elemento in frutas:
    print(elemento)

#for num in range(6) generators
#help range

exit()
var =0
while var <8:
#    if var % 2 == 0: #verifica se é par
    print(var)
    var += 1 ### var = var +1 ==var +=1

for num in range (3):
    print(num)
exit()

lista_names = ['Bruno', 'Isabela', 'Yahell']
print (lista_names)

#print ("##########")
#print ("# Aula 3 #")
#print ("##########")
#var = ' Bruno Bonfim '
#var.title ()
#' Bruno Bonfim '

exit()
