import unittest
from src.personagens import Personagem, Guerreiro, Mago, Inimigo

class TestPersonagens(unittest.TestCase):

    def test_personagem_atacar(self):
        p1 = Personagem(nome="Heroi", vida=100, ataque=10)
        p2 = Personagem(nome="Vilao", vida=100, ataque=10)
        p1.atacar(p2)
        self.assertEqual(p2.vida, 90)

    def test_guerreiro_atacar(self):
        guerreiro = Guerreiro(nome="Aragorn", vida=100, ataque=15, defesa=5)
        orc = Personagem(nome="Orc", vida=50, ataque=10)
        guerreiro.atacar(orc)
        self.assertEqual(orc.vida, 50 - (15 + 5))

    def test_mago_atacar(self):
        mago = Mago(nome="Gandalf", vida=80, ataque=20, magia=10)
        troll = Personagem(nome="Troll", vida=70, ataque=12)
        mago.atacar(troll)
        self.assertEqual(troll.vida, 70 - (20 + 10))

    def test_inimigo_atacar(self):
        inimigo = Inimigo(nome="Orc", vida=50, ataque=10, tipo="Orc")
        heroi = Personagem(nome="Heroi", vida=100, ataque=10)
        inimigo.atacar(heroi)
        self.assertEqual(heroi.vida, 90)

if __name__ == '__main__':
    unittest.main()