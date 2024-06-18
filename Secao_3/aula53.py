"""
enumere - enumere interáveis (indices)
"""
""" [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')] """
lista = ['Mari' , 'Maranhão' , 'Rato']
lista.append('Sofia')

for indice , nome in enumerate(lista):
    print(f'Indice: {indice} - Nome: {nome}')



#for item in enumerate(lista):
#  indice , nome = item
#  print(f'Indice: {indice} - Nome: {nome}')


#for tupla_ennumerada in enumerate(lista):
#    print('FOR da tupla: ')
#    for valor in tupla_ennumerada:
#        print(f'Valor: {valor}')