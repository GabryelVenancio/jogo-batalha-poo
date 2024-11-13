# Classe base Personagem
class Personagem:
    def __init__(self, nome, vida, ataque):
        self._nome = nome
        self._vida = vida
        self._ataque = ataque

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = valor

    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, valor):
        self._ataque = valor

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome} causando {self.ataque} de dano.")
        alvo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")

# HERANÇA: A classe Guerreiro herda de Personagem
class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque)  # HERANÇA: Herda atributos nome, vida e ataque de Personagem
        self._defesa = defesa

    @property
    def defesa(self):
        return self._defesa

    @defesa.setter
    def defesa(self, valor):
        self._defesa = valor

    # POLIMORFISMO: O método 'atacar' é sobrescrito para incluir a defesa
    def atacar(self, alvo):
        dano_total = self.ataque + self.defesa  # Calcula o dano total considerando a defesa do Guerreiro
        print(f"{self.nome} (Guerreiro) ataca {alvo.nome} com ataque de {self.ataque} e defesa de {self.defesa}, causando {dano_total} de dano.")
        alvo.receber_dano(dano_total)

# HERANÇA: A classe Mago herda de Personagem
class Mago(Personagem):
    def __init__(self, nome, vida, ataque, magia):
        super().__init__(nome, vida, ataque)  # HERANÇA: Herda atributos nome, vida e ataque de Personagem
        self._magia = magia

    @property
    def magia(self):
        return self._magia

    @magia.setter
    def magia(self, valor):
        self._magia = valor

    # POLIMORFISMO: O método 'atacar' é sobrescrito para incluir o atributo magia
    def atacar(self, alvo):
        dano_total = self.ataque + self.magia  # Calcula o dano total considerando a magia do Mago
        print(f"{self.nome} (Mago) lança uma magia em {alvo.nome}, causando {dano_total} de dano.")
        alvo.receber_dano(dano_total)

# HERANÇA: A classe Inimigo herda de Personagem
class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, tipo):
        super().__init__(nome, vida, ataque)  # HERANÇA: Herda atributos nome, vida e ataque de Personagem
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    # POLIMORFISMO: O método 'atacar' é sobrescrito para personalizar o ataque do inimigo
    def atacar(self, alvo):
        print(f"Inimigo {self.nome} do tipo {self.tipo} ataca {alvo.nome}, causando {self.ataque} de dano.")
        alvo.receber_dano(self.ataque)
