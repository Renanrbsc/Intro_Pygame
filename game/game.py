import pygame
from pygame.locals import *

# CONSTANTES
largura_tela = 900 # WIDTH X
altura_tela = 450  # HEIGHT Y
speed = 10

largura_ninja = 70 #x
altura_ninja = 90 #y


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


        # contador vinculado as imagens
        self.sequencia_image = 0

        # Conversao de image inicial
        self.image = pygame.image.load('Intro_pygame\game\\ninja run\\2d-game-sprite-6_001a.png').convert_alpha() 
        # self.image = pygame.transform.scale(self.image,(largura_ninja,altura_ninja)) # escalando dimensoes imagem x y
        self.rect = self.image.get_rect() 
        self.rect[0] = 100 # primeira posicao tupla posicionamento x
        self.rect[1] = altura_tela / 2 +100 # segunda posicao tupla posicionamento y
        print(self.rect)

    def update(self):
        self.sequencia_image = (self.sequencia_image + 1) % 4   #  % 4 zera o contador 
        self.image = self.images[self.sequencia_image]          #  e reseta a sequancia de image
       
        

pygame.init()
tela = pygame.display.set_mode((largura_tela,altura_tela)) #definindo janela e tamanho

plano_fundo = pygame.image.load('Intro_pygame\game\game_background_3\game_background_3.1.png') # load do plano de fundo
plano_fundo = pygame.transform.scale(plano_fundo,(largura_tela,altura_tela)) # escala plano para tamanho da tela

ninja_grupo = pygame.sprite.Group() # grupo de objetos do mesmo tipo
ninja = Ninja() # variavel que recebe a classe/objeto
ninja_grupo.add(ninja) # adicionando o objeto no grupo 

fps = pygame.time.Clock() # atribui uma variavel para limitar fps

while True: # loop principal do game

    fps.tick(10) # chama metodo limitar FPS 
     
    for event in pygame.event.get(): # evento de sair da janela
        if event.type == QUIT:
            pygame.quit()

    tela.blit(plano_fundo,(0,0)) # coloca plano de fundo na posicao x y

    ninja_grupo.update() # atualizaçao de frames do grupo de objetos 'Ninja'

    ninja_grupo.draw(tela) # desenhando o grupo de objetos 'Ninja'
        
    pygame.display.update() # atualizacao do janela de game


    
