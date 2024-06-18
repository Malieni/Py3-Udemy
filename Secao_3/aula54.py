""" Exercício
Faça uma lista de comprar com listas
o usuário deve ter a possibilidade de inserir , apagar e listar valores da sua lista
não permita que o programa quebre com erros de índices inexistentes na lista.
"""
compra = []
while True:
    print("\n1 - Inserir item na lista de compra")
    print("2 - Apagar item da lista de compra")
    print("3 - Listar itens da lista de compra")
    print("4 - Sair do programa")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        item = input("Insira um item na lista de compra: ")
        compra.append(item)  
    elif opcao == '2':
        if len(compra) == 0:
            print("A lista de compra está vazia!")
        else:
            print("Itens da lista de compra:" , compra)
            item_apagar = input("Insira o item que deseja apagar: ")
            if item_apagar in compra:
                compra.remove(item_apagar)
            else:
                print("Item não encontrado na lista de compra!")    
    elif opcao == '3':
        for indice , nome in enumerate(compra ,start=1):
            print(f'Indice: {indice} - Nome: {nome}')
    elif opcao == '4':
        break
    else:
        print('Nunca deveria chegar aqui...')

print(compra)