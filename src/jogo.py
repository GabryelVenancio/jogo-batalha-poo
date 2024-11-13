class Jogo:
    def __init__(self):
        self.jogadores = []
        self.inimigos = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def adicionar_inimigo(self, inimigo):
        self.inimigos.append(inimigo)

    def iniciar(self, exibir_mensagem=True):
        if exibir_mensagem:
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
        
        if exibir_mensagem:
            if self.jogadores:
                print("Jogadores venceram a batalha!")
            else:
                print("Inimigos venceram a batalha!")
