"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim 
"""
condicao = True

while condicao:
    digitou = input('O que você vai digitar: ')
    print(f'Você digitou {digitou}')

    if digitou == 'sair':
        break

print("acabou")
