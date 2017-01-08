#Crystal Boy (DEMO).
#A game about fossil fuels.
#Copyright (C) 2017 Corinna Yong & Ellie Ly
#Title background, Level background and music are not owned by us. 

import pygame, sys, time, random, math, glob
from pygame.locals import *
from time import sleep

pygame.init()
clock = pygame.time.Clock()
display_width = 800 #x
display_height = 600 #y

WHITE = (255,255,255)
BLACK = (0,0,0)

pywindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Crystals (DEMO)')

smallfont = pygame.font.Font('ARCADECLASSIC.TTF', 25)
medfont = pygame.font.Font('ARCADECLASSIC.TTF', 30)
largefont = pygame.font.Font('ARCADECLASSIC.TTF', 80)

#GRAPHICS, IMAGES, SOUNDS
#IMPORT ITEMS
titlebg = pygame.image.load('titlebg.jpg').convert()
titlebg = pygame.transform.scale(titlebg, (display_width, display_height))
levelbg = pygame.image.load('levelback.png').convert()
levelbg = pygame.transform.scale(levelbg, (display_width, display_height))
crystal = pygame.image.load('crystal1.png').convert_alpha()
boy = pygame.image.load('boy1.png').convert_alpha()

class Platform:
    def __init__(self, x,y,w,h):
        self.image=pygame.Surface((w,h))
        self.image.fill(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Crystal:
    def __init__(self):
        self.x=250
        self.y=500
        
        self.ani_speed_init=20
        self.ani_speed=self.ani_speed_init
        self.ani=glob.glob("crystal/crystal*.png")
        self.ani.sort()
        self.ani_pos=0
        self.ani_max = len(self.ani)-1
        self.img=pygame.image.load(self.ani[0])

        pywindow.blit(self.img, (self.x, self.y))

class Player:
    def __init__(self):
        self.x=80
        self.y=510
        
        self.ani_speed_init=10
        self.ani_speed=self.ani_speed_init
        self.ani=glob.glob("boy/boy*.png")
        self.ani.sort()
        self.ani_pos=0
        self.ani_max = len(self.ani)-1
        self.img=pygame.image.load(self.ani[0])
        self.update(0)

    def update(self, pos):
        if pos != 0:
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.img=pygame.image.load(self.ani[self.ani_pos])
                self.ani_speed=self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
        pywindow.blit(self.img, (self.x, self.y))

def game_intro():
    intro = True
    music = pygame.mixer.music.load("Title Theme - The Legend of Zelda- Ocarina of Time.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.4)
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    intro = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        pywindow.blit(titlebg, (0,0))
        message_to_screen('Crystal Boy Demo', WHITE, y_displace= -150, size='large')
        message_to_screen('Press SPACE to play or ESCAPE to quit', WHITE, 150)
        pygame.display.update()

def game_cutscene():
    cutscene = True
    while cutscene:
        #press S to skip or finish
        music = pygame.mixer.music.load("The Art Gallery from Ib.mp3")
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.4)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.mixer.music.stop()
                    cutscene = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        message_to_screen('King: The kingdom is now entering day 5 of it’s crystal drought. We must not continue to live this way.', WHITE, 12)
            
        message_to_screen('King: Ah yes, Errand Boy. You are aware of the lack of crystal supply in the kingdom no?', WHITE, 12)
            
        message_to_screen('King:  In order for our land to prosper and properly function, we need to obtain those crystals, they are the main source of our energy with their enchanted powers that wizards can utilize to run our mills and contraptions.', WHITE, 12)
            
        message_to_screen('King: I sentence you to pursue these crystals in the Green forest and bring prosperity back to our kingdom. From this day forth, ye shall be referred to as Crystal Boy.', WHITE, 12)
            
        message_to_screen('Press S to skip', WHITE, 12)
        #pywindow.blit(levelbg, (0,0))
        pygame.display.update()

def game_level():
    level = True
    playerBoy=Player()
    pos=0
    playerBoy.update(pos)
    while level:
        pywindow.blit(levelbg, (0,0))
        pywindow.blit(crystal, (500,520))
        pygame.display.update()
        clock.tick(500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                pos = 1
            elif event.type == KEYUP and event.key == K_RIGHT:
                pos = 0
            elif event.type == KEYDOWN and event.key == K_LEFT:
                pos = -1
            elif event.type == KEYUP and event.key == K_LEFT:
                pos = 0

        playerBoy.update(pos)
        pygame.display.update()

def text_objects(text, color, size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    elif size == 'medium':
        textSurface = medfont.render(text, True, color)
    elif size == 'large':
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size='small'):
    textSurf, textRect = text_objects(msg, color, size) #revamp code below
    textRect.center = (display_width/2), (display_height/2) + y_displace
    pywindow.blit(textSurf, textRect)

def gameLoop():
    gameExit = False
    gameOver = False

    while not gameExit: #CHECK FOR EVENT HANDLING
        while gameOver == True:  
            pywindow.blit(background, (0,0))
            message_to_screen('FIN', WHITE, y_displace = -100, size = 'large')
            message_to_screen('Press the SPACEBAR to play again or ESCAPE to quit', WHITE, y_displace = 100, size = 'medium')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        return #gameLoop()

        boy_rect = boy.get_rect(center=(80, 510))
        crystal_rect = crystal.get_rect(center=(500,520))
        if boy_rect.colliderect(crystal_rect):
            gameOver=True
        pygame.display.update()
        
    pygame.quit() #Uninitialize
    quit() #Exit game

game_intro()
game_cutscene()
game_level()
while True:
    gameLoop()
            
















        
