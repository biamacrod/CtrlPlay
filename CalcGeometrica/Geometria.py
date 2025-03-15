import math

def areaCirculo (raio):
    return math.pi * raio**2

def perimetroCirculo (raio):
    return math.pi * raio * 2

def areaRetangulo (base, altura):
    return base * altura

def perimetroRetangulo (base, altura):
    return 2 * (base + altura)

def areaTriangulo (base, altura):
    return (base * altura) / 2

def perimetroTriangulo (lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def volumeCilindro (raio, altura):
    return raio**2 * math.pi * altura

def volumeParalelepipedo (largura, altura, profundidade):
    return largura * altura * profundidade

def volumePiramide (ladoBase1, ladoBase2, altura):
    return ((ladoBase1 * ladoBase2) * altura) / 3