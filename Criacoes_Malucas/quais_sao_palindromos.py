#verificador de palindromos
user_input = input("Digite sua palavra ou frase: ")


if user_input:
    
    user_input = user_input.replace(" ", "").lower()

    
    if user_input == user_input[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
else:
    print("Você não digitou nada!")

