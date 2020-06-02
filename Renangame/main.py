import pygame
from pygame.locals import *

# CONSTANTES
largura_tela = 900  # WIDTH X
altura_tela = 450  # HEIGHT Y
PULO = 10
SPEED = 5  # constante de velocidade cenario e personagem
gravidade = 10

camada_largura = largura_tela
camada_altura = altura_tela


class Ninja(pygame.sprite.Sprite):  # modela um objeto do mundo real
    # atribui variaveis para atributos e funcoes para comportamento

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # construtor do pygame // inicializa a classe

        # lista de imagens
        self.images = [pygame.image.load(r'ninja\2d-game-sprite-6_001a.png').convert_alpha(),
                       pygame.image.load(r'ninja\2d-game-sprite-6_001a.png').convert_alpha(),
                       pygame.image.load(r'ninja\2d-game-sprite-6_002a.png').convert_alpha(),
                       pygame.image.load(r'ninja\2d-game-sprite-6_002a.png').convert_alpha(),
                       pygame.image.load(r'ninja\2d-game-sprite-6_003a.png').convert_alpha(),
                       pygame.image.load(r'ninja\2d-game-sprite-6_003a.png').convert_alpha(),
                       pygame.image.load(r'ninja\2d-game-sprite-6_004a.png').convert_alpha(),
                       pygame.image.load(r'ninja\2d-game-sprite-6_004a.png').convert_alpha(),
                       ]

        # Variaveis da Classe Ninja
        self.pulo = PULO
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.velocidade = SPEED
        self.gravidade = gravidade

        # contador vinculado as imagens
        self.sequencia_image = 0

        # Conversao de image inicial
        self.image = pygame.image.load(r'ninja\2d-game-sprite-6_001a.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 100  # primeira posicao tupla posicionamento x
        self.rect[1] = 315  # segunda posicao tupla posicionamento y

    def pular(self):  # move personagem no eixo y
        for i in range(self.pulo):  # loop na quantidade de pixels
            self.rect[1] -= gravidade / 5  # valor de pulo em relacao a metade da gravidade em 'loop'
            if self.rect[1] < -50:  # limitador de movimento Y
                self.rect[1] += self.pulo

    def direita(self):  # move personagem no eixo x
        self.rect[0] += self.velocidade
        if self.rect[0] > 830:  # limitador de movimento X
            self.rect[0] -= self.velocidade

    def esquerda(self):  # move personagem no eixo x
        self.rect[0] -= self.velocidade
        if self.rect[0] < 20:  # limitador de movimento X
            self.rect[0] += self.velocidade

    def gravidade_sprite(self):
        self.rect[1] += self.gravidade  # atualizacao de gravidade eixo y do personagem
        if self.rect[1] == 325:  # limitador para personagem permanecer na tela
            self.rect[1] -= self.gravidade  # anula gravidade no eixo y '325'

    def animacao_sprite(self):
        self.sequencia_image = (self.sequencia_image + 1) % 8  # % 4 zera o contador
        self.image = self.images[self.sequencia_image]  # e reseta a sequancia de image

    def update(self):
        self.animacao_sprite()
        self.gravidade_sprite()  # chamando metodo de gravidade para atualizaçao


class Camada1(pygame.sprite.Sprite):

    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)  # construtor do pygame // inicializa a classe

        # inicializaçao de variaveis
        self.speed = SPEED

        # Conversao de image inicial
        self.image = pygame.image.load(r'layers\ground_3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            (largura_tela, camada_altura))  # escala plano para tamanho da tela
        self.rect = self.image.get_rect()

        self.rect[0] = 0  # primeira posicao tupla posicionamento x
        self.rect[0] = xpos
        self.rect[1] = 0  # segunda posicao tupla posicionamento y

    def movimentacao_sprite(self):
        self.rect[0] -= (10 - self.speed)  # movimenta camada1 a esquerda

    def update(self):
        self.movimentacao_sprite()  # atualiza movimento linear do sprite


class Camada2(pygame.sprite.Sprite):

    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)  # construtor do pygame // inicializa a classe

        # inicializaçao de variaveis
        self.speed = SPEED

        # Conversao de image inicial
        self.image = pygame.image.load(r'layers\ground_2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            (largura_tela, camada_altura))  # escala plano para tamanho da tela
        self.rect = self.image.get_rect()

        self.rect[0] = 0  # primeira posicao tupla posicionamento x
        self.rect[0] = xpos
        self.rect[1] = 0  # segunda posicao tupla posicionamento y

    def movimentacao_sprite(self):
        self.rect[0] -= (7 - self.speed)  # movimenta camada1 a esquerda

    def update(self):
        self.movimentacao_sprite()  # atualiza movimento linear do sprite


class Camada3(pygame.sprite.Sprite):

    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)  # construtor do pygame // inicializa a classe

        # inicializaçao de variaveis
        self.speed = SPEED

        # Conversao de image inicial
        self.image = pygame.image.load(r'layers\ground_3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            (largura_tela, camada_altura))  # escala plano para tamanho da tela
        self.rect = self.image.get_rect()

        self.rect[0] = 0  # primeira posicao tupla posicionamento x
        self.rect[0] = xpos
        self.rect[1] = 0  # segunda posicao tupla posicionamento y

    def movimentacao_sprite(self):
        self.rect[0] -= (6 - self.speed)  # movimenta camada1 a esquerda

    def update(self):
        self.movimentacao_sprite()  # atualiza movimento linear do sprite


def esta_fora_tela(sprite):  # funcao para verificar se há camada fora da tela
    return sprite.rect[0] < -(sprite.rect[2])  # pega x atual do sprite - sua largura real


pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))  # definindo janela e tamanho

plano_fundo = pygame.image.load(r'game_background_3\game_background_3.1.png')  # load do plano de fundo
plano_fundo = pygame.transform.scale(plano_fundo, (largura_tela, altura_tela))  # escala plano para tamanho da tela

camada1_grupo = pygame.sprite.Group()  # grupo de objetos do mesmo tipo
camada2_grupo = pygame.sprite.Group()  # grupo de objetos do mesmo tipo
camada3_grupo = pygame.sprite.Group()  # grupo de objetos do mesmo tipo

for i in range(2):  # cria duas camada / uma apos outra iniciais
    camada1 = Camada1(largura_tela * i)  # variavel que recebe a classe/objeto 
    camada2 = Camada2(largura_tela * i)  # variavel que recebe a classe/objeto 
    camada3 = Camada3(largura_tela * i)  # variavel que recebe a classe/objeto 

    camada1_grupo.add(camada1)  # adicionando o objeto no grupo
    camada2_grupo.add(camada2)  # adicionando o objeto no grupo
    camada3_grupo.add(camada3)  # adicionando o objeto no grupo

ninja_grupo = pygame.sprite.Group()  # grupo de objetos do mesmo tipo
ninja = Ninja()  # variavel que recebe a classe/objeto
ninja_grupo.add(ninja)  # adicionando o objeto no grupo

fps = pygame.time.Clock()  # atribui uma variavel para limitar fps

while True:  # loop principal do game

    fps.tick(25)  # chama metodo limitar FPS

    for event in pygame.event.get():  # verifica evento de janela
        if event.type == QUIT:  # verifica evento sair
            pygame.quit()

    if event.type == KEYDOWN:  # verifica teclado
        if event.key == K_UP:  # verifica pulo
            ninja.pular()

        if event.key == K_LEFT:  # verifica esquerda
            ninja.esquerda()

        if event.key == K_RIGHT:  # verifica direita
            ninja.direita()

    tela.blit(plano_fundo, (0, 0))  # coloca plano de fundo na posicao x y

    if esta_fora_tela(camada1_grupo.sprites()[0]):  # chama funcao e verifica se a camada esta negativa ao x inicial
        camada1_grupo.remove(camada1_grupo.sprites()[0])  # remove a camada negativa q saiu da tela

        nova_camada1 = Camada1(camada_largura - 15)  # cria nova camada e posiciona -15 pixel do original
        camada1_grupo.add(nova_camada1)  # adiciona ao grupo de camada para update

    if esta_fora_tela(camada1_grupo.sprites()[0]):
        camada2_grupo.remove(camada2_grupo.sprites()[0])

        nova_camada2 = Camada2(camada_largura - 15)  # cria nova camada e posiciona -15 pixel do original
        camada2_grupo.add(nova_camada2)

    if esta_fora_tela(camada3_grupo.sprites()[0]):
        camada3_grupo.remove(camada2_grupo.sprites()[0])

        nova_camada3 = Camada3(camada_largura - 15)  # cria nova camada e posiciona -15 pixel do original
        camada3_grupo.add(nova_camada3)

    camada3_grupo.update()
    camada2_grupo.update()
    camada1_grupo.update()

    ninja_grupo.update()  # atualizaçao de frames do grupo de objetos 'Ninja'

    camada3_grupo.draw(tela)
    camada2_grupo.draw(tela)
    camada1_grupo.draw(tela)

    ninja_grupo.draw(tela)  # desenhando o grupo de objetos 'Ninja'

    pygame.display.update()  # atualizacao do janela de game
