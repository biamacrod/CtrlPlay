class animal:
    def identificar(self, vertebra, classe, alimentacao):
        raise NotImplementedError("este metodo deve ser implemetado")
    
class vertebrados(animal):
    mapa = {
        ("ave", "carnivoro"): "aguia", 
        ("ave", "onivoro"): "pomba",
        ("mamifero", "herbivoro"): "vaca",
        ("mamifero", "onivoro"): "homem"
    }
    def identificar(self, vertebra, classe, alimentacao):
        return self.mapa.get((classe, alimentacao))
    
class invertebrados(animal):
    mapa = {
        ("inseto", "hematofago"): "pulga", 
        ("inseto", "herbivoro"): "lagarta",
        ("anelideo", "hematofago"): "sanguessuga",
        ("anelideo", "onivoro"): "minhoca"
    }
    def identificar(self, vertebra, classe, alimentacao):
        return self.mapa.get((classe, alimentacao))
    
vertebra = input()
classe = input()
alimentacao = input()

if vertebra == "vertebrado":
    animal = vertebrados()
elif vertebra == "invertebrado":
    animal = invertebrados()

print(animal.identificar(vertebra, classe, alimentacao))