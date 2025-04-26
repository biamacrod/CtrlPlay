#beecrowd 1049 "animal"
corpo = input()
classe = input()
alimentacao = input()

if corpo == "vertebrado" and classe == "mamifero" and alimentacao == "onivoro":
    print("homem")
elif corpo == "vertebrado" and classe == "mamifero" and alimentacao == "herbivoro":
    print("vaca")
elif corpo == "vertebrado" and classe == "ave" and alimentacao == "carnivoro":
    print("aguia")
elif corpo == "vertebrado" and classe == "ave" and alimentacao == "onivoro":
    print("pomba")
elif corpo == "invertebrado" and classe == "inseto" and alimentacao == "hematofago":
    print("pulga")
elif corpo == "invertebrado" and classe == "inseto" and alimentacao == "herbivoro":
    print("lagarta")
elif corpo == "invertebrado" and classe == "anelideo" and alimentacao == "hematofago":
    print("sanguessuga")
elif corpo == "invertebrado" and classe == "anelideo" and  alimentacao == "onivoro":
    print("minhoca")
else:
    print("not found")
