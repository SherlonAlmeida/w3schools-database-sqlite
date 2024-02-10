def menu_opcoes():
    print("""
-------------------------------------------------
1) Selecionar Clientes e seus Pedidos.
2) Exibir produtos e suas categorias.
3) Apresentar dados das tabelas.
0) Sair
-------------------------------------------------""")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def listar_tabelas(conexao):
    cursor = conexao.cursor()
    tabelas = ["categories", "customers", "employees", "orders",
                   "order_details", "products", "shippers", "suppliers"]
    print("Tabelas Disponíveis:", end=" ")
    for t in tabelas:
        print(t, end=" | ")
    print("\n-------------------------------------------------")

    tabela = input("Digite a tabela desejada: ")
    while tabela not in tabelas:
        tabela = input("Digite a tabela desejada: ")

    comando_sql = cursor.execute(f"""SELECT * FROM {tabela};""")
    data = cursor.fetchall()
    for cliente in data:
        print(cliente)

def apresentar_clientes_e_pedidos(conexao):
    cursor = conexao.cursor()
    #Define o comando SQL para realizar a filtragem dos dados 
    comando_sql = f"""
        SELECT  Orders.OrderID,
                Orders.CustomerID,
                Customers.CustomerID,
                Customers.CustomerName,
                Customers.ContactName,
                OrderDetails.OrderID,
                OrderDetails.ProductID,
                Products.ProductID,
                Products.ProductName
        FROM (((Orders
        INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
        INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID)
        INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID)
    """
    
    #Verificando se o usuario deseja filtrar por nome de clientes
    opcao = int(input("Deseja filtrar por cliente? 1) Sim, 2) Não: "))
    if opcao == 1:
        substring = input("Digite o nome do cliente a ser pesquisado: ")
        comando_sql += f'''\nWHERE Customers.CustomerName LIKE "{substring}"'''

    #Executa o comando SQL e obtem os dados a serem apresentados
    cursor.execute(comando_sql)
    dados = cursor.fetchall()
    for dado in dados:
        cliente = dado[3]
        contato_cliente = dado[4]
        produto_adquirido = dado[8]
        print(f"O cliente '{cliente}' comprou o produto '{produto_adquirido}'.")

def apresentar_produto_e_categorias(conexao):
    cursor = conexao.cursor()
    #Define o comando SQL para realizar a filtragem dos dados 
    comando_sql = f"""
        SELECT Products.ProductID,
            Products.ProductName,
            Products.CategoryID,
            Categories.CategoryID,
            Categories.CategoryName
        FROM Products
        INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID
    """
    
    #Verificando se o usuario deseja filtrar por nome de clientes
    opcao = int(input("Deseja filtrar por categoria? 1) Sim, 2) Não: "))
    if opcao == 1:
        substring = input("Digite a categoria a ser pesquisada: ")
        comando_sql += f'''\nWHERE Categories.CategoryName LIKE "{substring}"'''

    #Executa o comando SQL e obtem os dados a serem apresentados
    cursor.execute(comando_sql)
    dados = cursor.fetchall()
    for dado in dados:
        produto = dado[1]
        categoria = dado[4]
        print(f"O produto '{produto}' pertence à categoria '{categoria}'.")