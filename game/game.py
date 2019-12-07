import pygame
from pygame.locals import *

# CONSTANTES
largura_tela = 850
altura_tela = 500
speed = 10

class Ninja(pygame.sprite.Sprite): # modela um objeto do mundo real
                                   # atribui variaveis para atributos e funcoes para comportamento

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.load('ninja run\2d-game-sprite-6_001.png').convert_alpha()
        self.rect = self.image.get_rect()



        self.plano_fundo = pygame.image.load('Intro_pygame\game\RvaMB7.png')
        self.plano_fundo = pygame.transform.scale(plano_fundo,(largura_tela,altura_tela))    
        self.rect = self.image.get_rect()
        print(self.rect)

    def update(self):
        pass
        

pygame.init()
tela = pygame.display.set_mode((largura_tela,altura_tela))

plano_fundo = pygame.image.load('Intro_pygame\game\RvaMB7.png')
plano_fundo = pygame.transform.scale(plano_fundo,(largura_tela,altura_tela)) 

ninja_grupo = pygame.sprite.Group() # grupo de objetos do mesmo tipo
ninja = Ninja() # variavel que recebe a classe/objeto
ninja_grupo.append(ninja) # adicionando o objeto no grupo 


while True:
     

    tela.blit(plano_fundo,(0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    ninja_grupo.update()

    ninja_grupo.draw(tela)
        
    pygame.display.update()

    
