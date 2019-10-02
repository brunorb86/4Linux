import pymysql.cursors

try:
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='4linux',
        db='4linux',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

# Errors
except Exception as err:
    print("Erro ao tentar conectar com o MySQL")
    print(err)
    
else:
    with conexao.cursor() as cursor:
        dic = { "nome_pessoa":"",
                "nac_pessoa":"",
                "idade_pessoa":""
            }
        dic["nome_pessoa"] = input ("Digite o nome: ")
        dic["nac_pessoa"] = input ("Digite a nacionalidade: ")
        dic["idade_pessoa"] = input ("Digite a idade: ")
        SQL = "INSERT INTO pessoa(nome_pessoa, nac_pessoa, idade_pessoa) VALUES ('{}', '{}', {})".format(dic["nome_pessoa"],dic["nac_pessoa"],dic["idade_pessoa"])
        cursor.execute(SQL)
        conexao.commit()
finally:
    conexao.close()
