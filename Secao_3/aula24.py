# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# G u i l h e r m e
# -6 -5 -4 -3 -2 -1
#nome = 'Guilherme'
##print(nome[2])
##print(nome[-2])
#print('e' in nome)
#print(10 * '-')
#print('a' in nome)
#print(10 * '-')
#print('Gui' in nome)
#print(10 * '-')
#print('gui' in nome)
#print(10 * '-')
#print('gui' not in nome)
#print(10 * '-')


nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')