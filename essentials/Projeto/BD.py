from BancoDados import BancoDeDados

# criei um objeto
bd = BancoDeDados()

#Iniciar conexao com o banco
bd.iniciaConexao()
'''
try:
    bd.iniciaConexao()
    
except Exception as err:
    print(err)
else:
    print("Estou no banco!")
finally:
'''
# chama o metodo de insercao
# Insere dados no banco
bd.insereRegistro()

## Atualiza registro
#bd.atualizaRegistro()

## Deleta registro
#bd.removeRegistro()

## Consulta registro
bd.consultaRegistro()
# encerra a conexao com o banco de dados
bd.conexao.close()
