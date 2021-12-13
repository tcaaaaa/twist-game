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
    
def chooseFigure():
    buttonConfs = [
        {
            'isHover': False,
            'coords': (20, 200, 60, 60),
            'position': (20, 200),
            'image': pygame.transform.scale(pygame.image.load('../assets/p1.png').convert_alpha(), (60, 60))
        },
        {
            'isHover': False,
            'coords': (120, 200, 70, 60),
            'position': (120, 200),
            'image': pygame.transform.scale(pygame.image.load('../assets/p2.png').convert_alpha(), (60, 60))
        },
        {
            'isHover': False,
            'coords': (220, 200, 70, 60),
            'position': (220, 200),
            'image': pygame.transform.scale(pygame.image.load('../assets/p3.png').convert_alpha(), (60, 60))
        },
        {
            'isHover': False,
            'coords': (320, 200, 70, 60),
            'position': (320, 200),
            'image': pygame.transform.scale(pygame.image.load('../assets/p4.png').convert_alpha(), (60, 60))
        },
        {
            'isHover': False,
            'coords': (420, 200, 70, 60),
            'position': (420, 200),
            'image': pygame.transform.scale(pygame.image.load('../assets/p5.png').convert_alpha(), (60, 60))
        },
    ]

    choosingItem = -1

    while True:
        DISPLAY_SCREEN.fill(BACKGROUND)
        draw_text('Choose figure', pygame.font.SysFont(None, 30), TEXT_COLOR, DISPLAY_SCREEN, 180, 120)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and choosingItem != -1:
                    return choosingItem

        clientX, clientY = pygame.mouse.get_pos()

        choosingItem = -1
        for index, buttonConf in enumerate(buttonConfs):
            # if buttonConf['isHover']:
            #     buttonConf['rect'] = pygame.draw.rect(DISPLAY_SCREEN, BACKGROUND, buttonConf['coords'])
            # else: 
            buttonConf['rect'] = pygame.draw.rect(DISPLAY_SCREEN, BACKGROUND, buttonConf['coords'])
            DISPLAY_SCREEN.blit(buttonConf['image'], buttonConf['position'])
            if buttonConf['rect'].collidepoint((clientX, clientY)):
                buttonConf['isHover'] = True
                choosingItem = index
            else:
                buttonConf['isHover'] = False

        FPSCLOCK.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    pygame.display.set_caption('Choose figure')

    pygame.display.update()

    sys.exit(chooseFigure())