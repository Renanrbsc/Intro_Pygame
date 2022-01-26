from pygame import Color
from PongGame.objects.draw import draw_retangule


class Player:
    def __init__(self, display, screen, direction: str, name: str, speed: int) -> None:
        self.screen = screen
        self.display = display  
        
        self.WIDTH = 20
        self.HEIGHT = self.WIDTH * 5
        self.Y_PLAYER = self.screen.HEIGHT / 2 - self.HEIGHT / 2
        self.set_coordenate(direction)
        self.Y_SPEED = speed
        self.name = name
        self.score = 0

    def set_coordenate(self, direction: str):
        if direction == "right":
            self.X_PLAYER = self.screen.right - self.WIDTH
            self.COLOR = Color("Blue")

        elif direction == "left":
            self.X_PLAYER = self.screen.left
            self.COLOR = Color("Red")

    def set_score(self):
        self.score = self.score + 1

    def create(self):
        draw_retangule(self.display, self.X_PLAYER, self.Y_PLAYER, 
                       self.WIDTH, self.HEIGHT, self.COLOR)
