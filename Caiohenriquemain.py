import pygame
from caiohenriquetelas import *
from caiohenriquefunções import *

# inicializar o pygame
pygame.init()
pygame.mixer.init()

# criar uma tela
largura = 1200
altura = 700
tela = pygame.display.set_mode((largura, altura))

# titulo e icone
pygame.display.set_caption("Deep Sea v2.0")
icone = pygame.image.load("imagens/submarino.png")
pygame.display.set_icon(icone)

# clique função
def click(rect, mouse):
    return rect.collidepoint(mouse)


# loop principal
rodando = True

#inicializar variaves
local = "menu_inicial"
musica_atual = None
texto_tanques = ""
mensagem_erro = ""
dimensao = None  # Ex: 9x9 ou 15x15
dificuldade = None  # Ex: fácil, médio ou difícil
tanques = None  # Número de tanques

#começo do lopp principal e do jogo em si
while rodando:
    eventos = pygame.event.get()   #essa função vai aparecer algumas vezes e ela serv pra capturar os enventos que ocorrem na tela do pygame e utilizamos um for pra separalas e analisalas 
    for event in eventos:
        if event.type == pygame.QUIT:
            rodando = False

        # Captura de texto e validação
        if local == "tela2":
            # Captura de texto para o campo de tanques
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    texto_tanques = texto_tanques[:-1]  # Remove o último caractere
                elif event.key == pygame.K_RETURN:
                    if texto_tanques.isdigit() and 160 <= int(texto_tanques) <= 500:
                        tanques = int(texto_tanques)
                        mensagem_erro = ""  # Limpa mensagem de erro
                    else:
                        mensagem_erro = "Tanques devem estar entre 160 e 500!"
                elif event.unicode.isdigit():
                    texto_tanques += event.unicode  # Adiciona o caractere digitado

            # Captura de cliques para os botões
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # Botões para escolher a dimensão
                if click(reacao_9x9_botao, mouse):
                    dimensao = 9
                elif click(reacao_15x15_botao, mouse):
                    dimensao = 15

                # Botões para escolher a dificuldade
                if click(reacao_facil, mouse):
                    dificuldade = "facil"
                elif click(reacao_medio, mouse):
                    dificuldade = "medio"
                elif click(reacao_dificil, mouse):
                    dificuldade = "dificil"

                # Botão de voltar
                if click(reacao_play_botao, mouse):
                    # Verificar se todas as configurações foram definidas
                    if dimensao and dificuldade and tanques:
                        jogo = inicializar(dimensao=dimensao, dificuldade=dificuldade, tanques=tanques)
                        local = "tela_jogo"
                    else:
                        mensagem_erro = "Preencha todas as configurações!"

        # Lógica para outras telas
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if local == "menu_inicial" and click(reacao_botao_play, mouse):
                local = "tela2"
            elif local == "menu_inicial" and click(reacao_botao_tutorial, mouse):
                local = "tutorial"
            elif local == "tutorial" and click(reacao_botao_voltar, mouse):
                local = "menu_inicial"

    # Atualiza a música
    musica_atual = tocar_musica(local, musica_atual)

    # Renderiza as telas, e da returns nas reações(posição de click) de seus botões, assim o for de eventos verifica se teve click
    if local == "menu_inicial":
        reacao_botao_play, reacao_botao_tutorial = tela_menu_inicial(largura, altura, tela)
    elif local == "tutorial":
        reacao_botao_voltar = tela_tutorial(largura, altura, tela)
    elif local == "tela2":
        (
            reacao_9x9_botao,
            reacao_15x15_botao,
            reacao_facil,
            reacao_medio,
            reacao_dificil,
            reacao_botao_voltar,reacao_play_botao
        ) = tela2(largura, altura, tela, texto_tanques, mensagem_erro)
    elif local == "tela_jogo":
        rodando = tela_jogo(largura, altura, tela, jogo, rodando)

    pygame.display.flip()

pygame.quit()
