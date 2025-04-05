class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 100
    def dormir(self, horas):
        energiaGanha = horas * 10
        self.energia = self.energia + energiaGanha
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nome} dormiu por {horas} e ganhou {energiaGanha} de energia. Energia atual: {self.energia}")
    def brincar(self, tempo):
        energiaGasta = tempo * 5
        if energiaGasta <= self.energia:
            self.energia = self.energia - energiaGasta
            print(f"{self.nome} brincou por {tempo} e perdeu {energiaGasta} de energia. Energia atual: {self.energia}")
        else:
            print(f"{self.nome} está cansado demais para brincar!")
    def InfoAnimal(self):
        return f"Informações: {self.nome}, {self.idade} anos, {self.energia} energia"
        
Animal1 = Animal(nome = "belly", idade = "15")
print(Animal1.brincar(40))
print(Animal1.dormir(1))
print(Animal1.InfoAnimal())