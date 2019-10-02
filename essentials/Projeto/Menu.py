#!/usr/bin/python3.7

from BancoDados import BancoDeDados
#Google from consolemenu import *
#Google from consolemenu.items import *

# criei um objeto
bd = BancoDeDados()

#Iniciar conexao com o banco
bd.iniciaConexao()

while True:
    print ("#"*34)
    # Google menu = ConsoleMenu("Title", "Subtitle")
    print ("# Cadastro de novos Funcionários #")
    print ("#"*34)
    print ("# 1 - Inserir novo funcionário   #")
    print ("# 2 - Remover funcionário        #")
    print ("# 3 - Atualizar informação       #")
    print ("# 4 - Consultar funcionário      #")
    print ("# 5 - Sair                       #")
    print ("#"*34)
    opcao = int(input("Escolha uma opção: "))


    if opcao == 1:
        bd.insereRegistro()
    elif opcao == 2:
        bd.removeRegistro()
    elif opcao == 3:
        bd.atualizaRegistro()
    elif opcao ==4:
        bd.consultaRegistro()
    elif opcao == 5:
        print("Muito Obrigado!")
        break
