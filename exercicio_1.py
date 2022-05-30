
def verticalName():
    nome = input("Digite seu nome: ")
    quantidade_letras = len(nome)

    for numero in range(quantidade_letras, 0, -1):
        word = ''
        for index in range(numero):
            word += nome[index]

        print(word)


verticalName()
