# -*- coding: utf-8 -*-
import random
import time
import pygame

def regras_do_jogo(secao):

    vizinhos = 0
    # celula selecionada, aplicando valor
    selecionada = secao[1][1]

    # soma de todos elementos
    for linha in secao:
        for celula in linha:
            vizinhos += celula

    #retirada do valor da celula central
    vizinhos -= selecionada

    #regra 1 - Qualquer célula viva com menos de dois vizinhos vivos morre de solidão
    if vizinhos <= 1:
        selecionada = 0
        print('morreu de solidão')

    #regra 2 - Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação
    elif vizinhos >= 4:
        selecionada = 0
        print('morreu por superpopulação')

    #regra 3 - Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva
    elif vizinhos == 3:
        selecionada = 1
        print('Nasceu')

    # regra 4 - Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado
    elif vizinhos == 2 or vizinhos == 3:
        print('continua vivo')

    return selecionada

def get_secao(matrix, linha, coluna):

    #analizar a area seguindo, por um plano 3x3
    secao = [[0 for _ in range(3)] for _ in range(3)]

    for sec_l, l in enumerate(range(linha-1, linha+2)):
        for sec_c, c in enumerate(range(coluna-1, coluna+2)):
            secao[sec_l][sec_c] = matrix[l % 50][c % 50]

    return secao


def jogo_da_vida(cenario):

    #gerar o cenário vázio 30X30
    proxima_gera = [[0 for _ in range(50)] for _ in range(50)]

    #percorer o cenário fazendo recorte 3x3 pegando a celular central e vendo as ao lado
    for l, linha in enumerate(cenario):
        for c, coluna in enumerate(linha):
            proxima_gera[l][c] = regras_do_jogo(get_secao(cenario, l, c))

    return proxima_gera

#cenario vazio
CELULA = [[0 for _ in range(50)] for _ in range(50)]

#Gerar os automatos aleatóriamente
CELULA = [[random.choice([0, 1]) for _ in range(50)] for _ in range(50)]

pygame.init()

screen = pygame.display.set_mode((550, 550))

def desenhar_matrix(matrix):

    screen.fill([0, 0, 0])

    for l, linha in enumerate(matrix):
        for c, celula in enumerate(linha):
            if celula:
                # se estiver viva pintar de vermelho
                pygame.draw.rect(
                    screen, (255, 0, 0), (11*c, 11*l, 10, 10)
                )


celula = CELULA

#desenhar o estado inicial das celulas
desenhar_matrix(celula)

pygame.display.flip()

time.sleep(1)

#looping do jogo
while True:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        #finaliza o program se clicar em fechar
        break
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        # quits the program on pressing ESC
        break

    #Atualização do jogo

    #interações
    celula = jogo_da_vida(celula)

    #desenhar
    desenhar_matrix(celula)

    pygame.display.flip()

#delay para cada interação
time.sleep(0.5)

# GAME UPDATE

# runs the game of life to get the next generation
seed = game_of_life(seed)

# DRAWING

# draws the new generation at the screen
draw_matrix(seed)

pygame.display.flip()

# waits a brief moment until going to the next generation
time.sleep(0.05)