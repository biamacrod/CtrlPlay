class Casa():
    def __init__(self, bairro, rua, numero, cep):
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.cep = cep

    def enderecoCompleto(self):
        return "Endereço Completo: " + self.rua + ", " + self.numero + ", " + self.bairro + ", CEP: " + self.cep
# Objeto -> "classe" em outra; precisa chamar classe para funcionar

casa1 = Casa(rua = "Rua Ceara", bairro = "Jardim dos Estados", cep = "32100000", numero = "1234")
# pra buscaar um atributo : usar .
casa2 = Casa( "Rua Jeribá", "Bairro Chacara Cachoeira", "1234567", "1000")
casa3 = Casa( "Rua Olario de Oliveira Franca", "Bairro Vila Nasser", "32489073", "5678")

rua = input("Rua: ")
bairro = input("Bairro: ")
numero = input("Número: ")
cep = input("CEP: ")
casa4 = Casa(bairro, rua, numero, cep)
print(casa4.enderecoCompleto())