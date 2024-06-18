"""
Formatação básica de strings
s -string
d - int 
f - float 
.<número de dígitos>f
x ou X - Hexadecimal 
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro 
= -Força o número a aparecer antes dos zeros
Sinal + ou - 
Ex.:0>-100,.1f
Conversion flags - !r !s !a
respectivamente - __repr__ __str__ __asp__ 
"""
variavel = 'ABC'
print(f'{variavel}' * 10 )
print(f'{variavel: >10} ')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:-^10}.')
print(f'{1000.4545487778412:0=+10,.1f}')
print(f'O Hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')