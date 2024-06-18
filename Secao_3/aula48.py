""" 
Listas em python 
tipo list - mutável
Suporta vários valores de qualquer tipo 
conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append , insert , pop , del , clear , extend , +
 """

#       +01234
#       -54321
string = 'ABCDE' #5 caracteres (len)
#print(bool([])) #falsy
#print(lista , type(lista))
#        0      1        2         3      4
#       -5     -4       -3        -2     -1
lista = [123 , True , 'Guilherme', 1.2 , []] # ''
lista[-3] = 'Malieni'
print(lista)
print(lista[2],type(lista[2]))

lista2 = [10,20,30,40]
#lista2[2] = 300
#del lista2[2]
#print(lista2)
#print(lista2[2])
lista2.append(50)
lista2.pop()
lista2.append(60)
lista2.append('70')
ultimo_valor = lista2.pop(3)
print(lista2, 'Removido', ultimo_valor)


lista3 = [10,20,30,40]
lista2.append('Guilherme')
nome = lista3.pop()
lista3.append(1223)
del lista3[-1]
#lista3.clear()
lista3.insert(100,5)
print(lista3[1])


""" append - adiciona item ao final
    insert - adiciona um item no indice escolhido
    pop - remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas 
Create Read Update Delete
Criar , ler , Alterar , apagar = lista [i] (CRUD)
"""



lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_d)



""" 
Cuidados com dados mutáveis 
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor (mutável) 
"""

lista_nomes = ['Luiz' , 'Marino' ,1 ,True , 1.2]
lista_nome = lista_nomes.copy()


lista_nomes[0] = 'qualquer coisa'
print(lista_nome)
print(lista_nomes)
