from FUNC_PROGRAM.fucaos import cadastro_infrator
import sqlite3

conexao = sqlite3.connect('db.sqliteData')
cursor = conexao.cursor()

cadastro = cadastro_infrator(cursor)