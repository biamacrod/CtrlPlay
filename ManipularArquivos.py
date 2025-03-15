arquivo= "MeuArquivo.txt"

try: 
    open("MeuArquivo.txt", "r")
except FileNotFoundError: 
    open("MeuArquivo.txt", "w")

# with open(arquivo, "w") as arq:
#     arq.write("primeira linha")
# with open(arquivo, "a") as arq:
#     arq.write("linha adicionada no final")

nome = "Bia"
idade = 15

with open(arquivo, "w") as arq:
    arq.write(f"nome: {nome}\n")
    arq.write(f"idade: {idade}\n")
#sem f acha que e tudo texto, com f entre {} é variável

arquivo2 = "ListaDeCompras.py"

open(arquivo2, "r")

# arquivo3 = input("Nome do seu arquivo: ")

# open(arquivo3, "w")