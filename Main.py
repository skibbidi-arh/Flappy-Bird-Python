import random #for generating random numbers
import sys # it has a sys.exit command which works like SetDefaultCloseOperation
import pygame
from pygame.locals import*

#global variables for the game
FPS = 32
SCREENWIDTH = 1080      #289
SCREENHEIGHT = 800       #511

SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8 
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'

def welcomeScreen():
    #shows welcome image on the screen
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT-GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH-GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and (event.key== K_ESCAPE or event.key == K_DOWN)):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key== K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def maingame():
    score =0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/2)



if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('flappy bird')
    GAME_SPRITES['numbers']=(
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),

    )

    GAME_SPRITES['message']= pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base']= pygame.image.load('gallery/sprites/ground.png').convert_alpha()
    GAME_SPRITES['pipe']=(
        pygame.transform.rotate(pygame.image.load('gallery/sprites/pipe.png').convert_alpha(),180),
        pygame.image.load('gallery/sprites/message.png').convert_alpha(),
    )
    #game sounds
    
    GAME_SOUNDS['die']=pygame.mixer.Sound('gallery/sounds/die.mp3')
    GAME_SOUNDS['hit']=pygame.mixer.Sound('gallery/sounds/hit.mp3')
    GAME_SOUNDS['point']=pygame.mixer.Sound('gallery/sounds/point.mp3')
    GAME_SOUNDS['swoosh']=pygame.mixer.Sound('gallery/sounds/swoosh.mp3')
    GAME_SOUNDS['wing']=pygame.mixer.Sound('gallery/sounds/wing.mp3')

    GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() #shows welcome screen to the user until he presses a button
        maingame() #this is the main game function

