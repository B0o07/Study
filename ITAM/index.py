import sqlite3

conexao =sqlite3.connect('itam.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS estoque (
        Periférico TEXT,
        Modelo TEXT,
        Quantidade INTEGER
    )
''')
conexao.commit()

while True:
    print("\n--- SISTEMA DE ESTOQUE ITAM ---")
    print("1. Cadastrar Novo Periférico")
    print("2. Listar Estoque")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input('Digite o nome do periférico: ')
        modelo = input('Digite o modelo do periférico: ')
        quantidade = int(input('Digite a quantidade do periférico: '))

        cursor.execute('''INSERT INTO estoque (Periférico, Modelo, Quantidade) VALUES (?, ?, ?)''', (nome, modelo, quantidade))
        conexao.commit()
        print("Periférico cadastrado com sucesso!")

    elif opcao == '2':
        cursor.execute('SELECT * FROM estoque')
        dados = cursor.fetchall()
        print("\n--- ESTOQUE ATUAL ---")
        for periferico, modelo, quantidade in dados:
            print(f'Periférico: {periferico}, Modelo: {modelo}, Quantidade: {quantidade}')
    
    elif opcao == '3':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

cursor.close()
conexao.close()
