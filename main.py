import random
#Lista onde as palavras estão armazenadas
FRUTAS = ["Maçã","Banana","Manga","Uva","Morango","Abacaxi","Melancia","Laranja","Limão","Mamão","Pera","Kiwi","Cereja","Pêssego","Coco","Goiaba","Melão","Acerola","Maracujá","Pitaya"]
AMBIENTE = ["Floresta","Praia","Montanha","Deserto","Cachoeira","Fazenda","Jardim","Cidade","Rio","Vulcão","Ilha","Campo","Selva","Pântano","Parque","Floresta","tropical","Oceano","Savana"]
NOMES = ["João","Maria","Pedro","Ana","Lucas","Julia","Gabriel","Beatriz","Rafael","Camila","Felipe","Larissa","Daniel","Mariana","Bruno","Isabela","André","Sofia","Henrique","vitória"]
MATERIAIS = ["Madeira","Ferro","Vidro","Plástico","Concreto","Alumínio","Cobre","Aço","Papel","Borracha","Ouro","Prata","Tecido","Couro","Pedra","Cerâmica","Titânio","Aço","inox","Fibra","Cimento"]
PROFISSÕES = ["Médico","Professor","Engenheiro","Advogado","Dentista","Arquiteto","Mecânico","Eletricista","Cozinheiro","Enfermeiro","Policial","Bombeiro","Jornalista","Fotógrafo","Agricultor","Programador","Piloto","Veterinário","Eletricista","Designer"]
#Parte onde ele seleciona uma categoria e depois dentro dela escolhe uma palavra
categorias = {
    "Frutas": FRUTAS,
    "Ambiente": AMBIENTE,
    "Nomes": NOMES,
    "Materiais": MATERIAIS,
    "Profissões": PROFISSÕES
}
#onde mexe on o random  e fazer a part que cria os pontinhos da plavras
categoria = random.choice(list(categorias))
palavra = random.choice(categorias[categoria])
palavra_escolhida_computador = palavra.lower()
falar = ["_"] * len(palavra_escolhida_computador)


    #parte onde o for come ele iciara  pos o pc escoler a categoria e a palavra
tentativas = 6

while tentativas > 0:

    print("============", categoria, "============")

    palavra_escolhida = input("Digite a Letra: ").lower()

    if palavra_escolhida in palavra_escolhida_computador:

        print("Acertou!")

        for i in range(len(palavra_escolhida_computador)):

            if palavra_escolhida_computador[i] == palavra_escolhida:
                falar[i] = palavra_escolhida

    else:

        tentativas -= 1

        print("Errou!")
        print("Vai de novo!")

    # Presiso tirar isso quando o jogo tiver pronto pra não dar a resposta
    print(palavra)

    # Aqui pra baixo não
    print(" ".join(falar))
    print("Chance:", tentativas)
    print("==============================")


    # Verifica se o jogador acertou a palavra
    if "_" not in falar:

        print("PARABÉNS, VOCÊ ACERTOU!")
        print("A palavra era:", palavra)
        break


# Se as 6 chances acabarem
if tentativas == 0:

    print("Você perdeu!")
    print("A palavra era:", palavra)

def draw_character():
    hangman = [
        """"
        -----------
        |
        |
        |
        |
        |
        |
        -
    """,
        """"
        -----------
        |         |
        |         0
        |
        |
        |
        |
        -
    """
    ]
