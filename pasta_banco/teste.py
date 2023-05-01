import sqlite3

conexao = sqlite3.connect('db.data')
cursor = conexao.cursor()

sql = '''CREATE TABLE tabela_01(id INTERGE PRIMERI KEY NOT NULL , 
produto, valor, preço)'''


# sql = '''INSERT INTO tabela (produto, valor, preço)
#  VALUES("Bola", "Moeda Brasileira", "Quarenta reis" )'''
cursor.execute(sql)
conexao.commit()
conexao.close()
print("TABELA CRIADA COM SUCESSO.")