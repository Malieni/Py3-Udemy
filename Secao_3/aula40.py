"""Calculadora com while"""

""" 
while True:
    print("Selecione uma opção: ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = int(input('Opção: '))
   
    if opcao == 1:
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo Número:  '))
        print('Resultado: ' , num1 + num2)

    if opcao == 2:
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo Número:  '))
        print('Resultado: ' , num1 - num2)
    
    if opcao == 3:
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo Número:  '))
        print('Resultado: ' , num1 * num2)

    if opcao == 4:
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo Número:  '))
        print('Resultado: ' , num1 / num2)

    elif opcao == 5:
        print('Saindo...')
        break
    else:
        print('Opção inválida!')


 """


while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except:
        numeros_validos is None
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando conta confira o Resultado abaixo:')
    print('-' * 10)

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=' , num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=' , num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=' , num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=' , num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui...')


    print('Obrigado por utilizar a calculadora do Malieni :) ')
    print('-' * 10)
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break