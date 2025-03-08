arquivo = "ListaDeCompras.txt"

#def = criar fubnção -> pode ser reutilizada
def adicionarItem():
    item = input("Digite o item a ser adicionado: ")
    with open(arquivo, "a") as arq:
        arq.write(item + "\n")
    print(f"{item} adicionado à lista!")

#parentesis e pra definir que e uma lista e adicionar tipagem
def vizualizarLista():
    try:
        with open(arquivo, "r") as arq:
            if not item:
                print("Lista está vazia!")
            else: 
                print("Sua lista de compras: ")
                for i, item in enumerate(item, start =1):
                    #i = indicar uma contagem
                    print(i, item.strip())
    except FileNotFoundError:
        print("A lista não existe")

def removerItem():
    vizualizarLista()
    try:
        num = int(input("digite o numero do item para remover: ")) -1
        with open(arquivo, "r") as arq:
            itens = arq.readlines()
        if 0<num<len(itens): 
            itemRemovido = itens.pop(num)
            with open(arquivo, "w") as arq:
                arq.writelines(itens)
            print(f"{itemRemovido.strip} foi removido!")
        else:
            print("Item não existe!")
    except (ValueError, FileNotFoundError):
        print("Erro ao remover item do sistema!")

while True:
    print("Sua lista de compras 🛒:")
    print("1 - adicionar item ➕")
    print("2 - vizualizar lista 👀")
    print("3 - remover item ⛔")
    print("4 - sair 🔒")
    opcao = int(input("digite uma opção: "))
# == é comparação
    if opcao == 1:
        adicionarItem
    elif opcao == 2:
        vizualizarLista
    elif opcao == 3:
        removerItem
    elif opcao == 4:
        print("Saindooooooo... ")
        break
    else:
        print("Opção inválida ❌")