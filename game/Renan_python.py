import pygame
from pygame.locals import *

# CONSTANTES
largura_tela = 900 # WIDTH X
altura_tela = 450  # HEIGHT Y
PULO = 20
SPEED= 15
gravidade = 10

class Ninja(pygame.sprite.Sprite): # modela um objeto do mundo real
                                   # atribui variaveis para atributos e funcoes para comportamento

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # construtor do pygame // inicializa a classe

        # lista de imagens
        self.images = [pygame.image.load('Intro_pygame\game\\ninja run\\2d-game-sprite-6_001a.png').convert_alpha(),
                       pygame.image.load('Intro_pygame\game\\ninja run\\2d-game-sprite-6_002a.png').convert_alpha(),
                       pygame.image.load('Intro_pygame\game\\ninja run\\2d-game-sprite-6_003a.png').convert_alpha(),
                       pygame.image.load('Intro_pygame\game\\ninja run\\2d-game-sprite-6_004a.png').convert_alpha(),
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
        self.image = pygame.image.load('Intro_pygame\game\\ninja run\\2d-game-sprite-6_001a.png').convert_alpha() 
        self.rect = self.image.get_rect() 
        self.rect[0] = 100 # primeira posicao tupla posicionamento x
        self.rect[1] = 315 # segunda posicao tupla posicionamento y
               
    def pular(self):     # move personagem no eixo y
        for i in range(self.pulo): # loop na quantidade de pixels
            self.rect[1] -= gravidade/5 # valor de pulo em relacao a metade da gravidade em 'loop'
            if  self.rect[1] < -50: #limitador de movimento Y
                self.rect[1] += self.pulo

    def direita(self):   # move personagem no eixo x
        self.rect[0] += self.velocidade
        if self.rect[0] > 830: #limitador de movimento X
            self.rect[0] -= self.velocidade
    
    def esquerda(self):  # move personagem no eixo x
        self.rect[0] -= self.velocidade
        if self.rect[0] < 20: #limitador de movimento X
            self.rect[0] += self.velocidade

    def gravidade_ninja(self):    
        self.rect[1] += self.gravidade # atualizacao de gravidade eixo y do personagem
        if self.rect[1] == 325: # limitador para personagem permanecer na tela
            self.rect[1] -= self.gravidade # anula gravidade no eixo y '325'
        
    def update(self):
        self.sequencia_image = (self.sequencia_image + 1) % 4   #  % 4 zera o contador 
        self.image = self.images[self.sequencia_image]          #  e reseta a sequancia de image
        self.gravidade_ninja() # chamando metodo de gravidade para atualizaçao
        
pygame.init()
tela = pygame.display.set_mode((largura_tela,altura_tela)) #definindo janela e tamanho

plano_fundo = pygame.image.load('Intro_pygame\game\game_background_3\game_background_3.1.png') # load do plano de fundo
plano_fundo = pygame.transform.scale(plano_fundo,(largura_tela,altura_tela)) # escala plano para tamanho da tela

ninja_grupo = pygame.sprite.Group() # grupo de objetos do mesmo tipo
ninja = Ninja() # variavel que recebe a classe/objeto
ninja_grupo.add(ninja) # adicionando o objeto no grupo 

fps = pygame.time.Clock() # atribui uma variavel para limitar fps

while True: # loop principal do game

    fps.tick(20) # chama metodo limitar FPS 
     
    for event in pygame.event.get(): # verifica evento de janela
        if event.type == QUIT: #verifica evento sair
            pygame.quit()
       
    if event.type == KEYDOWN: #verifica teclado
        if event.key == K_UP: #verifica pulo
                ninja.pular()
           
        if event.key == K_LEFT: #verifica esquerda
            ninja.esquerda()
                # if event.key == K_LEFT:   # funcao para inverter imagem ao mudar lado
                #     ninja.image = pygame.transform.flip(ninja.image,True,False)
                # else:
                #     ninja.image = pygame.transform.flip(ninja.image,False,False)
       
        if event.key == K_RIGHT: #verifica direita
            ninja.direita()

    tela.blit(plano_fundo,(0,0)) # coloca plano de fundo na posicao x y

    ninja_grupo.update() # atualizaçao de frames do grupo de objetos 'Ninja'

    ninja_grupo.draw(tela) # desenhando o grupo de objetos 'Ninja'
        
    pygame.display.update() # atualizacao do janela de game


    
