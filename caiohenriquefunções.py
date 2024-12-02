import random
import pygame
import math

#aqui o bixo pega

#uma classe para os jogadores
class jogadores: 
    def __init__(self,numero):
        self.vida = True
        self.tesouros = 0
        self.tesouros_no_submarino = 0
        self.numero_do_jogador = numero
        #dependendo do numero que eles ganham no seu nascimento( inicialização kskss) eles vao ter imagens e posições diferentes
        if self.numero_do_jogador == 2:
            jogador_imagem = pygame.image.load("imagens/jogador2.png")
            jogador_imagem_dead = pygame.image.load("imagens/dead_2.png")
            self.jogador_imagem_dead = pygame.transform.scale(jogador_imagem_dead,(30,30))
            self.jogador_imagem = pygame.transform.scale(jogador_imagem, (30, 30) )
            self.posiçao =(0,2)
        elif self.numero_do_jogador == 1:
            jogador_imagem = pygame.image.load("imagens/jogador1.png")
            jogador_imagem_dead = pygame.image.load("imagens/dead_1.png")
            self.jogador_imagem_dead = pygame.transform.scale(jogador_imagem_dead,(30,30))
            self.jogador_imagem = pygame.transform.scale(jogador_imagem, (30, 30) )
            self.posiçao = (0,1)
        elif self.numero_do_jogador == 3:
            jogador_imagem = pygame.image.load("imagens/jogador3.png")
            jogador_imagem_dead = pygame.image.load("imagens/dead_3.png")
            self.jogador_imagem_dead = pygame.transform.scale(jogador_imagem_dead,(30,30))
            self.jogador_imagem = pygame.transform.scale(jogador_imagem, (30, 30) )
            self.posiçao =(0,3)
        elif self.numero_do_jogador == 4:
            jogador_imagem = pygame.image.load("imagens/jogador4.png")
            jogador_imagem_dead = pygame.image.load("imagens/dead_4.png")
            self.jogador_imagem_dead = pygame.transform.scale(jogador_imagem_dead,(30,30))
            self.jogador_imagem = pygame.transform.scale(jogador_imagem, (30, 30) )
            self.posiçao =(0,4)


#a classe principal aqui é onde a coisa acontece
class Jogo:
    def __init__(self, dimensao,tanques):
        #inicialização de algumas variaves importantes
        self.dimensao = dimensao
        self.tanques = tanques
        self.mapa_jogadores = self.criar_matriz() #bem uma coisa muita importante é que eu preferi criar uma matriz para os jogadores e outra para as bombas e tesouros pois assim eu poderia contralar mais os tesouros e bombas sem me preucupar com o movimento dos jogadores, como se fosse camadas :))))) eu fiquei muito orgulhoso com esse pensamento meu
        self.mapa_tesouro_bombas = self.criar_matriz()
        self.jogadores_lista = []
        self.celulas = [] 
    #função para criar uma matriz zerada simples sem paranalé
    def criar_matriz(self):
        matriz = []
        for i in range(self.dimensao):
            linha = []
            for j in range(self.dimensao):
                linha.append(0)
            matriz.append(linha)
        return matriz

    #função para adicionar jogadores ao mapa ao incializar
    def adicionar_jogador(self, jogador):
        (x, y) = jogador.posiçao
        self.mapa_jogadores[x][y] = jogador.numero_do_jogador
        self.jogadores_lista.append(jogador)

    #função para adicionar os tesouros em seus respectivos lugares 10 valor 1 20 valor 2 e 30 valor 5 para o jogador de 1/3 em um terço do mapa eles aumentam
    def adicionar_tesouros(self):
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                if self.mapa_jogadores[i][j] not in [1,2,3,4]:
                    if (i+1) <= self.dimensao//3:
                        self.mapa_tesouro_bombas[i][j] = 10
                    elif self.dimensao//3 < (i+1) <= self.dimensao*2//3:
                        self.mapa_tesouro_bombas[i][j] = 20
                    elif self.dimensao*2//3 < (i+1) <= self.dimensao:
                        self.mapa_tesouro_bombas[i][j] = 30
    #as taxas de spawn de bombas eu usei o .ceil para abreviar o 0.81 para 1 ja que o python vai para o 0 com meus metodos porem aqui tudo normal de acordo com oq esta no problema
    def adicionar_bombas(self,dificuldade):
        if dificuldade == "facil":
            taxa =(self.dimensao**2)/100
            taxa = math.ceil(taxa)
        elif dificuldade == "medio":
            taxa =(self.dimensao**2)*(5/100)
        elif dificuldade == "dificil":
            taxa =(self.dimensao**2)*(15/100)
        #Um for para colocalas no mapa delas
        for i in range(int(taxa)):
            x_local = random.randint(4 ,self.dimensao-1)
            y_local = random.randint(0,self.dimensao-1)
            self.mapa_tesouro_bombas [x_local][y_local] = 50
    #função para pegar os tesouros da posição dos jogadores que a chaman 
    def pegar_tesouro(self,jogador):
        x,y = jogador.posiçao
        if self.mapa_tesouro_bombas[x][y] == 10:
            self.mapa_tesouro_bombas[x][y] = 0
            jogador.tesouros += 1
        elif self.mapa_tesouro_bombas[x][y] == 20:
            self.mapa_tesouro_bombas[x][y] = 0
            jogador.tesouros += 2
        elif self.mapa_tesouro_bombas[x][y] == 30:
            self.mapa_tesouro_bombas[x][y] = 0
            jogador.tesouros += 5

            
    #função mais importante, ela desenha tudo na tela
    def desenhar_mapa(self, tela, largura, altura,jogador,numero_aleatorio):
        #eu preferi (e por dica do jedi) criar o tamanho da celula proporcional a dimensão que o jogador escolheu e a tela do jogo, muito obrigado jedi me ajudo dms aq
        largura_matriz = largura // 1.25
        largura_celula = largura_matriz // self.dimensao
        altura_matriz = altura * 0.8
        altura_celula = altura_matriz // self.dimensao
        #inicio matriz é so pra matriz começa mais embaixo dando aquele espaçozinho
        inicio_matriz = (altura - altura_matriz)
        preto = (0, 0, 0)
        fonte = pygame.font.Font(None,50)
        #desenho a quantidades de tanques e tesouros de cada jogador na tela
        texto_surface = fonte.render(f"{self.tanques} tanques",True,preto)
        texto_surface2 = fonte.render(f"Tesouros: {jogador.tesouros}",True,preto)
        verde_esverdeado = (180, 255, 180)
        tela.blit(texto_surface,(980,320))
        tela.blit(texto_surface2,(980,420))
        self.celulas = []


        #se o jogador tiver vivo ele pode criar as casas que ele pode ir se n pula a vez
        if jogador.vida == True:
            x_jogador,y_jogador = jogador.posiçao
            #dar uma explicada aq, eu pego a quantidade de numero aleatorio e numero ex o numero aleatorio é 2 eu crio posições variando de -2,-1,1,2 assim as casas permitidas em que o jogador pode ir, criando aqueles quadrados verdes(meus colegas de curso me ajudaram dms nessa parte ent muito obrigado a todos)
            self.casas_permitidas = []
            for fx in range(-numero_aleatorio,numero_aleatorio+1):
                nova_x = x_jogador + fx
                if 0 <= nova_x< self.dimensao:
                    self.casas_permitidas.append((nova_x,y_jogador))

            for fy in range(-numero_aleatorio,numero_aleatorio+1):
                nova_y = y_jogador + fy
                if 0 <= nova_y < self.dimensao:
                    self.casas_permitidas.append((x_jogador,nova_y))
        else:
            self.casas_permitidas = []


        for i in range(self.dimensao):
            linha = []  
            for j in range(self.dimensao):
                x = j * largura_celula
                y = inicio_matriz + i * altura_celula
                #aqui é onde se desenha tudo na tela o x e o y são a posição em que vamos esta pondo as coisas , como se a tela fosse uma matriz assim separando ela por x e y e manipulando utilizando o local delas


                retangulo = pygame.Rect(x, y, largura_celula, altura_celula)
                linha.append(retangulo)
                if (i,j) in self.casas_permitidas and self.mapa_jogadores[i][j] not in[1,2,3,4]:
                    pygame.draw.rect(tela, verde_esverdeado, retangulo)
                    
                if self.mapa_tesouro_bombas[i][j] == 10:
                    tesouro1 = pygame.image.load("imagens/tesouro1.png")
                    tesouro1 = pygame.transform.scale(tesouro1,(largura_celula-5,altura_celula-5))
                    tela.blit(tesouro1,(x,y))
                
                elif self.mapa_tesouro_bombas[i][j] == 20:
                    tesouro2 = pygame.image.load("imagens/tesouro2.png")
                    tesouro2 = pygame.transform.scale(tesouro2,(largura_celula,altura_celula))
                    tela.blit(tesouro2,(x,y))
                
                elif self.mapa_tesouro_bombas[i][j] == 30:
                    tesouro3 = pygame.image.load("imagens/tesouro3.png")
                    tesouro3 = pygame.transform.scale(tesouro3,(largura_celula-5,altura_celula-5))
                    tela.blit(tesouro3,(x,y))

                elif self.mapa_tesouro_bombas[i][j] == 50:
                    bomba = pygame.image.load("imagens/Bomb.png")
                    bomba = pygame.transform.scale(bomba,(largura_celula-5,altura_celula-5))
                    tela.blit(bomba,(x,y))
            
                pygame.draw.rect(tela, preto, retangulo, 1)

                # Desenhe o jogador, se houver e se estiver morto ele vira o amonngus cortadinho bixinho coitado
                if self.mapa_jogadores[i][j] in [1, 2, 3, 4]:
                    jogador = self.jogadores_lista[self.mapa_jogadores[i][j] - 1]
                    if jogador.vida == True:
                        jogador_imagem_redimensionada = pygame.transform.scale(jogador.jogador_imagem, (largura_celula, altura_celula))
                    else:
                        jogador_imagem_redimensionada = pygame.transform.scale(jogador.jogador_imagem_dead,(largura_celula,altura_celula))
                    tela.blit(jogador_imagem_redimensionada, (x, y))
            self.celulas.append(linha)
        #aqui verifico o click e quem quer que click pra se movimentar por isso jogo e jogador acabam entrando aqui
    def verificar_clique(self, pos,jogo,jogador):
        if jogador.vida == True:
            for i, linha in enumerate(self.celulas):
                for j, rect in enumerate(linha):
                    if rect.collidepoint(pos) and (i,j) in self.casas_permitidas:  # Verifica se a posição do clique está no retângulo permitido para a movimentação
                        self.mover_para_celula(i, j,jogo,jogador)
        else:
            return

    def mover_para_celula(self, i, j,jogo, jogador):
        x, y = jogador.posiçao
        diferença_x = x - i
        diferença_y = y - j
        #aqui é a parte da movimentação e eu calculo a distencia percorrida, ponto inicial - final (fisica papaei) e uso no consumo ali em baixo
        if self.mapa_jogadores[i][j] not in [1,2,3,4]:
            self.mapa_jogadores[x][y] = 0
            self.mapa_jogadores[i][j] = jogador.numero_do_jogador
            jogador.posiçao = (i, j)
            if self.mapa_tesouro_bombas[i][j] == 50:
                jogador.vida = False
                self.mapa_tesouro_bombas[i][j] = 0
            consumo = 0
            if abs(diferença_y) > 0:
                consumo = abs(diferença_y) * jogador.tesouros + 1
            elif abs(diferença_x) >0:
                consumo = abs(diferença_x) * jogador.tesouros + 1

            jogo.tanques -= consumo #here
                
                

    
        
            


#aqui é a função mãe que incializa(dar a luz skkskss) a todo o jogo 
def inicializar(dimensao,dificuldade,tanques):
    jogo = Jogo(dimensao,tanques)
    for i in range(4):
        numero = i +1
        jogador = jogadores(numero)
        jogo.adicionar_jogador(jogador)      
    jogo.adicionar_tesouros()
    jogo.adicionar_bombas(dificuldade)
    return jogo        