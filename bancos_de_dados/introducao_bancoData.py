import sqlite3

# CRIANDO UMA TABELA
# conexao = sqlite3.connect('db.sqlite3')
# cursor = conexao.cursor()
# # o "id INTEGER PRIMERY KEY" - INDENTIFICADOR ÚNICO  PARA CADA LINHA 
# tabela = '''CREATE TABLE mercado( id INTEGER PRIMERY KEY, produto TEXT,
#  preco INTERGE, quantidade INTEGER )''' 
# inserir = 'INSERT INTO mercado VALUES( 1, melancia, 10)'
# cursor.execute(tabela)
# conexao.commit()
# conexao.close()






#INSERINDO DADOS NA TABELA

id = input('Insira o id: ')
categoria = input('Insira a categoria: ')

conexao = sqlite3.connect('db.sqlite3')
sql ='''
INSERT INTO categoria1 ( id, categoria)
VALUES(?,?); 
 '''
valores = [id, categoria]
cursor = conexao.cursor()
cursor.execute(sql,valores)
conexao.commit()
conexao.close()
print('DADOS INSERIDOS COM SUCESSO!')




conexao = sqlite3.connect('db.sqlite3')
sql ='''
SELECT * FROM categoria1 WHERE id > 3 OR categoria = 'PRODUTOS DE HIGIENE'; 
 '''
cursor = conexao.cursor()
resultados = cursor.execute(sql)
for resultado in resultados:
    print(resultado)
print('CONSULTA REALIZADA')    
conexao.commit()
conexao.close()