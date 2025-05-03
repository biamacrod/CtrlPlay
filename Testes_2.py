import unittest
from Testes import Prova

class TesteProva(unittest.TestCase):
    def test_armazenarQuestao(self):
        questao = "Quanto é 2 + 1?"
        p = Prova()
        p.armazenaQuestaoResposta(questao, "")
        self.assertIn("Quanto é 2 + 1?", p.questoes)
    def test_armazenarResposta(self):
        resposta = 3
        p = Prova()
        p.armazenaQuestaoResposta("", resposta)
        self.assertIn(3, p.respostas)
    
    
unittest.main(argv=[''], exit=False)