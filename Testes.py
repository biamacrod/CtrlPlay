# import unittest

# def SobrenomeNaOrdem(nome,sobrenome1, sobrenome2):
#     if(len(sobrenome2) >= len(sobrenome1)):
#         return nome + " " + sobrenome1 + " " + sobrenome2
#     else:
#         return nome + " " + sobrenome2 + " " + sobrenome1

# class NomeTeste(unittest.TestCase):
#     def test_SobrenomeNaOrdem(self):
#         nomeCompleto = SobrenomeNaOrdem("Joao Vitor", "Gomes", "Bitella")
#         self.assertEqual(nomeCompleto, "Joao Vitor Gomes Bitela")

# unittest.main(argv=[''], exit=False)

#print(SobrenomeNaOrdem("Gustavo", "Nowak", "da Silva"))
#print(SobrenomeNaOrdem("Raphael", "Alencar", "Araujo"))
#print(SobrenomeNaOrdem("Beatriz", "Machado", "Rodrigues"))

class Prova():
# init - inicializar (diferente de iniciar)
    def __init__(self):
        self.questoes = []
        self.respostas = []
    def mostraQuestoes(self):
        print(self.questoes)
    def mostraRespostas(self):
        print(self.respostas)
    def armazenaQuestaoResposta(self, novaQuestao, novaResposta):
        self.questoes.append(novaQuestao)
        self.respostas.append(novaResposta)
        