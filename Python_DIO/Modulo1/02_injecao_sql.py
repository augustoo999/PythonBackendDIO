import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

input_id = input("Digite o ID do cliente que deseja buscar: ")
cursor.execute(f"SELECT * FROM clientes WHERE id = {input_id}")
clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))
