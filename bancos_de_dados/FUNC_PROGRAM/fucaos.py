


def cadastro_infrator(cursor):
    infrator = input("Nome do infrator: ")
    cpf = input("CPF do infrator: ")
    nome_pai = input("pai do infrator: ")
    nome_mae = input('mãe do infrator: ')
    insert = '''INSERT INTO cadastro(infrator,cpf,nome_pai, nome_mae)
    VALUES(?,?,?,?); '''
    valores =[infrator,cpf, nome_pai, nome_mae]
    cursor.execute(insert,valores)
    conexao.commit()
    conexao.close()