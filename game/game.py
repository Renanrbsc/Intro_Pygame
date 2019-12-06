import pygame

largura_tela = 850
altura_tela = 500
speed = 10
pygame.init()
tela = pygame.display.set_mode((largura_tela,altura_tela))




class move(pygame.sprite.Sprite):

    def __init__(self,largura_tela,altura_tela):

        self.plano_fundo = pygame.image.load('Intro_pygame\game\RvaMB7.png')
        self.plano_fundo = pygame.transform.scale(plano_fundo,(largura_tela,altura_tela))    
        self.rect = self.image.get_rect()

    def update():
        self.rect[0] -= speed

while True:
     
    move_move = pygame.sprite.Group()
    move = move(largura_tela, 100)
    move_move.append(move)
    
    # tela.blit(plano_fundo,(0,0))
        
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

