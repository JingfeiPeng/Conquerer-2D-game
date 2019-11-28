#JefferPeng
#May.23rd, 2016
#Mr.Cope
#ICS Summative Game File.txt

#This is the program file of ICS Summative
#input: mouse, keyboard input
#output: images on screen

#import the neccessary libraries
import pygame 
from pygame.locals import * 
pygame.init()
#imort random so the enemies can be displayed randomly
import random
import math

# custom modules
from config import width, height
from util.utils import *

# screens
from screens.gameGuide import gameGuide, gameGuide2
from screens.menu import menu
from screens.labratory import labratory 
from screens.battleIntro import battleIntro

from gamePlay import gamePlay
      
#find background picture for menu
cancel=pygame.image.load("assets/images/cancel.png") #picture for the cancel button
cancelSize=cancel.get_rect()
full_size = (900, 700) #screen size

#character attriubutes
health=20
attack=1
mobility=10
tier=1
gold = 0
scorePoint = 0

#set screen
screen=pygame.display.set_mode(full_size)
pygame.display.set_caption("The Conqueror")#set caption

introImg=pygame.image.load('assets/images/IntroScreen.png')
introImg=pygame.transform.scale(introImg,(full_size))


#set boolean variables for each stage of the game
introscreen=True
interface=True


#create variables to represent status in the game
health=20
attack=1
mobility=10
gold=0
scorePoint=0

#set sounds files
click = pygame.mixer.Sound(file="assets/sounds/click.wav") #used for a sound effect

clock = pygame.time.Clock() #set clock
          
#blit intro screen
while introscreen:
    screen.blit(introImg, (0,0)) #intro image
    pygame.display.flip() #display the intro image
    
    for event in pygame.event.get():
        
        if event.type == QUIT:  #hanldes quit event
            keep_going = False
            pygame.display.quit()
            
        elif event.type == KEYDOWN: #hande whenever a key is pressed, this startes the game
            click.play()
            introscreen=False
            
seaImg=pygame.image.load('assets/images/Sea.png')

while interface:
    #get the mouse's position
    mouse =pygame.mouse.get_pos()

    clock.tick(30)
    
    #North American union x:50-275 y 115-540
    #Middle East union: x:335-519,Y:120-545
    #Soviet union: x:520-695 Y:120-545
    #Asia union: x:696-875 Y:120-545,
    screen.blit(seaImg,(0,0))
    
    #set boundary lines for option bar
    pygame.draw.rect(screen, black, (0,590,900,10))
    pygame.draw.rect(screen, white, (0,600,900,100))
    pygame.draw.rect(screen, black, (225,600,10,100))
    pygame.draw.rect(screen, black, (450,600,10,100))
    pygame.draw.rect(screen, black, (675,600,10,100))
    
    #put texts
    textScreen("Menu",black,10,600,100)
    textScreen("View             Game",black, 250 ,600,50)
    textScreen("status             Guide",black, 255,650,50)
    textScreen("Laboratory",black, 685,610,50)
    for event in pygame.event.get():
        if event.type == QUIT:
            interface = False
            pygame.display.quit()
        elif event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                if mouse[0]>50 and mouse[0]<275 and mouse[1]>115 and mouse[1]<545:
                    click.play()
                    battle = "NorthAmericaUnion"
                    back , diffculty= battleIntro(battle, attack,health,mobility)
                    if back == False:  #checks if the cancel button in the game intro is clicked
                        soldier = round(5*diffculty)
                        tank = round(2 *diffculty)
                        health, gold, scorePoint = gamePlay(attack, health, mobility, gold, scorePoint,soldier,tank)
                    pygame.mixer.music.stop()


                elif mouse[0]>335 and mouse[0]<519 and mouse[1]>120 and mouse[1]<545:
                    click.play()
                    battle = "MiddleEastUnion"
                    back , diffculty= battleIntro(battle, attack,health,mobility)
                    if back == False:  #checks if the cancel button in the game intro is clicked
                        soldier = round(3*diffculty)
                        tank = round(2 *diffculty)+1
                        health, gold, scorePoint = gamePlay(attack, health, mobility, gold, scorePoint,soldier,tank)
                    pygame.mixer.music.stop()
                    
                elif mouse[0]>520 and mouse[0]<695 and mouse[1]>120 and mouse[1]<545:
                    click.play()
                    battle = "SovietUnion"
                    back , diffculty= battleIntro(battle, attack,health,mobility)
                    if back == False:  #checks if the cancel button in the game intro is clicked
                        soldier = round(2*diffculty)
                        tank = round(1 *diffculty)+1
                        health, gold, scorePoint = gamePlay(attack, health, mobility, gold, scorePoint,soldier,tank)
                    pygame.mixer.music.stop()
                    
                elif mouse[0]>696 and mouse[0]<875 and mouse[1]>120 and mouse[1]<545:
                    click.play()
                    battle = "AsiaUnion"
                    back , diffculty= battleIntro(battle, attack,health,mobility)
                    if back == False:  #checks if the cancel button in the game intro is clicked
                        soldier = round(2*diffculty)
                        tank = 0
                        health, gold, scorePoint = gamePlay(attack, health, mobility, gold, scorePoint,soldier,tank)
                    pygame.mixer.music.stop()

                #check if the four buttons on the bottem is clicked. Menu,view status, Game guide and labratory
                if mouse[1]>600:
                    if mouse[0]>0 and mouse[0]<225 :
                        click.play()
                        #send attribute variables to the function
                        attack, health,mobility, gold, scorePoint,interface = menu(attack, health,mobility, gold, scorePoint)
                    elif mouse[0]>225 and mouse[0]<450 :
                        print(gold)
                        viewStatus=True
                        click.play()
                        #make the background black image
                        backG=pygame.image.load("assets/images/Black.png")
                        backG=pygame.transform.scale(backG,(full_size))
                        while viewStatus:
                            clock.tick(10)
                            #get the mouse's position
                            mouse=pygame.mouse.get_pos()
                            screen.blit(backG,(0,0))
                            
                            #write the text that will be shown on screen
                            textScreen("View Status:",orange,0,0,100)
                            textScreen("Attack:",white,50,100,75)
                            attackStr=str(attack)
                            textScreen(attackStr,white,250,100,75)
                            healthStr=str(health)
                            textScreen("Health Points:", white, 50,180,75)
                            textScreen(healthStr, white,450,180,75)
                            textScreen("Mobility:", white,50,260,75)
                            mobilityStr=str(mobility)
                            textScreen(mobilityStr,white,300,260,75)
                            textScreen("Golds:",white,50,340,75)
                            goldS=str(gold)
                            textScreen(goldS,white,280,340,75)
                            textScreen("Score Points:", white,50,420,75)
                            scorePointStr=str(scorePoint)
                            textScreen(scorePointStr,white,450,420,75)
                            screen.blit(cancel,(850,0))
                            MovingAlien(650,200)

                            #update the pictures
                            pygame.display.update()

                            #handle mouse actions
                            for event in pygame.event.get():
                                
                                #quit everything when cancel is clicked
                                if event.type==QUIT:
                                    viewStatus=False
                                    interface=False
                                    pygame.display.quit()
                                elif event.type==MOUSEBUTTONDOWN:
                                    
                                    if pygame.mouse.get_pressed() == (1,0,0):
                                        #quit the view status interface when the cancel button is clicked
                                        if mouse[0]>850 and mouse[1]<50:
                                            click.play()
                                            viewStatus=False
                    #handle if gameguide is clicked                
                    elif mouse[0]>460 and mouse[0]<675 :
                        
                        #play the click sound
                        click.play()
                        gameGuide()           #goes to the function for game guide
                    elif mouse[0]>685 and mouse[0]<900 :
                        click.play()
                        #pass gold, scorepoint information to the labratory and get it back
                        attack, health,mobility, gold,scorePoint=labratory(attack, health,mobility,gold,scorePoint)
            
    pygame.display.flip()


pygame.display.quit()

