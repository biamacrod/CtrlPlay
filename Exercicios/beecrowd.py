#1002
#num = float(input())

#areaCirculo = 3.14159 * num**2
#print("A=%.4f" %areaCirculo)

#1004
# salario = float(input())

# if (salario <= 400.00 and salario >= 0):
#     novoSalario = salario * 1.15
#     reajuste = novoSalario - salario
#     percentual = 15
# elif (salario >= 400.01 and salario <= 800.00):
#     novoSalario = salario * 1.12
#     reajuste = novoSalario - salario
#     percentual = 12
# elif (salario >= 800.01 and salario <= 1200.00):
#     novoSalario = salario * 1.10
#     reajuste = novoSalario - salario
#     percentual = 10
# elif (salario >= 1200.01 and salario <= 2000.00):
#     novoSalario = salario * 1.07
#     reajuste = novoSalario - salario
#     percentual = 7
# elif (salario > 2000.00):
#     novoSalario = salario * 1.04
#     reajuste = novoSalario - salario
#     percentual = 4

# print("Novo salario: %.2f" %novoSalario)
# print("Reajuste ganho: %.2f" %reajuste)
# print("Em percentual:",percentual,"%")

#1151
# primeiroNum = 0
# segundoNum = 1
# sequenciaFibo = [primeiroNum, segundoNum]

# for i in range(2, 46): 
#     proxNum = primeiroNum + segundoNum
#     primeiroNum = segundoNum
#     segundoNum = proxNum
#     sequenciaFibo.append(proxNum)

# termo = int(input())

# for i in range(termo):
#     print(sequenciaFibo[i])

#1018
# num = int(input())

# print(num)
# # // = divisao inteira (resultado inteiro)
# print(num//100,"nota(s) de R$100,00")
# num = num % 100
# print(num//50,"nota(s) de R$50,00")
# num = num % 50
# print(num//20,"nota(s) de R$20,00")
# num = num % 20
# print(num//10,"nota(s) de R$10,00")
# num = num % 10
# print(num//5,"nota(s) de R$5,00")
# num = num % 5
# print(num//2,"nota(s) de R$2,00")
# num = num % 2
# print(num,"nota(s) de R$1,00")

#1045
A, B, C = list(map(float, input().split()))
#map = mistura as duas funcoes
if (A<B):
    temp = A
    A = B
    B = temp
if (B < C):
    temp = B
    B = C
    C = temp
if (A < C):
    temp = A
    A = C
    C = temp
if (A>=(B+C)):
    print("NAO FORMA TRIANGULO")
if (A*A == (B*B + C*C)):
    print("TRIANGULO RETANGULO")
if (A*A > (B*B + C*C)):
    print("TRIANGULO OBTUSANGULO")
if (A*A < (B*B + C*C)):
    print("TRIANGULO ACUTANGULO")
if (A == B == C):
    print("TRIANGULO EQUILATERO")
if (A == B or B == C or C == A):
    print("TRIANGULO ISOCELES")