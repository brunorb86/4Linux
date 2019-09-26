# Importar o módulo pymysql
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
    print("Nao possivel conectar com o Banco de dados")
    print(err)
    
else:
    with conexao.cursor() as cursor:
        SQL = "SELECT * FROM pessoa;"
        cursor.execute(SQL)
        for linha in cursor:
#            print(linha)
            print("----------------------------------------")
            print("ID:",linha["id_pessoa"])
            print("Nome:",linha["nome_pessoa"])
            print("Nacionalidade:",linha["nac_pessoa"])
            print("Idade:",linha["idade_pessoa"])

finally:
    conexao.close()
