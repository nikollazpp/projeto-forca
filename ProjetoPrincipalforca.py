import random
import os
#Lista onde as palavras estão armazenadas
FRUTAS = ["Maçã","Banana","Manga","Uva","Morango","Abacaxi","Melancia","Laranja","Limão","Mamão","Pera","Kiwi","Cereja","Pêssego","Coco","Goiaba","Melão","Acerola","Maracujá","Pitaya"]
AMBIENTE = ["Floresta","Praia","Montanha","Deserto","Cachoeira","Fazenda","Jardim","Cidade","Rio","Vulcão","Ilha","Campo","Selva","Pântano","Parque","Floresta","tropical","Oceano","Savana"]
NOMES = ["João","Maria","Pedro","Ana","Lucas","Julia","Gabriel","Beatriz","Rafael","Camila","Felipe","Larissa","Daniel","Mariana","Bruno","Isabela","André","Sofia","Henrique","vitória"]
MATERIAIS = ["Madeira","Ferro","Vidro","Plástico","Concreto","Alumínio","Cobre","Aço","Papel","Borracha","Ouro","Prata","Tecido","Couro","Pedra","Cerâmica","Titânio","Aço","inox","Fibra","Cimento"]
PROFISSÕES = ["Médico","Professor","Engenheiro","Advogado","Dentista","Arquiteto","Mecânico","Eletricista","Cozinheiro","Enfermeiro","Policial","Bombeiro","Jornalista","Fotógrafo","Agricultor","Programador","Piloto","Veterinário","Eletricista","Designer"]

# Função que escolhe a lista de palavras
def escolher_palavras(tentativas):

    match tentativas:

        case 6:
            return FRUTAS

        case 5:
            return AMBIENTE

        case 4:
            return NOMES

        case 3:
            return MATERIAIS

        case 2:
            return PROFISSÕES

        case _:
            return None

# Número inicial de tentativas
tentativas = 6

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
oque_o_jogador_chutou = []
while tentativas > 0:

    print("============", categoria, "============")
  
    palavra_escolhida = input("Digite a Letra ou palavra: ").lower().strip()
    # aceitar somente entradas com letras
    if not palavra_escolhida.isalpha():
        print("Temos um palhaço.")
        continue

    # se o jogador chutar uma palavra inteira
    if len(palavra_escolhida) > 1:
        if palavra_escolhida == palavra_escolhida_computador:
            falar = list(palavra_escolhida_computador)
            print("PARABÉNS, VOCÊ ACERTOU!")
            print("A palavra era:", palavra)
            break
        else:
            tentativas -= 1
            print("Errou a palavra!")
            print("Vai de novo!")
    else:
        if palavra_escolhida in palavra_escolhida_computador:
            print("Acertou!")
            for i in range(len(palavra_escolhida_computador)):
                if palavra_escolhida_computador[i] == palavra_escolhida:
                    falar[i] = palavra_escolhida
        else:
            tentativas -= 1
            print("Errou!")
            print("Vai de novo!")

    if len(palavra_escolhida) == 1 and palavra_escolhida.isalpha() and palavra_escolhida not in oque_o_jogador_chutou:
        oque_o_jogador_chutou.append(palavra_escolhida)
        print("Palavras Escolhidas:", ", ".join(oque_o_jogador_chutou))

    #não juntar no else
    print(" ".join(falar))
    print("Chance:", tentativas,"/6")
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