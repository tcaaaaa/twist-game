import random
import array as arr
from array import array
from typing import Union, Any
import os

import pygame, sys
from pygame.locals import *

import subprocess

pygame.init()
fpsClock = pygame.time.Clock()

userMoney = 100

# SET UP SCREEN MENU----------------------------------------------------------------------------------#
WINDOWWIDTH = 1024
WINDOWHEIGHT = 682

BACKGROUND_2 = pygame.image.load('../assets/Fairy Forest.jpg')

DISPLAYSCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Twist Game')

# COLOR-----------------------------------------------------------------------------------------------#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# TEXT DESIGN-----------------------------------------------------------------------------------------#
font_1 = pygame.font.SysFont(None, 60)

def draw_text_1(text, font_1, color, surface, x, y):
    textobj = font_1.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#--------------------------------------------------#

font_2 = pygame.font.SysFont(None, 140)

def draw_text_2(text, font_2, color, surface, x, y):
    textobj = font_2.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# START MENU------------------------------------------------------------------------------------------#

# ICON------------------------------------------------------------------#
icon = pygame.image.load('../assets/Icon.png')

# DEF-------------------------------------------------------------------#
click = False

def main_menu_start():
    click = False
    while True:
        DISPLAYSCREEN.fill(WHITE)

        DISPLAYSCREEN.blit(icon, (387, 50))
        draw_text_2('Twist', font_2, BLACK, DISPLAYSCREEN, 110, 125)
        draw_text_2('Game', font_2, BLACK, DISPLAYSCREEN, 665, 125)

        button_start = draw_text_1('Start', font_1, BLACK, DISPLAYSCREEN, 465, 365)
        button_rect_1 = pygame.draw.rect(DISPLAYSCREEN, WHITE, (420, 315, 200, 100), 1)

        button_exit = draw_text_1('Exit', font_1, BLACK, DISPLAYSCREEN, 475, 500)
        button_rect_2 = pygame.draw.rect(DISPLAYSCREEN, WHITE, (420, 465, 200, 100), 1)

        mx, my = pygame.mouse.get_pos()

        if button_rect_1.collidepoint((mx, my)):
            if click == True:
                main_menu()

        if button_rect_2.collidepoint((mx, my)):
            if click == True:
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = True

        pygame.display.update()
        fpsClock.tick(60)


# FUNCTION MENU---------------------------------------------------------------------------------------#

# TEXT DESIGN-----------------------------------------------------------#
font_3 = pygame.font.SysFont(None, 90)

def draw_text_3(text, font_3, color, surface, x, y):
    textobj = font_3.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# FUNCTION IMAGES-------------------------------------------------------#
icon_back = pygame.image.load('../assets/back_button_1.png')

img_shop = pygame.image.load('../assets/mushroom shop.png')
img_play = pygame.image.load('../assets/mushroom party.png')
img_mini_game = pygame.image.load('../assets/mushroom fight.png')
img_options = pygame.image.load('../assets/mushroom options.png')

click = False

# SETTING---------------------------------------------------------------#
setting_play = False
setting_mini = False
setting_shop = False
setting_opts = False

# ENTER-----------------------------------------------------------------#
enter_play = False
enter_mini = False
enter_shop = False
enter_opts = False


def main_menu():
    userMoney = 100
    running = True
    click = False

    # SETTING---------------------------------------------------------------#
    setting_play = False
    setting_mini = False
    setting_shop = False
    setting_opts = False

    # ENTER-----------------------------------------------------------------#
    enter_play = False
    enter_mini = False
    enter_shop = False
    enter_opts = False

    while running:
        # POSITION--------------------------------------------------------------#
        shape_play = pygame.draw.rect(DISPLAYSCREEN, WHITE, (100, 110, 380, 240), 3)
        shape_mini = pygame.draw.rect(DISPLAYSCREEN, WHITE, (530, 110, 380, 240), 3)
        shape_shop = pygame.draw.rect(DISPLAYSCREEN, WHITE, (100, 385, 380, 240), 3)
        shape_opts = pygame.draw.rect(DISPLAYSCREEN, WHITE, (530, 385, 380, 240), 3)

        DISPLAYSCREEN.blit(BACKGROUND_2, (0, 0))

        # BUTTON----------------------------------------------------------------#

        mx, my = pygame.mouse.get_pos()

        # Play button---------------------------------------------------#
        DISPLAYSCREEN.blit(img_play, (155, 115))
        draw_text_3('PvE', font_3, WHITE, DISPLAYSCREEN, 230, 275)

        if shape_play.collidepoint((mx, my)):
            setting_play = True
            setting_mini = False
            setting_shop = False
            setting_opts = False

            if enter_play == True:
                money = subprocess.call(['python', 'pages/chooseMoney.py'])
                print(money)
                bettingFigure = subprocess.call(['python', 'pages/chooseFigure.py'])
                userMoney = GamePlay(userMoney, money, bettingFigure)
                print(userMoney)

        # Mini game button----------------------------------------------#
        DISPLAYSCREEN.blit(img_mini_game, (630, 125))
        draw_text_3('Miniplay', font_3, WHITE, DISPLAYSCREEN, 600, 275)

        if shape_mini.collidepoint((mx, my)):
            setting_mini = True
            setting_play = False
            setting_shop = False
            setting_opts = False

            if enter_mini:
                score = subprocess.call(['python', 'experiment.py'])
                userMoney += score
                subprocess.call(['python', 'pages/gainCoin.py', str(score), str(userMoney)])

        # Shop button---------------------------------------------------#
        DISPLAYSCREEN.blit(img_shop, (175, 370))
        draw_text_3('Shop', font_3, WHITE, DISPLAYSCREEN, 210, 550)

        if shape_shop.collidepoint((mx, my)):
            setting_shop = True
            setting_play = False
            setting_mini = False
            setting_opts = False

            if enter_shop == True:
                shop()

        # Options button------------------------------------------------#
        DISPLAYSCREEN.blit(img_options, (580, 390))
        draw_text_3('Option', font_3, WHITE, DISPLAYSCREEN, 620, 550)

        if shape_opts.collidepoint((mx, my)):
            setting_opts = True
            setting_play = False
            setting_mini = False
            setting_shop = False

        button_1_1 = DISPLAYSCREEN.blit(icon_back, (10, 10))

        if button_1_1.collidepoint((mx, my)):
            if click == True:
                running = False

        # DRAW BUTTON----------------------------------------------------#
        if setting_play == True:
            pygame.draw.rect(DISPLAYSCREEN, WHITE, (100, 110, 380, 240), 3)

        if setting_mini == True:
            pygame.draw.rect(DISPLAYSCREEN, WHITE, (530, 110, 380, 240), 3)

        if setting_shop == True:
            pygame.draw.rect(DISPLAYSCREEN, WHITE, (100, 385, 380, 240), 3)

        if setting_opts == True:
            pygame.draw.rect(DISPLAYSCREEN, WHITE, (530, 385, 380, 240), 3)

        click = False

        # ENTER-----------------------------------------------------------------#
        enter_play = False
        enter_mini = False
        enter_shop = False
        enter_opts = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    enter_play = True
                    enter_mini = True
                    enter_shop = True
                    enter_opts = True



        pygame.display.update()
        fpsClock.tick(60)


# SHOP------------------------------------------------------------------------------------------------#

# FUNCTION IMAGES-------------------------------------------------------#
img_back = pygame.image.load('../assets/back_button.png')
# img_coin = pygame.image.load('../assets/coin_Twist_Game.png')
img_frame = pygame.image.load('../assets/wood frame.png')

img_shop_background = pygame.image.load('../assets/mushroom board.png')

def shop():
    click = False
    running = True
    while running:

        DISPLAYSCREEN.blit(img_shop_background, (0,0))
        DISPLAYSCREEN.blit(img_frame, (700,10))

        mx, my = pygame.mouse.get_pos()


        button_1_1 = DISPLAYSCREEN.blit(img_back, (10,10))

        if button_1_1.collidepoint((mx,my)):
            if click == True:
                running = False

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        fpsClock.tick(60)

# GAME------------------------------------------------------------------------------------------------#

# X,Y POS---------------------------------------------------------------#
x = [10, 10, 10, 10, 10]
y = arr.array('f', [100, 200, 300, 400, 500])

# IMG IN GAME-----------------------------------------------------------#
img_p1 = pygame.image.load('../assets/p1.png').convert_alpha()
img_p2 = pygame.image.load('../assets/p2.png').convert_alpha()
img_p3 = pygame.image.load('../assets/p3.png').convert_alpha()
img_p4 = pygame.image.load('../assets/p4.png').convert_alpha()
img_p5 = pygame.image.load('../assets/p5.png').convert_alpha()

getx = 850
winner = 0

# TEXT DESIGN-----------------------------------------------------------#
font_3 = pygame.font.SysFont(None, 90)

def draw_text_3(text, font_3, color, surface, x, y):
    textobj = font_3.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

background = pygame.image.load('../assets/pinky_background.png')
finish = pygame.image.load('../assets/race_road.png')

# GAMEPLAY--------------------------------------------------------------------------------------------#
running = True
def GamePlay(userMoney, money, bettingFigure):
    while True:
        running = True
        DISPLAYSCREEN.blit(background, (0, 0))

        pygame.draw.line(DISPLAYSCREEN, RED, (15, 100), (950, 100), 1)
        pygame.draw.line(DISPLAYSCREEN, RED, (15, 200), (950, 200), 1)
        pygame.draw.line(DISPLAYSCREEN, RED, (15, 300), (950, 300), 1)
        pygame.draw.line(DISPLAYSCREEN, RED, (15, 400), (950, 400), 1)
        pygame.draw.line(DISPLAYSCREEN, RED, (15, 500), (950, 500), 1)
        pygame.draw.line(DISPLAYSCREEN, RED, (15, 600), (950, 599), 1)

        DISPLAYSCREEN.blit(finish, (850, 100))
        DISPLAYSCREEN.blit(finish, (850, 200))

        p1 = DISPLAYSCREEN.blit(img_p1, (x[0], y[0]))
        p2 = DISPLAYSCREEN.blit(img_p2, (x[1], y[1]))
        p3 = DISPLAYSCREEN.blit(img_p3, (x[2], y[2]))
        p4 = DISPLAYSCREEN.blit(img_p4, (x[3], y[3]))
        p5 = DISPLAYSCREEN.blit(img_p5, (x[4], y[4]))

        for i in range(0,5):
            if x[i] <= getx:
                x[i] += random.uniform(1,5)

            if x[i] >= getx:
                winner = i
                if winner == bettingFigure: 
                    userMoney += money
                else:
                    userMoney -= money
                running = False
                break

        if running == False:
            # result = str(winner)
            GameResult(winner, bettingFigure, money, userMoney)
            break

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


        fpsClock.tick(1000)
        pygame.display.update()
    
    return userMoney

# GAMERESULT------------------------------------------------------------------------------------------#

def GameResult(winner, bettingFigure, money, userMoney) -> object:
    click = False
    running = True

    # TODO - call file that display the result
    subprocess.call(['python', \
                     'pages/winnerCongratulation.py', \
                     str(winner),\
                     str(bettingFigure),\
                     str(money),\
                     str(userMoney)])
    
    while running:
        DISPLAYSCREEN.blit(background, (0, 0))
        draw_text_3('CONGRATULATION!!! ',font_3, RED, DISPLAYSCREEN, 200, 400)

        mx,my = pygame.mouse.get_pos()

        button_1_1 = DISPLAYSCREEN.blit(img_back, (10, 10))

        if button_1_1.collidepoint((mx, my)):
            if click == True:
                main_menu_start()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        fpsClock.tick(60)

if __name__ == '__main__':
    main_menu_start()
