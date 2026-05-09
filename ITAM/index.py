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

nome = input('Digite o nome do periférico: ')
modelo = input('Digite o modelo do periférico: ')
quantidade = int(input('Digite a quantidade do periférico: '))

cursor.execute('''INSERT INTO estoque (Periférico, Modelo, Quantidade) VALUES (?, ?, ?)''', (nome, modelo, quantidade))
conexao.commit()

cursor.execute('SELECT * FROM estoque')
dados = cursor.fetchall()

for periferico, modelo, quantidade in dados:
    print(f'Periférico: {periferico}, Modelo: {modelo}, Quantidade: {quantidade}')

cursor.close()

conexao.close()
