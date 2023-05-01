import sqlite3

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = '''CREATE TABLE cliente (id TEXTO, nome TEXT(50), data_cadastro TEXT(250), endereço TEXT(50))'''
cursor.execute(sql)
conexao.commit()
conexao.close()



