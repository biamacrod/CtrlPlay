import Geometria as g

def menu():
    print("CALCULADORA GEOMÉTRICA")
    print("1 - Área do Círculo")
    print("2 - Perímetro do Círculo")
    print("3 - Área do Retângulo")
    print("4 - Perímetro do Retãngulo")
    print("5 - Área do Triângulo")
    print("6 - Perímetro do Triângulo")
    print("7 - Volume do Cilindro")
    print("8 - Volume do Paralelepípedo")
    print("9 - Volume da Pirâmide")
    print("0 - Sair")

while True: 
    menu()
    opcao = int(input("DIGITE A OPÇÃO DESEJADA: ")) 
    if opcao == 1:
        raio = float(input("Raio: "))
        print(f"Área: {g.areaCirculo(raio)}")
    
    elif opcao == 2:
        raio = float(input("Raio: "))
        print(f"Perímetro: {g.perimetroCirculo(raio)}")
    
    elif opcao == 3:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área: {g.areaRetangulo(base, altura)}")
    
    elif opcao == 4:
        base = float(input("Base: "))
        altura = float(input("Altura: ")) 
        print(f"Perímetro: {g.perimetroRetangulo(base, altura)}")
    
    elif opcao == 5:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área: {g.areaTriangulo(base, altura)}")
    
    elif opcao == 6:
        lado1 = float(input("Primeiro lado: "))
        lado2 = float(input("Segundo lado: "))
        lado3 = float(input("Terceiro lado: "))
        print(f"Perímetro: {g.perimetroTriangulo(lado1, lado2, lado3)}")
    
    elif opcao == 7:
        raio = float(input("Raio: "))
        altura = float(input("Altura: "))
        print(f"Volume: {g.volumeCilindro(raio, altura)}")

    elif opcao == 8:
        largura = float(input("Largura: ")) 
        altura = float(input("Altura: "))
        profundidade = float(input("Profundidade: "))
        print(f"Volume: {g.volumeParalelepipedo(largura, altura, profundidade)}")

    elif opcao == 9:
        ladoBase1 = float(input("Lado da Base: "))
        ladoBase2 = float(input("Outro lado da Base: "))
        altura = float(input("Altura: "))
        print(f"Volume: {g.volumePiramide(ladoBase1, ladoBase2, altura)}")

    elif opcao == 0:
        print("Encerrado")
        break

    else:
        print("OPERAÇÃO NÃO ENCONTRADA")

