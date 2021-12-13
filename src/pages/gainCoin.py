import sys

import pygame
from pygame.locals import *

pygame.init()  # Initialize all pygame's modules

font = pygame.font.SysFont(None, 90)

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

TRANSPARENT = (0, 0, 0, 0)

BACKGROUND = pygame.Color('#FEFAE0')
TEXT_COLOR = pygame.Color('#4D3F1B')
BOLD_COLOR = pygame.Color('#F9EED2')

FPS = 32
FPSCLOCK = pygame.time.Clock()

DISPLAY_SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

if __name__ == '__main__':
    pygame.display.set_caption('Gain coin')

    coin = int(sys.argv[1])
    userMoney = int(sys.argv[2])

    DISPLAY_SCREEN.fill(BACKGROUND)

    draw_text(f'Congratulation, you has gained {coin}$', pygame.font.SysFont(None, 30), TEXT_COLOR, DISPLAY_SCREEN, 100, 80)
    draw_text(f'Your current money: {userMoney}$', pygame.font.SysFont(None, 30), TEXT_COLOR, DISPLAY_SCREEN, 130, 190)
    # draw_text('', pygame.font.SysFont(None, 30), TEXT_COLOR, DISPLAY_SCREEN, 180, 120)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit(0)

        FPSCLOCK.tick(FPS)
        pygame.display.update()
