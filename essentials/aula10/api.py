import requests , json

with open("CEP.txt") as l_cep:
    ceps = l_cep.readlines()

print (ceps)

for item in ceps:
    
    destino = "https://viacep.com.br/ws/" + item[0:8] + "/json/"
    resposta = requests.get(destino)

    if resposta.status_code == 200:
        json = resposta.json()
    
        print(json['cep'])
        print(json['logradouro'])
        print(json['complemento'])
        print(json['bairro'])
        print(json['localidade'])
        print(json['uf'])
        print(json['ibge'])
        print(json['gia'])

    else:
        print("Unknown error - IDK what to do!! Leave me alone!!")

'''
#cep = input("Digite o CEP: ")
destino = "https://viacep.com.br/ws/" + ceps + "/json/"
resposta = requests.get(destino)


if resposta.status_code == 200:
    json = resposta.json()

    for item in json.values():
        print(item)
else:
    print("Unknown error - IDK what to do!! Leave me alone!!")

#Imprimir como json
#print(json)

print(json['cep'])
print(json['logradouro'])
print(json['complemento'])
print(json['bairro'])
print(json['localidade'])
print(json['uf'])
print(json['ibge'])
print(json['gia'])
'''
