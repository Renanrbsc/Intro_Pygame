import pygame
from pygame.locals import *

class Background(pygame.sprite.Sprite):

    def __init__(self,camada,SPEED,largura_tela,camada_altura,xpos):
        pygame.sprite.Sprite.__init__(self) # construtor do pygame // inicializa a classe

        # inicializaçao de variaveis
        self.speed = SPEED

        # Conversao de image inicial
        self.image = pygame.image.load(f'{camada}').convert_alpha() 
        self.image = pygame.transform.scale(self.image,(largura_tela,camada_altura)) # escala plano para tamanho da tela
        self.rect = self.image.get_rect() 

        self.rect[0] = 0 # primeira posicao tupla posicionamento x
        self.rect[0] = xpos
        self.rect[1] = 0 # segunda posicao tupla posicionamento y

    def set_largura(self,camada_largura):
        camada_largura - 15
        return

    def movimentacao_sprite(self):
        self.rect[0] -= (10 - self.speed)  # movimenta camada1 a esquerda
        

    def update(self):
        self.movimentacao_sprite() # atualiza movimento linear do sprite