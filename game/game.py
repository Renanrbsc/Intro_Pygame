import pygame

largura_tela = 850
altura_tela = 500

pygame.init()
tela = pygame.display.set_mode((largura_tela,altura_tela))


plano_fundo = pygame.image.load('Intro_pygame\game\RvaMB7.png')
plano_fundo = pygame.transform.scale(plano_fundo,(largura_tela,altura_tela))


while True:
     
        
    tela.blit(plano_fundo,(0,0))
        
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

