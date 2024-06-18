import random

while True:
    entrada_usuario = input('Você quer gerar números da loteria? [s]im ou [n]ão: ')
    if entrada_usuario ==  's':
        print('Você escolheu gerar números da loteria! Boa sorte!')
        for _ in range (5):
            numeros_aleatorios = random.sample(range(1, 26), 15)
            numeros_aleatorios.sort()
            print("-".join(map(str, numeros_aleatorios)))
    elif entrada_usuario == 'n':
        print('Você escolheu não gerar números da loteria. Tudo bem!')
        break
    else:
        print('Você digitou uma opção inválida. Tente novamente!')

    