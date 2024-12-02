import pygame
from caiohenriquefunções import *
import random

#função de click(saber onde esta acontecendo um click)
def click(rect, mouse):
    return rect.collidepoint(mouse)



def tela_menu_inicial(largura, altura, tela):
    # Carregar fundo e desenhar ele no fundo da tela
    fundo = pygame.image.load('imagens/Fundo.png')
    fundo = pygame.transform.scale(fundo, (largura, altura))
    #calcular meio da tela
    x = (largura) // 2
    y = (altura) // 2

    logo = pygame.image.load("imagens/logo.png")
    logo = pygame.transform.scale(logo,(450,300))

    # Carregar botão
    botao_icon = pygame.image.load("imagens\play1.png")
    botao_icon = pygame.transform.scale(botao_icon, (150, 75))
    # Ajustar a posição  e esse padrão vai se repetir pra todo botão infelizmente
    reacao_pegar_botao = botao_icon.get_rect(center=(x, y + 100))

    botao_icon_tutorial = pygame.image.load("imagens/tutorialsemfundo.png")
    botao_icon_tutorial = pygame.transform.scale(botao_icon_tutorial,(150,75))
    reacao_pegar_botao2 = botao_icon_tutorial.get_rect(center=(x,y +200))
    # Desenhar na tela
    tela.blit(fundo, (0, 0))
    tela.blit(botao_icon, reacao_pegar_botao)
    tela.blit(botao_icon_tutorial, reacao_pegar_botao2)
    tela.blit(logo,(x-200,y-300))
    #retorna a posição dos botoes para verificar o click
    return reacao_pegar_botao , reacao_pegar_botao2

def tela_tutorial(largura,altura,tela):
    fundo = pygame.image.load('imagens\Fundo.png')
    fundo = pygame.transform.scale(fundo,(largura,altura))

    x = (largura) // 2
    y = (altura) // 2
    
    #botão de voltar
    botao_icon = pygame.image.load("imagens/voltar.png")
    botao_icon = pygame.transform.scale(botao_icon,(150,75))
    reacao_pegar_botao = botao_icon.get_rect(center=(x,y+200))
    
    
    tela.blit(fundo,(0,0))
    tela.blit(botao_icon, reacao_pegar_botao)

    return reacao_pegar_botao

    fundo = pygame.image.load('imagens/Fundo.png')
    fundo = pygame.transform.scale(fundo, (largura, altura))

    x = (largura) // 2
    y = (altura) // 2

def tela2(largura, altura, tela,texto,mensagem_erro):
    #aqui é onde o jogador escolhe as coisas do jogo dimensão dificuldade e etc, nesse sentido aqui vai ter muito returns de botões e funçoes
    fonte = pygame.font.Font(None,50)
    fundo = pygame.image.load('imagens/Fundo.png')
    fundo = pygame.transform.scale(fundo, (largura, altura))
    tela.blit(fundo, (0, 0))

    x = (largura) // 2
    y = (altura) // 2
    #crio um dicionario armazenando o nome que quero que apareça na tela e sua posição
    textos = [{"texto": "MATRIZ:", "pos": (100, 100)},{"texto": "TANQUES:", "pos": (100, 200)},{"texto": "160 a 500", "pos": (600, 200)},{"texto": "DIFICULDADE:", "pos":(100,300)}]

    #um for pra identificar e desenhar na tela
    for item in textos:
        texto_surface = fonte.render(item["texto"],True,(0,0,0))
        tela.blit(texto_surface,item["pos"])

    #alguns bottonssssss que se auto explicam ex 9x9 pra dimsensão 9
    botao_icon = pygame.image.load("imagens/voltar.png")
    botao_icon = pygame.transform.scale(botao_icon,(150, 75))
    reacao_voltar_botao = botao_icon.get_rect(center=(x+500,y+300))

    botao_icon_play = pygame.image.load("imagens/play1.png")
    botao_icon_play = pygame.transform.scale(botao_icon_play,(150, 75))
    reacao_play_botao = botao_icon.get_rect(center=(x+500,y+300))

    botao_9x9 = pygame.image.load("imagens/9x9.png")
    botao_9x9= pygame.transform.scale(botao_9x9,(200,75))
    reacao_9x9_botao = botao_9x9.get_rect(center=(400,115))

    botao_15x15 = pygame.image.load("imagens/15x15.png")
    botao_15x15= pygame.transform.scale(botao_15x15,(200,75))
    reacao_15x15_botao = botao_15x15.get_rect(center=(600,115))

    botao_facil = pygame.image.load("imagens/facil.png")
    botao_facil = pygame.transform.scale(botao_facil,(200,75))
    reacao_facil = botao_facil.get_rect(center=(450,315))

    botao_medio = pygame.image.load("imagens/medio.png")
    botao_medio = pygame.transform.scale(botao_medio,(200,75))
    reacao_medio = botao_facil.get_rect(center=(650,315))

    botao_dificil = pygame.image.load("imagens/dificil.png")
    botao_dificil = pygame.transform.scale(botao_dificil,(200,75))
    reacao_dificil = botao_dificil.get_rect(center=(850,315))   
    #desenhar todos os botões na tela
    tela.blit(botao_icon, reacao_voltar_botao)
    tela.blit(botao_9x9,reacao_9x9_botao)
    tela.blit(botao_15x15,reacao_15x15_botao)
    tela.blit(botao_facil,reacao_facil)
    tela.blit(botao_medio,reacao_medio)
    tela.blit(botao_dificil,reacao_dificil) 
    tela.blit(botao_icon_play,reacao_play_botao)
    #imput do texto jogados
    input_box = pygame.Rect(300, 200, 200, 50)  # Retângulo para input 
    cor_input = (255, 255, 255)  # Cor do campo

    #desenhar a imput_box
    pygame.draw.rect(tela, cor_input, input_box)
    pygame.draw.rect(tela, (0, 0, 0), input_box, 2)  # Borda preta
    fonte = pygame.font.Font(None, 50)
    texto_surface = fonte.render(texto, True, (0, 0, 0))
    tela.blit(texto_surface, (input_box.x + 10, input_box.y + 10))

    #mensagem de erro caso algo n esteja nos planos(maior ou menor que o esperado)
    if mensagem_erro:
        erro_surface = fonte.render(mensagem_erro, True, (255, 0, 0))
        tela.blit(erro_surface, (300, 260))
    #return de todas as posiçoes de botoes
    return reacao_9x9_botao, reacao_15x15_botao, reacao_facil, reacao_medio, reacao_dificil,reacao_voltar_botao,reacao_play_botao 

#aqui utilizei variavel global ( me perdoe pamela e caro leito ) pois dentro das funções elas eram afetadas pelo loop principal, meio icoerente o uso talvez
numero = 0
indice_jogador = 0
def tela_jogo(largura,altura,tela,jogo,rodando):
    global indice_jogador
    global numero
    #faço o msm de sempre imagem de fundo e etc
    fundo = pygame.image.load('imagens/Fundo.png')
    fundo = pygame.transform.scale(fundo, (largura, altura))
    moldura = pygame.image.load("imagens/moldura.png")
    moldura = pygame.transform.scale(moldura,(220,220)) #moldura que mostrar o personagem atual_eu dou blit nela logo no começo para que ela fique em baixo do blit do jogador ja que o pygame funciona por camadas
    botao_pegar = pygame.image.load('imagens/pegar.png')
    botao_pegar = pygame.transform.scale(botao_pegar,(300,300))
    reacao_pegar = botao_pegar.get_rect(center=(1100,500))
    tela.blit(fundo, (0, 0)) 
    if jogo.jogadores_lista[indice_jogador].vida ==  False: #verifico se o jogador atual esta vivo, se n estiver avança para o proximo
        indice_jogador +=1
       #outro for para conseguir os eventos dessa tela especificar(pra n ter que voltar na do loop principal)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False  #porem a varialvel de fechar o jogo continuar a msm pra da pra fechar o jogo inteiro
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos() #posição do click = mouse
            jogo.verificar_clique(mouse,jogo,jogador=jogo.jogadores_lista[indice_jogador]) 
            if click(reacao_pegar,mouse):
                jogo.pegar_tesouro(jogador = jogo.jogadores_lista[indice_jogador])
                indice_jogador += 1
                numero = random.randint(0,3)
        


            
    #se o indice for = ao numero de jogadores reseta 
    if indice_jogador >= len(jogo.jogadores_lista):
        indice_jogador = 0
    jogador_atual_imagem = jogo.jogadores_lista[indice_jogador].jogador_imagem #desenho da moldura
    jogador_atual_imagem = pygame.transform.scale(jogador_atual_imagem,(200,200))
    #e algumas funções que vão ser melhor explicadas na classe
    jogo.desenhar_mapa(tela, largura, altura,jogador=jogo.jogadores_lista[indice_jogador],numero_aleatorio = numero)
    tela.blit(moldura,(980,30))
    tela.blit(jogador_atual_imagem,(980,30))
    tela.blit(botao_pegar,reacao_pegar)
    return rodando

#aqui é complementar apenas musicas para fundo, nem sei se vai funionar ja que o forms deve ter limite 
def tocar_musica(local, musica_atual):
    if local == "menu_inicial" and musica_atual != "menu_inicial":
        pygame.mixer.music.load("musicas/Sun Araw - Horse Steppin'.mp3")
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(-1)
        musica_atual = "menu_inicial"
    elif local == "tela2" and musica_atual != "tela2":
        pygame.mixer.music.load("musicas\Terraria Music - Day.mp3")
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(-1)
        musica_atual = "tela2"
    elif local == "tela_jogo" and musica_atual != "tela_jogo":
        pygame.mixer.music.load("musicas\Terraria Music - Day.mp3")
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(-1)
        musica_atual = "tela_jogo"
    return musica_atual