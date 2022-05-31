
import random


words = ['Banana', 'Bicicleta', 'Amor', 'Tiroteio']


def word_game():
    random_word = random.choice(words)
    scrambled_word = "".join(random.sample(random_word, len(random_word)))
    tentativas = 1
    while tentativas < 4:
        print("Qual palavra e essa? ")
        print(scrambled_word)

        resposta = input("Digite sua resposta: ")
        if (resposta != random_word):
            tentativas += 1
        else:
            print("Acertou")
            tentativas = 5


word_game()
