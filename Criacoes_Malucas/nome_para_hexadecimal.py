# Convertor de nome para Hexadecimal 
def nome_para_hex(nome):
    return ''.join(format(ord(c),'02X') for c in nome)

nome = input ('Digite um nome : ')

nome_hex = nome_para_hex(nome)

print(f'O Nome {nome} em hexadecimal é: {nome_hex}')


