import pymysql.cursors
# Database projetofuncionarios
# Table funcionarios_dados
class BancoDeDados:
    def __init__(self):
        self.host='localhost'
        self.usuario='root'
        self.senha='4linux'
        self.banco='projetofuncionarios'
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
        dic = { "id_func":"",
                "nome_func":"",
                "cpf_func":"",
                "idade_func":""
        }
    
        dic["id_func"] = input ("Digite o ID: ")   
        dic["nome_func"] = input ("Digite o nome: ")
        dic["cpf_func"] = input ("Digite o CPF: ")
        dic["idade_func"] = input ("Digite a idade: ")
        
        with self.conexao.cursor() as cursor:
            SQL = "INSERT INTO funcionarios_dados(id_func, nome_func, cpf_func, idade_func) VALUES ('{}', '{}', '{}', {})".format(dic["id_func"],dic["nome_func"],dic["cpf_func"],dic["idade_func"])
            cursor.execute(SQL)
            self.conexao.commit()
            
    def consultaRegistro(self):
        nome_func = input("Digite o nome para consulta: ")
        with self.conexao.cursor() as cursor:
            SQL = "SELECT * FROM funcionarios_dados WHERE nome_func like '%{}%'".format(nome_func)
            cursor.execute(SQL)
            for linha in cursor:
    #            print(linha)
                print("----------------------------------------")
                print("ID:",linha["id_func"])
                print("Nome:",linha["nome_func"])
                print("CPF:",linha["cpf_func"])
                print("Idade:",linha["idade_func"])

    def removeRegistro(self):
        exclui_func = input("Digite o nome para consulta: ")
        with self.conexao.cursor() as cursor:
            SQL = "DELETE FROM funcionarios_dados WHERE nome_func like '%{}%'".format(exclui_func)
            cursor.execute(SQL)
            self.conexao.commit()
