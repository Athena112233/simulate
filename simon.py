import pygame
import random
import sys
import time
from pygame.locals import *

#variables initialization 
#global variables
FPS = 30 #frame per second
WINDOWWIDTH = 750
WINDOWHEIGHT = 750 
FLASHSPEED = 500
FLASHDELAY = 200
BUTTONSIZE = 300
BUTTONGAPSIZE = 50

#color name            R     G     B 
WHITE = 0
BLACK = 0
BRIGHTRED = 0
RED = 0
BRIGHTGREEN = 0 
GREEN = 0
BRIGHTBLUE = 0
BLUE = 0
BRIGHTYELLOW = 0 
YELLOW = 0

#functions
def main():
    """controls game conditions, game display, and main while loop"""
    global FPSCLOCK, WIN, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    WIN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('simulate')

    while True:
        checkForQuit()


def terminate():
    """end the game"""
    pygame.quit()
    sys.exit()

def checkForQuit():
    """check if to call terminate"""
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

def flashButtonAnimation(color, animationSpeed = 50):
    """flash button animation"""
    #todo

def drawButtons():
    """draw rectangles"""
    #todo 

def changeBackgroundAnimation(animationSpeed = 40):
    """change bg every rounds"""
    #todo 

def gameOverAnimation(color = WHITE, animationSpeed = 50):
    """game over animation"""
    #todo 

def getButtonClicked(x, y):
    """get the button clicked"""
    #tod0

main()