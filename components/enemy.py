import pygame 
from pygame.locals import * 
pygame.init()

# change sys path to root
import sys
sys.path.append('../')

from util.utils import *
from util.map import mapObstacles
import random
import math


#a class to define enemies
class Enemy:
    def __init__(self, tier):
        self.shoot = pygame.mixer.Sound(file="assets/sounds/GunShoot.wav")
        
        self.counter = 0
        self.shootList = []
        self.direction = None
        self.tier = tier
        
        #a dictionary that contatins coordinates of obstacles in a map
        self.mapDict = mapObstacles
        self.mapUse = 1
        
        if self.tier == 1 :   #tier for soldiers
            self.imageSizeX=50
            self.imageSizeY=80
            self.attack =1
            self.health =3
            self.mobility =3
            self.attackspeed = 10
            self.bulletSpeed = 15
            self.image = pygame.image.load("assets/images/SoldierTier2Front.png")
            self.image=pygame.transform.scale(self.image, (self.imageSizeX,self.imageSizeY))

        elif self.tier == 2:
            self.imageSizeX = 100
            self.imageSizeY = 120
            self.attack = 5
            self.health = 10
            self.mobility =1
            self.attackspeed =30
            self.bulletSpeed = 10
            self.image = pygame.image.load("assets/images/TankLeft.png")
            self.image=pygame.transform.scale(self.image, (self.imageSizeX,self.imageSizeY))
            
        else:
            print("tier not defined")
            
        touchObstacle = True
        touch = "no"  #preset if the enemy touch the obstacle to no
        
        #generate the enemy and check if the enemy is overlapping with any obstacle
        while touchObstacle:
            touch = "no"
            self.x = random.randrange(12,85)*10
            self.y = random.randrange(12,60)*10
            for block in self.mapDict[self.mapUse]:
                #checks if the enemy collides with an obstacle
                if checkCollisionRect((self.x,self.y),self.imageSizeX,self.imageSizeY,(block[0],block[1]),block[2],block[3]):
                    touch = "yes"
            if touch == "no":
                touchObstacle = False
                

        #randomly generate the enemy's position
        
    def updateEnemy(self, playerpos):
        
        #checks if the enemy should move accodring to the player's postion
        if playerpos[0] < self.x and playerpos[0] <= self.x- 10:   #enemy move left
            self.x -=self.mobility
            self.direction = "left"
            
        elif playerpos[0] > self.x and playerpos[0] >= self.x- 10: #enemy move right
            self.x += self.mobility
            self.direction = "right"
            
        if playerpos[1] >= self.y and playerpos[1] >= self.y- 10: #enemy move down
            self.y +=self.mobility
            self.direction = "down"

        elif playerpos[1] <= self.y and playerpos[1] <= self.y- 10: #enemy move up
            self.y -=self.mobility
            self.direction = "up"

        if self.direction == "left": # change the picture of the enemy according to its direction of movement
            
            if self.tier ==1:
                self.image = pygame.image.load("assets/images/SoldierTier2Left.png")
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))

            elif self.tier == 2:
                self.image = pygame.image.load("assets/images/TankLeft.png")
                self.imageSizeX = 100
                self.imageSizeY= 120
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))

        if self.direction == "right": # change the picture of the enemy according to its direction of movement
            
            if self.tier == 1:
                self.image = pygame.image.load("assets/images/SoldierTier2Right.png")
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))
                
            elif self.tier == 2:
                self.image = pygame.image.load("assets/images/TankRight.png")
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))

        if self.direction == "up":
            if self.tier == 1:
                self.image = pygame.image.load("assets/images/SoldierTier2Back.png")
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))
                
        if self.direction == "down":
            if self.tier == 1:
                self.image = pygame.image.load("assets/images/SoldierTier2Front.png")
                self.imageSizeX = 50
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY)) 
            



        
        #check if the sprite is overlapping with any obstacle
        for block in self.mapDict[self.mapUse]:
            #checks if the enemy collides with an obstacle
            if checkCollisionRect((self.x,self.y),self.imageSizeX,self.imageSizeY,(block[0],block[1]),block[2],block[3]):
                
                if self.x <= block[0] and self.y <= block[1]+block[3] and self.y+self.imageSizeY >= block[1]:
                #checks if the obstacle is to the right of the enemy 
                    self.x -= 2*self.mobility
                    
                #check if the obstacle is to the left of the enemy    
                if self.x <= block[0]+block[2] and self.y <block[1]+block[3] and self.y+self.imageSizeY > block[1]: 
                    self.x += self.mobility
                    
                if self.x+self.imageSizeX >= block[0] and self.x <= block[0]+block[2] and self.y+self.imageSizeY >=block[1]:
                    self.y += self.mobility
                    
                if self.x+self.imageSizeX >= block[0] and self.x <= block[0]+block[2] and self.y < block[1]+block[3]:
                    self.y -= 2*self.mobility 
                    
        #code the enemy to shoot bullets at the player
        if self.counter > self.attackspeed:
            
            if playerpos[1] <= self.y+10 and playerpos[1] > self.y-10:
                if playerpos[0]< self.x:
                    self.direction = "left"
                    if self.tier == 1:
                        self.shootList += [(self.x+self.imageSizeX/2, self.y+self.imageSizeY/2, self.direction, self.attack)]
                        
                    elif self.tier == 2:
                        self.shootList += [(self.x+self.imageSizeX/2, self.y+20, self.direction, self.attack)]
                    self.shoot.play()
                    
                elif playerpos[0] > self.x:
                    self.direction = "right"

                    if self.tier == 1:
                        self.shootList += [(self.x+self.imageSizeX/2, self.y+self.imageSizeY/2, self.direction, self.attack)]

                    elif self.tier == 2:
                        self.shootList += [(self.x+self.imageSizeX/2, self.y+20, self.direction, self.attack)]                    
                    self.shoot.play()
                    
            elif playerpos[0] <= self.x +10 and playerpos[0] >=self.x-10:
                if playerpos[1] < self.y:
                    self.direction = "up"
                    self.shootList += [(self.x+self.imageSizeX/2, self.y+self.imageSizeY/2, self.direction, self.attack)]
                    self.shoot.play()
                    
                elif playerpos[1] >self.y:
                    self.direction = "down"
                    self.shootList += [(self.x+self.imageSizeX/2, self.y+self.imageSizeY/2, self.direction, self.attack)]
                    self.shoot.play()
                    
            self.counter = 0  #reset the attackspeed timer
                    
        for bullet in self.shootList:  #proccess the bullet to make it shoot
            if bullet[2] == "left": #shoot at left direction
                self.shootList[self.shootList.index(bullet)] = ((bullet[0]-self.bulletSpeed),bullet[1],bullet[2],self.attack)
                
            
            elif bullet [2] == "right": #shoot in right direction
                self.shootList[self.shootList.index(bullet)] = ((bullet[0]+self.bulletSpeed),bullet[1],bullet[2],self.attack)
                
            elif bullet[2] == "up": #shoot in up direction
                self.shootList[self.shootList.index(bullet)] = (bullet[0],bullet[1]-self.bulletSpeed,bullet[2],self.attack)
                
            elif bullet[2] == "down": #shoot down
                self.shootList[self.shootList.index(bullet)] = (bullet[0],bullet[1]+self.bulletSpeed,bullet[2], self.attack)
                
            
        #time when the enemy can shoot bullets
        self.counter +=1 
              
        #delete the bullet when a bullet passes through a wall
        for bullet in self.shootList:
            
            for block in self.mapDict[self.mapUse]:
                #checks if the player collides with an obstacle
                if checkCollisionRect((bullet[0],bullet[1]),10,10,(block[0],block[1]),block[2],block[3]):
                    bulletPointer = self.shootList.index(bullet)
                    del (self.shootList[bulletPointer])
