import pygame 
from pygame.locals import * 
pygame.init()
from config import width, height

screen = pygame.display.set_mode((width,height)) # set up screen
clock = pygame.time.Clock()
menuSea=pygame.image.load("assets/images/menuSea.png")
cancel=pygame.image.load("assets/images/cancel.png") #picture for the cancel button
click = pygame.mixer.Sound(file="assets/sounds/click.wav") #used for a sound effect

#Colours:
red=(230,0,0)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
lightYellow=(200,250,204)
orange=(255,165,0)
brightYellow=(244,219,3)


#A dictionary that is used to store the list of items in labratory
items = {"Doran's Blade":"1,0,0,150,100","Inifinity Edge":"2,0,1,300,150","Hextech Gun":"3,0,2,400,200","Fire cannon":"4,0,2,600,400","Relic shield":"0,10,0,300,150","Warmog's armor":"0,30,0,600,300","Boot of mobility":"0,0,3,200,100","Boot of swiftness":"0,0,4,400,200"}

#A function to make item attributes store in variables, pass the name of the item in
def findAtt(Name):
    #find what is the values of the name, name being the item's name
    attributes = items[Name]
    attributesSplit = attributes.split(",")
    attackInfo = attributesSplit[0]
    healthInfo = attributesSplit[1]
    mobilityInfo = attributesSplit[2]
    goldInfo = attributesSplit[3]
    scorePointInfo = attributesSplit[4]
    return (attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo)

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
