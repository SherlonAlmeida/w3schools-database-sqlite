import sqlite3
from funcionalidades import *

#Realizando a conexão com o Banco de Dados
conexao = sqlite3.connect("w3SchoolsDatabase.sqlite3")
cursor = conexao.cursor()
############################################################

while True:
    #Obtém a opção do usuário
    opcao = menu_opcoes()
    
    if opcao == 0:
        print("Programa finalizado!")
        break

    elif opcao == 1:
        apresentar_clientes_e_pedidos(conexao)

    elif opcao == 2:
        apresentar_produto_e_categorias(conexao)
    
    elif opcao == 3:
        listar_tabelas(conexao)
    
    else:
        print("Opção inválida!")

############################################################
#Finalizando a conexão com o Banco de Dados
conexao.commit()
cursor.close()