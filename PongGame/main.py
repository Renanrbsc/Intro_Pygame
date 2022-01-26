import pygame
from pygame.locals import *

from PongGame.objects.screen import Screen
from PongGame.objects.pong import Pong
from PongGame.objects.player import Player
from PongGame.objects.draw import draw_score

screen = Screen()

pygame.init()
display = pygame.display.set_mode((screen.WIDTH, screen.HEIGHT), 1)
fps = pygame.time.Clock()

pong = Pong(display, screen, speed=8)
player1 = Player(display, screen, direction="right", name="Player1", speed=10)
player2 = Player(display, screen, direction="left", name="Player2", speed=10)


def on_draw_frame():

    display.fill((0, 0, 0))

    pong.create()
    player1.create()
    player2.create()

    draw_score(display, player1, player2, screen)

    pygame.display.flip()


def on_update_frame():

    pong.X_PONG = pong.X_PONG + pong.X_SPEED
    pong.Y_PONG = pong.Y_PONG + pong.Y_SPEED

    if (pong.X_PONG + pong.WIDTH > player1.X_PLAYER) \
            and (pong.Y_PONG + pong.HEIGHT > player1.Y_PLAYER) \
            and (pong.Y_PONG < player1.Y_PLAYER + player1.HEIGHT):
        pong.X_SPEED = -pong.X_SPEED
    if (pong.X_PONG < player2.X_PLAYER + player2.WIDTH) \
            and (pong.Y_PONG + pong.HEIGHT > player2.Y_PLAYER) \
            and (pong.Y_PONG < player2.Y_PLAYER + player2.HEIGHT):
        pong.X_SPEED = -pong.X_SPEED

    if pong.Y_PONG + pong.HEIGHT > screen.top:
        pong.Y_SPEED = -pong.Y_SPEED
    if pong.Y_PONG < screen.bottom:
        pong.Y_SPEED = -pong.Y_SPEED

    if pong.X_PONG + pong.WIDTH > screen.right:
        pong.set_cood_center()
        player1.set_score()

    if pong.X_PONG < screen.left:
        pong.set_cood_center()
        player2.set_score()

    if player1.Y_PLAYER + player1.HEIGHT > screen.top:
        player1.Y_PLAYER = player1.Y_PLAYER - player1.Y_SPEED
    if player1.Y_PLAYER < screen.bottom:
        player1.Y_PLAYER = player1.Y_PLAYER + player1.Y_SPEED

    if player2.Y_PLAYER + player2.HEIGHT > screen.top:
        player2.Y_PLAYER = player2.Y_PLAYER - player1.Y_SPEED
    if player2.Y_PLAYER < screen.bottom:
        player2.Y_PLAYER = player2.Y_PLAYER + player1.Y_SPEED

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player1.Y_PLAYER = player1.Y_PLAYER - player1.Y_SPEED
    if keys[K_DOWN]:
        player1.Y_PLAYER = player1.Y_PLAYER + player1.Y_SPEED
    if keys[K_w]:
        player2.Y_PLAYER = player2.Y_PLAYER - player1.Y_SPEED
    if keys[K_s]:
        player2.Y_PLAYER = player2.Y_PLAYER + player1.Y_SPEED


while True:
    on_draw_frame()
    on_update_frame()
    pygame.event.pump()
    fps.tick(60)
