import sys

import pygame
from pygame.locals import *

pygame.init()  # Initialize all pygame's modules

font = pygame.font.SysFont(None, 90)

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

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

def chooseMoney():
    buttonConfs = [
        {
            'isHover': False,
            'coords': (60, 200, 60, 60),
            'position': (80, 220),
            'text': '50',
        },
        {
            'isHover': False,
            'coords': (160, 200, 70, 60),
            'position': (180, 220),
            'text': '100'
        },
        {
            'isHover': False,
            'coords': (260, 200, 70, 60),
            'position': (280, 220),
            'text': '150'
        },
        {
            'isHover': False,
            'coords': (360, 200, 70, 60),
            'position': (380, 220),
            'text': '250'
        },
    ]

    choosingItem = 0

    while True:
        DISPLAY_SCREEN.fill(BACKGROUND)
        draw_text('Choose betting money', pygame.font.SysFont(None, 30), TEXT_COLOR, DISPLAY_SCREEN, 140, 120)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and choosingItem != 0:
                    return choosingItem
                    # sys.exit(choosingItem)

        clientX, clientY = pygame.mouse.get_pos()

        choosingItem = 0
        for buttonConf in buttonConfs:
            if buttonConf['isHover']:
                buttonConf['rect'] = pygame.draw.rect(DISPLAY_SCREEN, TEXT_COLOR, buttonConf['coords'])
                draw_text(buttonConf['text'], pygame.font.SysFont(None, 30), BOLD_COLOR, DISPLAY_SCREEN, *buttonConf['position'])
            else: 
                buttonConf['rect'] = pygame.draw.rect(DISPLAY_SCREEN, BOLD_COLOR, buttonConf['coords'])
                draw_text(buttonConf['text'], pygame.font.SysFont(None, 30), TEXT_COLOR, DISPLAY_SCREEN, *buttonConf['position'])
            if buttonConf['rect'].collidepoint((clientX, clientY)):
                buttonConf['isHover'] = True
                choosingItem = int(buttonConf['text'])
            else:
                buttonConf['isHover'] = False

        FPSCLOCK.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    pygame.display.set_caption('Choose money')

    pygame.display.update()

    sys.exit(chooseMoney())