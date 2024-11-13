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
    
# from personagens import Guerreiro, Mago, Inimigo

# class Jogo:
#     def __init__(self):
#         self.jogadores = []
#         self.inimigos = []

#     def adicionar_jogador(self):
#         tipo = input("Escolha o tipo do seu personagem (Guerreiro/Mago): ").strip().lower()
#         nome = input("Digite o nome do seu personagem: ")
#         vida = int(input("Defina a vida do seu personagem (ex: 100): "))
#         ataque = int(input("Defina o ataque do seu personagem (ex: 15): "))

#         if tipo == "guerreiro":
#             defesa = int(input("Defina a defesa do seu Guerreiro (ex: 5): "))
#             jogador = Guerreiro(nome=nome, vida=vida, ataque=ataque, defesa=defesa)
#         elif tipo == "mago":
#             magia = int(input("Defina a magia do seu Mago (ex: 10): "))
#             jogador = Mago(nome=nome, vida=vida, ataque=ataque, magia=magia)
#         else:
#             print("Tipo inválido! Criando um Guerreiro padrão.")
#             jogador = Guerreiro(nome="Guerreiro Padrão", vida=100, ataque=15, defesa=5)

#         self.jogadores.append(jogador)

#     def adicionar_inimigo(self, nome, vida, ataque, tipo):
#         inimigo = Inimigo(nome=nome, vida=vida, ataque=ataque, tipo=tipo)
#         self.inimigos.append(inimigo)

#     def iniciar(self):
#         print("Bem-vindo ao Jogo de Batalha!")

#         while self.jogadores and self.inimigos:
#             for jogador in self.jogadores[:]:
#                 if not self.inimigos:
#                     break

#                 print("\nInimigos disponíveis para atacar:")
#                 for i, inimigo in enumerate(self.inimigos):
#                     print(f"{i}. {inimigo.nome} (Vida: {inimigo.vida})")

#                 indice_alvo = int(input("Escolha o índice do inimigo que deseja atacar: "))
#                 alvo = self.inimigos[indice_alvo]
                
#                 jogador.atacar(alvo)

#                 if alvo.vida <= 0:
#                     print(f"{alvo.nome} foi derrotado!")
#                     self.inimigos.remove(alvo)

#             for inimigo in self.inimigos[:]:
#                 if not self.jogadores:
#                     break

#                 alvo = self.jogadores[0]
#                 inimigo.atacar(alvo)

#                 if alvo.vida <= 0:
#                     print(f"{alvo.nome} foi derrotado!")
#                     self.jogadores.remove(alvo)

#         if self.jogadores:
#             print("Jogadores venceram a batalha!")
#         else:
#             print("Inimigos venceram a batalha!")


# if __name__ == "__main__":
#     jogo = Jogo()

#     num_jogadores = int(input("Quantos jogadores deseja adicionar? "))
#     for _ in range(num_jogadores):
#         jogo.adicionar_jogador()

#     jogo.adicionar_inimigo(nome="Orc", vida=50, ataque=10, tipo="Orc")
#     jogo.adicionar_inimigo(nome="Troll", vida=70, ataque=12, tipo="Troll")

#     jogo.iniciar()
