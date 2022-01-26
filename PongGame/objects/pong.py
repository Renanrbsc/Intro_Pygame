from pygame import Color
from PongGame.objects.draw import draw_retangule
from PongGame.objects.screen import Screen


class Pong(Screen):
    def __init__(self, display, screen, speed: int) -> None:
        self.screen = screen
        self.display = display
        self.set_cood_center()
        self.WIDTH = 20
        self.HEIGHT = 20
        self.X_SPEED = speed
        self.Y_SPEED = speed
        self.COLOR = Color("White")
    
    def set_cood_center(self):
        self.X_PONG = self.screen.x_center
        self.Y_PONG = self.screen.y_center

    def create(self):
        draw_retangule(self.display, self.X_PONG, self.Y_PONG, 
                       self.WIDTH, self.HEIGHT, self.COLOR)


