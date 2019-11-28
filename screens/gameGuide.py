import pygame 
from pygame.locals import *

from config import width, height
screen = pygame.display.set_mode((width,height)) # set up screen
from util.utils import *

# change sys path to root
import sys
sys.path.append('../')

#A function for creating the second page of game guide
def gameGuide2():
    
    #set boolean variable for the while loop 
    gameGuide2=True
    guidePic2=pygame.image.load("assets/images/GameGuide2.png")
    
    while gameGuide2:
        mouse=pygame.mouse.get_pos() #get mouse inputs
        screen.blit(guidePic2,(0,0)) #blit the neccessary pictures
        screen.blit(cancel,(850,0))
        pygame.display.update()
        
        for event in pygame.event.get():
            
            if event.type== QUIT: #handles the cancel button
                menu=False
                inteface= False
                pygame.display.quit()
                
            elif event.type==MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    if mouse[0]>850 and mouse[1]<50 and mouse[1]>0: #handle the in game cancel button
                        click.play()
                        gameGuide2=False

#function used to handle game guide pages
def gameGuide():
    guidePic=pygame.image.load("assets/images/GameGuide.png") #load the image for gameguide page
    gameguide=True
    
    while gameguide:
        
        mouse=pygame.mouse.get_pos() #get mouse's position
        screen.blit(guidePic,(0,0)) #bilt the picture of game guide
        screen.blit(cancel,(850,0)) #bilt the cancel button
        pygame.display.update() #refresh the screen
        
        for event in pygame.event.get():  #handle events
            
            if event.type== QUIT:
                menu=False
                inteface= False
                
                
            elif event.type==MOUSEBUTTONDOWN:
                #handle buttons on the screen
                if pygame.mouse.get_pressed() == (1,0,0):  #handle when the cancel button is clicked
                    if mouse[0]>850 and mouse[1]<50 and mouse[1]>0:
                        click.play()
                        gameguide=False
                    if mouse[0]>725 and mouse[1]>50 and mouse[1]<89: #handle when next page button is clicked
                        click.play()
                        gameGuide2()