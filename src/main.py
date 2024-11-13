from personagens import Guerreiro, Mago, Inimigo
from jogo import Jogo

if __name__ == "__main__":
    guerreiro = Guerreiro(nome="Aragorn", vida=100, ataque=15, defesa=5)
    mago = Mago(nome="Gandalf", vida=80, ataque=20, magia=10)

    orc = Inimigo(nome="Gorbag", vida=50, ataque=10, tipo="Orc")
    troll = Inimigo(nome="Ugluk", vida=70, ataque=12, tipo="Troll")

    jogo = Jogo()
    jogo.adicionar_jogador(guerreiro)
    jogo.adicionar_jogador(mago)
    jogo.adicionar_inimigo(orc)
    jogo.adicionar_inimigo(troll)

    jogo.iniciar()
