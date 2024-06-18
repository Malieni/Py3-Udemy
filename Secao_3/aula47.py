"""
Faça um jogo para o usuário adivinhar qual 
qual a palavra secreta.
-Você vai propor uma palavra secreta 
qualquer e vai dar a possibilidade para o usuário
digitar digitar apenas uma letra , você vai conferir
se a letra digitada está na palavra secreta.
    -Se a letra digitada estiver na palavra secreta; exiba a letra;
    -Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do usuário.
"""

palavra = 'banana'
palavra_secreta = ['*'] * len(palavra)
tentativas = 0

while True:
    tentativa = input('Digite uma letra da palavra secreta: ')
    tentativas += 1
    if len(tentativa) > 1:
        print('Digite apenas uma letra')
        continue
    for i in range(len(palavra)):
        if palavra[i] == tentativa:
            palavra_secreta[i] = tentativa
    print(' '.join(palavra_secreta))
    if '*' not in palavra_secreta:
      print(f'Parabéns a você conseguiu descobrir a palavra secreta "{palavra}" em {tentativas} tentativas.')
      break