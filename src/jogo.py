from .personagens import Guerreiro, Mago, Inimigo

class Jogo:
    def __init__(self):
        self.jogadores = []
        self.inimigos = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def adicionar_inimigo(self, inimigo):
        self.inimigos.append(inimigo)

    def iniciar(self):
        print("Bem-vindo ao Jogo de Batalha!")
        
        self.jogadores = [jogador for jogador in self.jogadores if jogador.vida > 0]
        self.inimigos = [inimigo for inimigo in self.inimigos if inimigo.vida > 0]
        
        while self.jogadores and self.inimigos:
            for jogador in self.jogadores[:]:
                if not self.inimigos:
                    break
                alvo = self.inimigos[0]
                jogador.atacar(alvo)
                if alvo.vida <= 0:
                    self.inimigos.remove(alvo)
            for inimigo in self.inimigos[:]:
                if not self.jogadores:
                    break
                alvo = self.jogadores[0]
                inimigo.atacar(alvo)
                if alvo.vida <= 0:
                    self.jogadores.remove(alvo)
        if self.jogadores:
            print("Jogadores venceram a batalha!")
        else:
            print("Inimigos venceram a batalha!")

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
