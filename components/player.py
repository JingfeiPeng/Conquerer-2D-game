import pygame 
from pygame.locals import * 
pygame.init()

# change sys path to root
import sys
sys.path.append('../')

from util.utils import *


class MainPlayer:
    def __init__(self, health, attack, mobility):
        #a sound file for shooting bullets
        self.shoot = pygame.mixer.Sound(file="assets/sounds/CoolGunShoot.wav")
        self.direction = None #preset a variable to show the bullet/character's direction
        
        #a list for bullets
        self.bulletList = []
        self.bulletSpeed = int(15)

        #a counter variable to control the rate of fire
        self.counter = 0
        
        #a dictionary is used to store the coordinates of obstacles in a map
        self.mapDict = {
            1: [(300,500,50,300),(300,0,50,300),(500,300,50,600),(700,100,200,50),(700,500,200,50)],
            2:[(695,100,50,300),(500,300,50,300),(300,100,50,300),(100,250,50,300)],
            3:[(550,20,80,50),(500,320,50,50),(250,0,50,300),(150,500,50,300),(750,300,50,400), (400,600,50,100),(430,250,200,50),(430,400,200,50),(500,100,200,50)],
            4:[],
            5:[]}

        self.mapUse = 1
        
        
        self.health = health  #convert the variables to variables in a class
        self.attack = attack
        self.mobility = mobility
    
        #set the imageSize
        self.imageX=50
        self.imageY=80

        self.x =0 #set the inital x, y, change values
        self.y =0 
        self.x_change = 0
        self.y_change = 0
        
        self.image = pygame.image.load("assets/images/AlienStand.png").convert_alpha() #load the image of the character
        self.image=pygame.transform.scale(self.image,(self.imageX,self.imageY))   #change the scale of image
        self.rect=self.image.get_rect()
        
        
    def updateMap(mapNum):  #this function deterimines the map number to use
        
        if mapNum == 1:
            self.mapUse=self.Map1
        elif mapNum == 2:
            self.mapUse = self.Map2
        elif mapNum == 3:
            self.mapUse = self.Map3
        elif mapNum == 4:
            self.mapUse = self.Map4
        
    def update(self):
        for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.display.quit()
                    
        keys = pygame.key.get_pressed()  #handles the control of the player

        if keys[K_a]:  #go left 
            self.x -= self.mobility
            self.direction = "left"
        elif keys[K_d]: #go right
            self.x += self.mobility
            self.direction = "right"
        elif keys[K_w]: #move up
            self.y -= self.mobility
            self.direction = "up"
        elif keys[K_s]:#move down
            self.y += self.mobility
            self.direction = "down"

        #changes the main character's picture when it moves left
        if self.direction  ==  "left":
            self.image = pygame.image.load("assets/images/CharacterLeft.png")

            self.image = pygame.transform.scale(self.image, (self.imageX , self.imageY)) 
            
        elif self.direction  ==  "right": #changes picture when move right
            self.image = pygame.image.load("assets/images/CharacterRight.png")

            self.image = pygame.transform.scale(self.image, (self.imageX , self.imageY))
            
        elif self.direction  ==  "up": #changes picture when move Back
            self.image = pygame.image.load("assets/images/CharacterBack.png")

            self.image = pygame.transform.scale(self.image, (self.imageX , self.imageY))
            
        elif self.direction  ==  "down": #changes picture when move down
            self.image = pygame.image.load("assets/images/AlienStand.png")
            self.image = pygame.transform.scale(self.image, (self.imageX , self.imageY)) 
            

        #shoot bullets when self.counter, attack speed is greater than 10
        if self.counter > 10:
            if keys[K_k]:
                self.shoot.play()
                self.bulletList += [(self.x+self.imageX/2, self.y+self.imageY/2, self.direction, self.attack)]
                self.counter = 0

        for bullet in self.bulletList:
            if bullet[2] == "left":
                self.bulletList[self.bulletList.index(bullet)] = ((bullet[0]-self.bulletSpeed),bullet[1],bullet[2],self.attack)
                
            
            elif bullet [2] == "right":
                self.bulletList[self.bulletList.index(bullet)] = ((bullet[0]+self.bulletSpeed),bullet[1],bullet[2],self.attack)
                
            elif bullet[2] == "up":
                self.bulletList[self.bulletList.index(bullet)] = (bullet[0],bullet[1]-self.bulletSpeed,bullet[2],self.attack)
                
            elif bullet[2] == "down":
                self.bulletList[self.bulletList.index(bullet)] = (bullet[0],bullet[1]+self.bulletSpeed,bullet[2], self.attack)
        
        #check first before the soldier move
        #check if the sprite is overlapping with any obstacle
        for block in self.mapDict[self.mapUse]:
            
            #checks if the player collides with an obstacle
            if checkCollisionRect((self.x,self.y),50,80,(block[0],block[1]),block[2],block[3]):
                if self.x <= block[0] and self.y < block[1]+block[3] and self.y+self.imageY > block[1] and keys[K_d]:
                #checks if the obstacle is to the right and the right key is being pressed
                    self.x -= self.mobility
                    
                #but the player back to before moving
                #check if the obstacle is to the left of the player
                elif self.x <= block[0]+block[2] and self.y <block[1]+block[3] and self.y+self.imageY > block[1] and keys[K_a]: 
                    self.x += self.mobility
                    
                elif self.x+self.imageX >= block[0] and self.x <= block[0]+block[2] and self.y >=block[1] and keys[K_w]:
                    self.y += self.mobility
                    
                elif self.x+self.imageX >= block[0] and self.x <= block[0]+block[2] and self.y < block[1]+block[3] and keys[K_s]:
                    self.y -=self.mobility

        for bullet in self.bulletList:            #delete the bullet that collides with a wall
            for block in self.mapDict[self.mapUse]:
                #checks if the bullet collides with an obstacle
                if checkCollisionRect((bullet[0],bullet[1]),10,10,(block[0],block[1]),block[2],block[3]):
                    bulletPointer = self.bulletList.index(bullet)
                    del (self.bulletList[bulletPointer])

        #check if the player has gone out of the boundary    
        if self.x <= 0:
            self.x = 0
            
        if self.x >= (900-self.imageX):
            self.x = (900-self.imageX)
            
        if self.y <= 0:
            self.y = 0
            
        if self.y >=(700-self.imageY):
            self.y = 700-self.imageY
            
        if self.x >800 and self.y>600:
            self.mapUse += 1
            self.x = 0
            self.y = 0

        self.counter +=1
            
        
        return(self.x , self.y, self.mapUse)

        