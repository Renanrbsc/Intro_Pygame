import pygame


def draw_retangule(display, x: int, y: int,
                   width: int, height: int, color: pygame.Color):
    
    x, y = round(x), round(y)
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(display, color, rect)


def draw_score(display, player1, player2, screen):
    font = pygame.font.Font(None, 50)

    score_p1 = f"{player1.name}: {str(player1.score)}"
    score_p2 = f"{player2.name}: {str(player2.score)}"

    text1 = font.render(f"{score_p1}",
                        True, pygame.Color("Red"), None)

    text2 = font.render(f"{score_p2}",
                        True, pygame.Color("Blue"), None)

    x1 = round(screen.x_center - screen.x_center * 0.7)
    y1 = round(screen.y_center - screen.y_center * 0.8)
    text_rect1 = text1.get_rect(center=(x1, y1))

    x2 = round(screen.x_center + screen.x_center * 0.7)
    y2 = round(screen.y_center - screen.y_center * 0.8)
    text_rect2 = text2.get_rect(center=(x2, y2))

    display.blit(text1, text_rect1)
    display.blit(text2, text_rect2)

