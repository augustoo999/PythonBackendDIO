import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )


def inserir_cliente(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", data)
    conexao.commit()


def atualizar_cliente(conexao, cursor, id, nome, email):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data)
    conexao.commit()


def excluir_cliente(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?", data)
    conexao.commit()


def inserir_lote_clientes(conexao, cursor, lista_clientes):
    cursor.executemany(
        "INSERT INTO clientes (nome, email) VALUES (?, ?)", lista_clientes
    )
    conexao.commit()


def buscar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    return cursor.fetchone()


def buscar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome").fetchall()


buscar_clientes = buscar_clientes(cursor)
for cliente in buscar_clientes:
    print(dict(cliente))

cliente_encontrado = buscar_cliente(cursor, 1)
print(dict(cliente_encontrado))

# lista_clientes = [
#     ("Maria Oliveira", "maria.oliveira@gmail.com"),
#     ("Carlos Pereira", "carlos.pereira@gmail.com"),
#     ("Ana Souza", "ana.souza@gmail.com"),
# ]

# inserir_lote_clientes(conexao, cursor, lista_clientes)

# excluir_cliente(conexao, cursor, 3)
# excluir_cliente(conexao, cursor, 4)
# excluir_cliente(conexao, cursor, 5)

# inserir_cliente(conexao, cursor, "Victoria", "victoria@gmail.com")
