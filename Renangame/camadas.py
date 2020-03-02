  
class Camada1(pygame.sprite.Sprite):

    def __init__(self,xpos):
        pygame.sprite.Sprite.__init__(self) # construtor do pygame // inicializa a classe

        # inicializaçao de variaveis
        self.speed = SPEED

        # Conversao de image inicial
        self.image = pygame.image.load('Renangame\layers\ground_3.png').convert_alpha() 
        self.image = pygame.transform.scale(self.image,(largura_tela,camada_altura)) # escala plano para tamanho da tela
        self.rect = self.image.get_rect() 

        self.rect[0] = 0 # primeira posicao tupla posicionamento x
        self.rect[0] = xpos
        self.rect[1] = 0 # segunda posicao tupla posicionamento y

    def movimentacao_sprite(self):
        self.rect[0] -= (10 - self.speed)  # movimenta camada1 a esquerda
        

    def update(self):
        self.movimentacao_sprite() # atualiza movimento linear do sprite

class Camada2(pygame.sprite.Sprite):

    def __init__(self,xpos):
        pygame.sprite.Sprite.__init__(self) # construtor do pygame // inicializa a classe

        # inicializaçao de variaveis
        self.speed = SPEED

        # Conversao de image inicial
        self.image = pygame.image.load('Renangame\layers\ground_2.png').convert_alpha() 
        self.image = pygame.transform.scale(self.image,(largura_tela,camada_altura)) # escala plano para tamanho da tela
        self.rect = self.image.get_rect() 

        self.rect[0] = 0 # primeira posicao tupla posicionamento x
        self.rect[0] = xpos
        self.rect[1] = 0 # segunda posicao tupla posicionamento y

    def movimentacao_sprite(self):
        self.rect[0] -= (7 - self.speed)  # movimenta camada1 a esquerda
        

    def update(self):
        self.movimentacao_sprite() # atualiza movimento linear do sprite

class Camada3(pygame.sprite.Sprite):

    def __init__(self,xpos):
        pygame.sprite.Sprite.__init__(self) # construtor do pygame // inicializa a classe

        # inicializaçao de variaveis
        self.speed = SPEED

        # Conversao de image inicial
        self.image = pygame.image.load('Renangame\layers\ground_3.png').convert_alpha() 
        self.image = pygame.transform.scale(self.image,(largura_tela,camada_altura)) # escala plano para tamanho da tela
        self.rect = self.image.get_rect() 

        self.rect[0] = 0 # primeira posicao tupla posicionamento x
        self.rect[0] = xpos
        self.rect[1] = 0 # segunda posicao tupla posicionamento y

    def movimentacao_sprite(self):
        self.rect[0] -= (6 - self.speed)  # movimenta camada1 a esquerda
        

    def update(self):
        self.movimentacao_sprite() # atualiza movimento linear do sprite


def esta_fora_tela(sprite): # funcao para verificar se há camada fora da tela
    return sprite.rect[0] < -(sprite.rect[2]) # pega x atual do sprite - sua largura real
