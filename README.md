# Jogo de Batalha POO

**Descrição**  
Jogo de Batalha POO é um jogo simples desenvolvido em Python que demonstra os conceitos de Programação Orientada a Objetos (POO). Os jogadores controlam personagens que lutam contra inimigos, utilizando atributos como vida, ataque e habilidades especiais. O objetivo é derrotar todos os inimigos antes que sejam derrotados.

## Funcionalidades


Instalação
Requisitos
Python 3.8 ou superior

### Classes e Objetos
- **Personagem**: Classe base para todos os personagens.
- **Guerreiro**, **Mago**, **Inimigo**: Classes derivadas com atributos e métodos específicos.

### Conceitos de POO
- **Herança**: Reutilização de atributos e métodos na criação de classes derivadas.
- **Polimorfismo**: Sobrescrita de métodos para comportamentos específicos.
- **Encapsulamento**: Uso de getters e setters para proteger os atributos.

### Lógica de Batalha
- **Turnos alternados** entre jogadores e inimigos.
- **Remoção de personagens** quando a vida atinge 0.

### Testes Automatizados
- **Cobertura de funcionalidades principais** usando `unittest`.

## Tecnologias Utilizadas 🛠️

<p>
  <img src="https://img.icons8.com/color/48/000000/python.png" alt="Python Logo" width="40" height="40"/>
</p>

- **Python 3.8 ou superior**

## Instalação

### Requisitos
- **Python 3.8** ou superior

### Clone o Repositório
```bash
git clone https://github.com/seu_usuario/jogo_poo.git
cd jogo_poo

Crie e Ative um Ambiente Virtual

No Windows:

python -m venv venv
.\venv\Scripts\activate

No macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Uso
Executar o Jogo
Para iniciar o jogo, execute o seguinte comando no terminal:

python src/jogo.py

Nota: Certifique-se de que o ambiente virtual está ativado antes de executar o comando.

Estrutura do Jogo
Jogadores:

Guerreiro: Possui atributos de defesa adicionais.
Mago: Possui atributos de magia para ataques especiais.

Inimigos:

Diversos tipos como Orc, Troll, etc., cada um com atributos específicos.
Fluxo do Jogo
Início da Batalha:

Jogadores atacam os inimigos.
Inimigos atacam os jogadores.

Condições de Vitória:

Jogadores Vencem: Quando todos os inimigos são derrotados.
Inimigos Vencem: Quando todos os jogadores são derrotados.

Testes

python -m unittest discover -s tests

no Windows, se estiver usando o lançador py:

py -m unittest discover -s tests

Estrutura dos Testes
tests/test_personagens.py: Testes para as classes de personagens.
tests/test_jogo.py: Testes para a lógica do jogo.
Resultado dos Testes
Após executar os testes, você deverá ver uma saída indicando o status de cada teste. Exemplo de saída bem-sucedida:


Ran 3 tests in 0.299s
OK

Se algum teste falhar, revise os métodos e as condições esperadas para identificar e corrigir o problema.

Contato
Desenvolvedor: Gabryel Venâncio
Email: gabrielvenanciocleffs@gmail.com
GitHub: https://github.com/GabryelVenancio

cd jogo_poo

