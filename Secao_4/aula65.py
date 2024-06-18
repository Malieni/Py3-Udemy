""" 
Introdução às funçoes (def) em Python
Funbções são trechos de código usados para
replicar determinada ação ao longfo do seu código.
Elas podem receber valores para parãmetros (argumentos)
e retornar um valor específico.
Por padrão , funcões Python retornam None (nada).
"""
""" def Print(a, b, c):
    print("Várias1")
    print("Várias2")
    print("Várias3")
    print("Várias4") """

""" def imprimir(a, b, c):
  print(a,b,c)

imprimir(1,2,3) """

def saudacao(nome='Sem nome'):
    print(f"Olá, {nome}!")

saudacao('Guilherme')
saudacao('Malieni')
saudacao('Henrique')
saudacao()