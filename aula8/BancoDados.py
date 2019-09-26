import pymysql.cursors

class BancoDeDados:
    def __init__(self):
        self.host='localhost'
        self.usuario='root'
        self.senha='4linux'
        self.banco='4linux'
        self.charset='utf8mb4'
#        self.cursorclass=pymysql.cursors.DictCursor) - Parametro do cursor, pode ficar fora
        self.conexao = ''

    def iniciaConexao(self):
        try:
            self.conexao = pymysql.connect(
                host = self.host,
                user = self.usuario,
                password = self.senha,
                db = self.banco,
                charset = self.charset,
                cursorclass=pymysql.cursors.DictCursor)
        except Exception as err:
            print(err)
    
    def insereRegistro(self):
        dic = { "nome_pessoa":"",
                "nac_pessoa":"",
                "idade_pessoa":""
        }
    
        dic["nome_pessoa"] = input ("Digite o nome: ")
        dic["nac_pessoa"] = input ("Digite a nacionalidade: ")
        dic["idade_pessoa"] = input ("Digite a idade: ")
        
        with self.conexao.cursor() as cursor:
            SQL = "INSERT INTO pessoa(nome_pessoa, nac_pessoa, idade_pessoa) VALUES ('{}', '{}', {})".format(dic["nome_pessoa"],dic["nac_pessoa"],dic["idade_pessoa"])
            cursor.execute(SQL)
            self.conexao.commit()
            
    def consultaRegistro(self):
        with self.conexao.cursor() as cursor:
            SQL = "SELECT * FROM pessoa;"
            cursor.execute(SQL)
            for linha in cursor:
    #            print(linha)
                print("----------------------------------------")
                print("ID:",linha["id_pessoa"])
                print("Nome:",linha["nome_pessoa"])
                print("Nacionalidade:",linha["nac_pessoa"])
                print("Idade:",linha["idade_pessoa"])
                
    def atualizaRegistro(self):
        with self.conexao.cursor() as cursor:
            idade = input("Informe a Idade: ")
            id_pessoa = input("Inform o ID: ")
            SQL = "UPDATE pessoa SET idade_pessoa = {} WHERE id_pessoa = {}".format(idade, id_pessoa)
            cursor.execute(SQL)
            self.conexao.commit()
            
    def removeRegistro(self):
        with self.conexao.cursor() as cursor:
            id_pessoa = input("Inform o ID: ")
            SQL = "DELETE FROM pessoa WHERE id_pessoa = {}".format(id_pessoa)
            cursor.execute(SQL)
            self.conexao.commit()
