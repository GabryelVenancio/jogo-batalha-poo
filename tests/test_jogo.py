import unittest
from src.jogo import Jogo
from src.personagens import Guerreiro, Mago, Inimigo

class TestJogo(unittest.TestCase):

    def setUp(self):
        self.jogo = Jogo()
        self.guerreiro = Guerreiro(nome="Aragorn", vida=100, ataque=15, defesa=5)
        self.mago = Mago(nome="Gandalf", vida=80, ataque=20, magia=10)
        self.orc = Inimigo(nome="Orc", vida=50, ataque=10, tipo="Orc")
        self.jogo.adicionar_jogador(self.guerreiro)
        self.jogo.adicionar_jogador(self.mago)
        self.jogo.adicionar_inimigo(self.orc)

    def test_adicionar_jogadores_e_inimigos(self):
        self.assertIn(self.guerreiro, self.jogo.jogadores)
        self.assertIn(self.mago, self.jogo.jogadores)
        self.assertIn(self.orc, self.jogo.inimigos)

    def test_iniciar_jogo_vitoria_jogadores(self):
        self.jogo.iniciar()
        self.assertEqual(len(self.jogo.inimigos), 0)
        self.assertGreater(len(self.jogo.jogadores), 0)

    def test_iniciar_jogo_vitoria_inimigos(self):
        self.guerreiro.vida = 0
        self.mago.vida = 0
        self.jogo.iniciar()
        self.assertEqual(len(self.jogo.jogadores), 0)
        self.assertGreater(len(self.jogo.inimigos), 0)

if __name__ == '__main__':
    unittest.main()
