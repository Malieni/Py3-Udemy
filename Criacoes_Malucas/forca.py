import random

#lista de palavras para descobrir
lista_palavras = ["banana" , "morango" , "melancia" , "pitaia"]

#escolha uma palavra aleatória da lista
palavra_a_acertar = random.choice(lista_palavras)

#Cria uma lista para guardar as letras 
tentativa_letra = ["_"] * len(palavra_a_acertar)

#inicia a contagem de vidas 
vidas = 6

print("Vamos jogar Forca!!!")
print(" ".join(tentativa_letra))

while vidas > 0:
#pergunta por uma letra ao usuário
    tentativa = input("Digite uma letra: ")
#Procura a letra na palavra
    if tentativa in palavra_a_acertar:
#Revela se a letra está correta
        for i in range(len(palavra_a_acertar)):
            if palavra_a_acertar[i] == tentativa:
                tentativa_letra[i] = tentativa
        print(" ".join(tentativa_letra))
    else:
#perde pontos de vida
        vidas -= 1
        print("Oops, incorrect! You have", vidas, "vidas left.")

#Conferir a vitória do usário
    if "_" not in tentativa_letra:
        print(" Congratulations, you won! The word was", palavra_a_acertar)
        break