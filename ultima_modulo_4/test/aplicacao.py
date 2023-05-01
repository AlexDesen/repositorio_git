class cadastro:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
            
    def imprime_email(self):
        email =  "{}.{}@emial.com".format(self.nome, self.sobrenome)
        print(email)
        



# resultado = cadastro("Armando","Gomes")
# resultado.imprime_email()


# *O reutrn precisa esta presente na função para que o teste faça a comparação.
def imprime_email(nome, sobrenome):
    return  "{}.{}@email.com.br".format(nome, sobrenome) 
      