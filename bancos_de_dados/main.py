# import sqlite3
# conexao = sqlite3.connect("db.sqlite3")
# cursor = conexao.cursor()
# insert = '''INSERT INTO cadastro (infrator, cpf, nome_pai, nome_mae)
# VALUES("Mariano Silva",74125863451, "Cristiano Silva", "Bruna Silva" ); '''
# cursor.execute(insert)
# conexao.commit()


# import sqlite3
# conexao = sqlite3.connect("db.sqliteData")
# cursor = conexao.cursor()

# def cadastro_infrator(cursor):
#     infrator = input("Nome do infrator: ")
#     cpf = input("CPF do infrator: ")
#     nome_pai = input("pai do infrator: ")
#     nome_mae = input('mãe do infrator: ')
#     conexao = sqlite3.connect('db.sqliteData')
#     cursor = conexao.cursor()
#     insert = '''INSERT INTO cadastro(infrator,cpf,nome_pai, nome_mae)
#     VALUES(?,?,?,?); '''
#     valores =[infrator,cpf, nome_pai, nome_mae]
#     cursor.execute(insert,valores)
#     conexao.commit()
#     conexao.close()

# cadastro_infrator(cursor)


import sqlite3
conexao = sqlite3.connect("db.sqlite3")
cursor = conexao.cursor()
insert = '''INSERT INTO cadastro (infrator) VALUES("Mariano Silva" ); '''
cursor.execute(insert)
conexao.commit()
conexao.close()