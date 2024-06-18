"""
interável -> str , range , etc
interador -> quem sabe entregar um valor por vez 
next -> me entregue o próximo valor 
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'malieni'#iterável
iteratador = iter(texto)#iterator
""" 
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except  StopIteration:
        break """

for letra in texto:
    print(letra)