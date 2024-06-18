"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar . Caso o usuário não digite um número 
inteiro , informe que não é um número inteiro.
"""

try:
    numero_inteiro = int(input('Digite um número: '))
    if numero_inteiro % 2 == 0:
        print(f'O número {numero_inteiro} é par')
    else:
        print(f'O número {numero_inteiro} é ímpar')
except ValueError:
    print('Você não digitou um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e , baseando-se no horário
descrito , exiba a saudação apropriada. Ex.
Bom dia 0-11 , Boa Tarde 12-17 e Boa noite 18-23.
"""

hora = int(input('Digite a hora do dia (0-23): '))
if hora < 0 or hora > 23:
    print('Hora inválida!')
elif hora <= 11:
    print('Bom dia!')
elif hora <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')

"""
Faça um programa que peça o primeiro nome do usuário . Se o nome tiver 4 letras ou 
menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras , escreva 
"Seu nome é normal" ; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = str(input('Digite o seu nome: '))
if len(nome) <= 4:
    print("Seu nome é curto")
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")