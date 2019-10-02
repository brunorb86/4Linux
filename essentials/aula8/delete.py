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
    print("Erro ao deletar!")
    print(err)
    
else:
    with conexao.cursor() as cursor:
        id_pessoa = input("Inform o ID: ")
        
        SQL = "DELETE FROM pessoa WHERE id_pessoa = {}".format(id_pessoa)
        
        cursor.execute(SQL)
        conexao.commit()
finally:
    conexao.close()
