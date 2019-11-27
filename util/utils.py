import pygame 
from pygame.locals import * 
pygame.init()
from config import width, height

screen = pygame.display.set_mode((width,height)) # set up screen

# a function to check if the objects are colliding. check enemy in enemy list
#  then check collide using the function, then delete the enemy.
def checkCollisionRect(pos1,pos1w,pos1h,pos2,pos2w, pos2h):
    mask1 = pygame.Rect((pos1),(pos1w,pos1h))  #create a mask to shadow over the player's position
    mask2 = pygame.Rect((pos2),(pos2w,pos2h))  #create a mask to shadow over the obstacle's position
    return mask1.colliderect(mask2)

#create a function to put concontroble size text on the screen
def textScreen(msg,colour,x,y,size):
    gameFontS=pygame.font.SysFont("Arial", size )  #set the font 
    screen_text=gameFontS.render(msg,True,colour)   #place the text message
    screen.blit(screen_text, (x,y))

#Make a function to move the Alien character
def MovingAlien(x,y):
    AlienStand1=pygame.image.load("assets/images/AlienStand.png") #load the images of character
    AlienStand2=pygame.image.load("assets/images/AlienStand2.png")
    AlienStand3=pygame.image.load("assets/images/AlienStand3.png")
    AlienStand4=pygame.image.load("assets/images/AlienStand4.png") 
    MoveA=[AlienStand1,AlienStand2,AlienStand3,AlienStand4]
    
    for pic in MoveA:
        clock.tick(10)
        screen.blit(pic,(x,y))
        pygame.display.update()
