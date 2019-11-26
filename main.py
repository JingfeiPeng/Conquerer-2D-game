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

#a function to check if the objects are colliding. check enemy in enemy list, then check collide using the function, then delete the enemy.
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

class MainPlayer:
    def __init__(self, health, attack, mobility):
        #a sound file for shooting bullets
        self.shoot = pygame.mixer.Sound(file="CoolGunShoot.wav")
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
        
        self.tier = tier
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
            self.image = pygame.image.load("CharacterLeft.png")

            self.image = pygame.transform.scale(self.image, (self.imageX , self.imageY)) 
            
        elif self.direction  ==  "right": #changes picture when move right
            self.image = pygame.image.load("CharacterRight.png")

            self.image = pygame.transform.scale(self.image, (self.imageX , self.imageY))
            
        elif self.direction  ==  "up": #changes picture when move Back
            self.image = pygame.image.load("CharacterBack.png")

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

        

        
#a class to define enemies
class Enemy:
    def __init__(self, tier):
        self.shoot = pygame.mixer.Sound(file="GunShoot.wav")
        
        self.counter = 0
        self.shootList = []
        self.direction = None
        self.tier = tier
        
        #a dictionary that contatins coordinates of obstacles in a map
        self.mapDict = {
            1: [(300,500,50,300),(300,0,50,300),(500,300,50,600),(700,100,200,50),(700,500,200,50)],
            2:[(695,100,50,300),(500,300,50,300),(300,100,50,300),(100,250,50,300)],
            3:[(550,20,80,50),(500,320,50,50),(250,0,50,300),(150,500,50,300),(750,300,50,400), (400,600,50,100),(430,250,200,50),(430,400,200,50),(500,100,200,50)],
            4:[],
            5:[]}
        self.mapUse = 1
        
        if self.tier == 1 :   #tier for soldiers
            self.imageSizeX=50
            self.imageSizeY=80
            self.attack =1
            self.health =3
            self.mobility =3
            self.attackspeed = 10
            self.bulletSpeed = 15
            self.image = pygame.image.load("SoldierTier2Front.png")
            self.image=pygame.transform.scale(self.image, (self.imageSizeX,self.imageSizeY))

        elif self.tier == 2:
            self.imageSizeX = 100
            self.imageSizeY = 120
            self.attack = 5
            self.health = 10
            self.mobility =1
            self.attackspeed =30
            self.bulletSpeed = 10
            self.image = pygame.image.load("TankLeft.png")
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
                self.image = pygame.image.load("SoldierTier2Left.png")
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))

            elif self.tier == 2:
                self.image = pygame.image.load("TankLeft.png")
                self.imageSizeX = 100
                self.imageSizeY= 120
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))

        if self.direction == "right": # change the picture of the enemy according to its direction of movement
            
            if self.tier == 1:
                self.image = pygame.image.load("SoldierTier2Right.png")
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))
                
            elif self.tier == 2:
                self.image = pygame.image.load("TankRight.png")
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))

        if self.direction == "up":
            if self.tier == 1:
                self.image = pygame.image.load("SoldierTier2Back.png")
                self.image = pygame.transform.scale(self.image, (self.imageSizeX , self.imageSizeY))
                
        if self.direction == "down":
            if self.tier == 1:
                self.image = pygame.image.load("SoldierTier2Front.png")
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


#A function for creating the second page of game guide
def gameGuide2():
    
    #set boolean variable for the while loop 
    gameGuide2=True
    guidePic2=pygame.image.load("GameGuide2.png")
    
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
    guidePic=pygame.image.load("GameGuide.png") #load the image for gameguide page
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


#creating the menu function
def menu(attack, health,mobility, gold, scorePoint):
    interface = True
    menu=True
    while menu:
        #get the mouse's position
        mouse =pygame.mouse.get_pos()
        
        #blit pictures on screen
        screen.blit(menuSea,(0,0))
        
        pygame.draw.rect(screen,lightYellow,(250,200,400,445)) #draw pictures that are neccessary for the menu
        pygame.draw.rect(screen,(0,0,255),(260,210,380,140))
        pygame.draw.rect(screen,green,(260,350,380,140))
        pygame.draw.rect(screen,brightYellow,(260,490,380,70))
        pygame.draw.rect(screen,red,(260,560,380,70))
        
        textScreen("The Conqueror",white,0,0,100) #write texts that are neccessary for the menu
        textScreen("New Game",white,270,230,75)
        textScreen("Load Previous",black,290,360,50)
        textScreen("Game",black,320,420,50)
        textScreen("Save Game", black,280,495,60)
        textScreen("Quit", brightYellow,300,555,60)
        screen.blit(cancel,(600,200))
        
        
        for event in pygame.event.get():
            #handles what will happen when the cancel button is clicked
            if event.type== QUIT:
                menu=False
                inteface= False
                pygame.display.quit()
                
            elif event.type==MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    if mouse[0]>600 and mouse[0]<650 and mouse[1]>200 and mouse[1]<250:
                        click.play()
                        menu=False
                    #to detect if a button is cliked, Check the coordinates of X firt
                    elif mouse[0]>260 and mouse[0]<640:
                        #check for Y
                        if mouse[1]>210 and mouse[1]<350:
                            click.play()
                            #since the function of this button is to create a new game, we will rewrite the csv file
                            OverwriteF=open("UserData.csv","w+")
                            OverwriteF.close()
                            
                        elif mouse[1]>350 and mouse[1]<490:
                            click.play()
                            #open the file that contains the route in read mode
                            #open the file that contains the route in read mode
                            ReadF=open("UserData.csv","r+")
                            #format of file: Attack, Health,mobility, gold, score points, True,True,True,True
                            
                            #create a dictionary to store data
                            data=[]

                            #store information in a dictionary
                            for line in ReadF:
                                #Check if there are actully previous game history
                                if line[0] != None:
                                    #seperate the line using commas
                                    splitLine=line.split(",")
                                    # delete the /n character
                                    del splitLine[len(splitLine)-1]
                                    #store the data
                                    print(splitLine)
                                    attack = int(splitLine[0])
                                    health = int(splitLine[1])
                                    mobility = int(splitLine[2])
                                    gold = int(splitLine[3])
                                    scorePoint = int(splitLine[4])
                                    textScreen("Data retrived Successfully", black, 300,500,40)
                                else:
                                    textScreen("No data found", black, 300,500,40)
                            
                            #Close the file after it's loaded in the dictionary
                            ReadF.close()
                        elif mouse[1]>490 and mouse[1]<560:
                            click.play()
                            writeF=open("UserData.csv", "w+")
                            #make a list of attributes to store
                            attList=[attack,health,mobility,gold,scorePoint]
                            for att in attList:
                                attStr=str(att)
                                writeF.write(attStr)
                                writeF.write(",")
                            #place a None in the end as place holder
                            writeF.write("None")
                            writeF.close()
                        elif mouse[1]>560 and mouse[1]<630:
                            click.play()
                            menu=False
                            interface=False
                        
        pygame.display.update()
    return(attack, health,mobility,gold,scorePoint, interface)

#make a function for labratory
def labratory(attack, health,mobility,gold,scorePoint):
    labPic=pygame.image.load("Labratory.png") #load the background image
    
    #preset some attributes information as place holders
    Name=None                 
    buyReady=None   
    attackInfo=None
    healthInfo=None
    mobilityInfo=None
    goldInfo=None
    scorePointInfo=None

    #load the images of weapons
    HexCan=pygame.image.load("Hextech.png") #load the image of hextech gun
    HexCan=pygame.transform.scale(HexCan,(150,100))  #transform the scale of the image to appropriate size

    FireCan=pygame.image.load("FireCannon.png")
    FireCan=pygame.transform.scale(FireCan,(150,100))

    InfinityEdge=pygame.image.load("Infinity edge.png")
    InfinityEdge=pygame.transform.scale(InfinityEdge,(150,115))

    DoranBlade=pygame.image.load("Doran's Blade.png")
    DoranBlade=pygame.transform.scale(DoranBlade,(150,100))

    War=pygame.image.load("Warmog.png")
    War=pygame.transform.scale(War,(150,100))

    Relic=pygame.image.load("Relic Shield.png")
    Relic=pygame.transform.scale(Relic,(100,80))
    
    Mobility=pygame.image.load("Mobility.png")
    Mobility=pygame.transform.scale(Mobility,(150,100))

    Swift=pygame.image.load("Swift.png")
    Swift=pygame.transform.scale(Swift,(120,80))


    interface = True    
    labratory=True
    
    while labratory:
        mouse=pygame.mouse.get_pos()
        screen.blit(labPic,(0,0))
        screen.blit(cancel,(850,0))

        #blit all the weapon icons on screen
        pygame.draw.rect(screen,white,(300,90,150,100)) #draw its background
        screen.blit(DoranBlade,(290,90)) #Blit the item, DoranBlade

        pygame.draw.rect(screen,white,(500,90,150,100))
        screen.blit(InfinityEdge,(500,90))

        pygame.draw.rect(screen,white,(500,210,150,100))
        screen.blit(HexCan,(300,210))   #300 and 500 are x coordinates of weapons
        screen.blit(FireCan,(500,210))

        pygame.draw.rect(screen,white,(300,330,150,100))
        screen.blit(Relic,(320,340))
        
        pygame.draw.rect(screen,white,(500,330,150,100))
        screen.blit(War,(500,330))
        
        pygame.draw.rect(screen,white,(300,450,150,100))  #place holder
        screen.blit(Mobility,(300,450))
        
        pygame.draw.rect(screen,white,(500,450,150,100))  #place holder
        screen.blit(Swift,(520,460))
        
        pygame.draw.rect(screen,lightYellow,(0,570,900,130))
        pygame.draw.rect(screen,orange,(0,570,900,32))
        pygame.draw.rect(screen,orange,(770,660,130,40))

        textScreen("Item Name:",black,0,570,30)
        textScreen("Attack:",black,0,600,25)
        textScreen("Health:",black,225,600,25)
        textScreen("Mobility:",black,450,600,25)
        textScreen("ScorePoint:",black,0,650,30)
        textScreen("Gold:",black,300,650,30)
        textScreen("Research?",black,770,660,30)
        textScreen("Gold:",black,630,0,30)
        textScreen("Score Point:", black, 600,30,30)
        scorePointStr=str(scorePoint)
        textScreen(buyReady,black,480,630,20)
        goldStr=str(gold)
        textScreen(goldStr,black,710,0,30)
        textScreen(scorePointStr,black,750,30,30)

        textScreen(Name,black,150,570,30)
        textScreen(attackInfo,black,75,600,25)
        textScreen(healthInfo,black,300,600,25)
        textScreen(mobilityInfo,black,525,600,25)
        textScreen(scorePointInfo,black,150,650,30)
        textScreen(goldInfo,black,375,650,30)

        pygame.display.update()
        
        for event in pygame.event.get():
            
            if event.type== QUIT:
                menu=False
                inteface= False
                pygame.display.quit()
                
            elif event.type==MOUSEBUTTONDOWN:
                #resets the buy status to nothing
                buyReady=None
                if pygame.mouse.get_pressed() == (1,0,0):
                    if mouse[0]>850 and mouse[1]<50 and mouse[1]>0:
                        click.play()
                        labratory=False
                        
                    elif mouse[1]>90 and mouse[1]<190:
                        if mouse[0]>300 and mouse[0]<450:
                            #get the attributes related to the name item in the item dictionary
                            Name="Doran's Blade"
                            #use a function to find what's contained in each key
                            attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo=findAtt(Name)
                        if mouse[0]>500 and mouse[0]<650:
                            #get the attributes related to the name item in the item dictionary
                            Name="Inifinity Edge"
                            attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo=findAtt(Name)
                            
                    elif mouse[1]>210 and mouse[1]<310:
                        if mouse[0]>300 and mouse[0]<450:
                            #get the attributes related to Hextech Gun in the item dictionary
                            Name="Hextech Gun"
                            attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo=findAtt(Name)
                        if mouse[0]>500 and mouse[0]<650:
                            #get the attributes related to Fire Cannon in the item dictionary
                            Name="Fire cannon"
                            attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo=findAtt(Name)
                    elif mouse[1]>330 and mouse[1]<430:
                        if mouse[0]>300 and mouse[0]<450:
                            #get the attributes related to Relic Shield in the item dictionary
                            Name="Relic shield"
                            #use a function to find what's contained in each 
                            attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo=findAtt(Name)
                        if mouse[0]>500 and mouse[0]<650:
                            #get the attributes related to Warmog's armor in the item dictionary
                            Name="Warmog's armor"
                            attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo=findAtt(Name)
                    elif mouse[1]>450 and mouse[1]<550:
                        #Boot of mobility and Boot of swiftness
                        if mouse[0]>300 and mouse[0]<450:
                            Name="Boot of mobility"
                            attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo=findAtt(Name)
                        if mouse[0]>500 and mouse[0]<650:
                            Name="Boot of swiftness"
                            attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo=findAtt(Name)
                            
                    #hanldes if the research button is pressed
                    elif mouse[1]>660 and mouse[0]>770:
                        #checks if an item is selected
                        if Name!=None:
                            goldInfoInt=int(goldInfo)
                            scorePointInt=int(scorePointInfo)

                            #if structure checks if the player has enough money
                            if (gold-goldInfoInt)>=0 and (scorePoint-scorePointInt)>=0:
                                buyReady="Research succeeded"
                                #subtract gold and add attributes
                                gold=gold-goldInfoInt
                                attackInfoInt=int(attackInfo)
                                healthInfoInt=int(healthInfo)
                                mobilityInfoInt=int(mobilityInfo)
                                attack += attackInfoInt
                                health +=healthInfoInt
                                mobility +=mobilityInfoInt
                                
                            else:
                                buyReady="You do not have either enough Gold or Score Points"
                                
    return(attack, health,mobility,gold,scorePoint)
                            
                            
#A function to make item attributes store in variables, pass the name of the item in
def findAtt(Name):
    #find what is the values of the name, name being the item's name
    attributes=items[Name]
    attributesSplit=attributes.split(",")
    attackInfo=attributesSplit[0]
    healthInfo=attributesSplit[1]
    mobilityInfo=attributesSplit[2]
    goldInfo=attributesSplit[3]
    scorePointInfo=attributesSplit[4]
    return(attackInfo,healthInfo,mobilityInfo,goldInfo,scorePointInfo)
                
def battleIntro(battle, attack,health, mobility):
    
    if battle == "AsiaUnion":
        Pic = pygame.image.load("AsiaUnion.png")
        pygame.mixer.music.load("Hell March.mp3")
        
    elif battle == "SovietUnion":
        Pic = pygame.image.load("SovietUnion.png")
        pygame.mixer.music.load("SovietMarch.mp3")
        
    elif battle == "MiddleEastUnion":
        Pic = pygame.image.load("MiddleEastUnion.png")
        pygame.mixer.music.load("TheMass.mp3")
        
    elif battle == "NorthAmericaUnion":
        Pic = pygame.image.load("NorthAmericaUnion.png")
        pygame.mixer.music.load("OCanada.mp3")
        

    pygame.mixer.music.set_volume(5)  #plays the theme song of each battle
    pygame.mixer.music.play(-1)  #play for infinately long until the battle stops
    
    #A boolean variable used in loop
    asiaBattle=True
    highlightY = None
    back = False
    diffculty = 1
    
    while asiaBattle:
        mouse =pygame.mouse.get_pos()
        
        screen.blit(Pic,(0,0))
        screen.blit(cancel,(760,555)) #bilt the cancel button
        
        if highlightY != None:  #check if diffculty is selected
            highLight=pygame.Surface((150,43))
            highLight.set_alpha(128)   #highlight the selected diffculty
            highLight.fill(orange)
            screen.blit(highLight,(580,highlightY))
            
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                keep_going = False
                pygame.display.quit()
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    click.play()
                    
                    if mouse[0]>92 and mouse[0]<407 and mouse[1]>530 and mouse[1]<610: #check if the to batte icon is clicked
                        asiaBattle = False
                        
                    elif mouse[0]>760 and mouse[0]<810 and mouse[1]>530 and mouse[1]<610: #check if the canel icon is clicked
                        asiaBattle=False
                        back = True
                        
                    #check if diffculity level is selected
                    elif mouse[0]>580 and mouse[0]<730:
                        if mouse[1]>513 and mouse[1]<556:
                            highlightY=513
                            diffculty = 1
                        elif mouse[1]>470 and mouse[1]<513:
                            highlightY=470
                            diffculty = 1.5
                        elif mouse[1]>556 and mouse[1]<599:
                            highlightY=556
                            diffculty = 0.5
                            
    return(back, diffculty )

def gamePlay(attack, health, mobility, gold, scorePoint,soldier, tank):
    
    #character attriubutes
    health=health
    attack= attack
    mobility=mobility
    tier=1
    gold = gold
    scorePoint = scorePoint
    soldierNum = soldier
    tankNum = tank
    
    screen =pygame.display.set_mode((900,700)) # set up screen
    background = pygame.Surface(screen.get_size()).convert()
    background.fill((50, 180, 50))
    screen.blit(background, (0,0))

    enemy_group=pygame.sprite.Group()
    main_player=pygame.sprite.Group()

    player=[]
    player += [MainPlayer(health,attack,mobility)]
    #puts object in variable instead of list

    enemy=[]
    soldierNum =  int(soldierNum)
    for numberOfSoldier in range (soldierNum):
        enemy +=[Enemy(1)]

    tank = []
    tankNum =  int(tankNum)
    for numberOfTank in range (tankNum):
        tank +=[Enemy(2)]

    hole=pygame.image.load("hole.gif")

    game=True
    clock = pygame.time.Clock()
    strGold = str(gold)
    strScorePoint = str(scorePoint)

    mapUse = 0

    enemyPresence = False

    while game:
        clock.tick(30)

        stuckList=[] # a list that will be used to check if the enemy is stucked 
        
        #blit background
        screen.blit(background, (0,0))
        screen.blit(hole,(800,600))
        mapUse = player[0].mapUse
        
        if mapUse == 5: #if the player finishes all the rooms in a battle, the battle terminates
            Finish = pygame.image.load("BattleComplete.gif")
            finish = True # a while loop to display the finish screen
            
            while finish:
                screen.blit(Finish, (0,0))
                strGold = str(gold)
                strScorePoint = str(scorePoint)
                textScreen(strGold,(0,0,0),500,350,70)
                textScreen(strScorePoint,(0,0,0),630,450,70)
                
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_b:
                            finish = False
            game = False

        # draw the obstacles according to dictionary:
        for block in player[0].mapDict[player[0].mapUse]:
            pygame.draw.rect(screen,(240,120,0), (block[0],block[1],block[2],block[3]))

         #draw a status boards
        pygame.draw.rect(screen, (100,100,100), (0,0,200,150))
        textScreen("Status Board: Player" ,(200,200,200),0,0,20)
        
        strHealth=str(health)  #convert attribute informations to string so it can be blited
        strAttack= str(attack)
        strMobility = str(mobility)
        textScreen("Health:" ,(200,200,200),0,25,20) #for player
        textScreen("Attack:" ,(200,200,200),0,50,20)
        textScreen("Mobility:" ,(200,200,200),0,75,20)
        textScreen("Gold:" ,(200,200,200),0,100,20)
        textScreen("Score Point:" ,(200,200,200),0,125,20)

        if enemyPresence == True: #check if an enemy is hit, if yes, display its health
            pygame.draw.rect(screen, (100,100,100), (700,0,200,50))
            textScreen("Status Board: Enemy" ,(200,200,200),700,0,20)
            textScreen(displayHealth, (200,200,200),770,25,20)
            textScreen("Health:" ,(200,200,200),710,25,20)

        textScreen(strHealth ,(200,200,200),60,25,20)
        textScreen(strAttack,(200,200,200),50,50,20)
        textScreen(strMobility,(200,200,200),60,75,20)
        textScreen(strGold,(200,200,200),60,100,20)
        textScreen(strScorePoint,(200,200,200),90,125,20)

        for play in player:
            play.update()
            screen.blit(play.image,(play.x,play.y))

        for tanks in tank:
            tanks.mapUse = mapUse
            
            #pass in the position of the player
            tanks.updateEnemy((play.x,play.y) )
            screen.blit(tanks.image, (tanks.x , tanks.y))

        
        for enemies in enemy:
            enemies.mapUse = mapUse
            #pass in the position of the player
            enemies.updateEnemy((play.x,play.y) )
            screen.blit(enemies.image, (enemies.x , enemies.y))
        
        
        if len(enemy) == 0 and mapCurrent != mapUse:
            enemy=[]
            tank= []
            for numberOfSoldier in range (soldierNum):
                enemy +=[Enemy(1)]

            tank = []
            for numberOfTank in range (tankNum):
                tank +=[Enemy(2)]

            
        mapCurrent = mapUse
        duplicatingList = []
            
        for bullet in player[0].bulletList:
            #draw each bullets on screen
            pygame.draw.circle(screen,(0,0,0),(int(bullet[0]), int(bullet[1])), 10,0)
            
            for eachEnemy in enemy:
                if checkCollisionRect((bullet[0],bullet[1]),10,10,(eachEnemy.x,eachEnemy.y), eachEnemy.imageSizeX, eachEnemy.imageSizeY):
                    #delete the bullet if the bullet colides with the enemy
                    bulletPointer = player[0].bulletList.index(bullet)
                    
                    duplicatingList += [(player[0].bulletList[bulletPointer])]

                    enemyPresence = True
                    #bullet[3] is the atack damage, use enemy health minus attack damage of the bullet
                    eachEnemy.health -= bullet[3]
                    displayHealth = str(eachEnemy.health)
                    
                    #show the health points of the enemy
                    textScreen("health:" ,(200,10,30),eachEnemy.x,eachEnemy.y - 20,20)
                    textScreen( displayHealth ,(200,10,30),eachEnemy.x +50 ,eachEnemy.y - 20,20)
                    
                    #removes an enemy from the list when its health point is below zero
                    if eachEnemy.health <= 0:
                        pointer = enemy.index(eachEnemy)
                        del(enemy[pointer])
                        #increment gold and score points
                        gold +=20
                        scorePoint +=10
                        strGold = str(gold)
                        strScorePoint = str(scorePoint)
                        
            for eachEnemy in tank:
                if checkCollisionRect((bullet[0],bullet[1]),10,10,(eachEnemy.x,eachEnemy.y), eachEnemy.imageSizeX, eachEnemy.imageSizeY):
                    #delete the bullet if the bullet colides with the enemy
                    bulletPointer = player[0].bulletList.index(bullet)
                    
                    duplicatingList += [(player[0].bulletList[bulletPointer])]

                    enemyPresence = True
                    #bullet[3] is the atack damage, use enemy health minus attack damage of the bullet
                    eachEnemy.health -= bullet[3]
                    displayHealth = str(eachEnemy.health)
                    
                    #show the health points of the enemy
                    textScreen("health:" ,(200,10,30),eachEnemy.x,eachEnemy.y - 20,20)
                    textScreen( displayHealth ,(200,10,30),eachEnemy.x +50 ,eachEnemy.y - 20,20)
                    
                    #removes an enemy from the list when its health point is below zero   
                    if eachEnemy.health <= 0:
                        pointer = tank.index(eachEnemy)
                        del(tank[pointer])
                        #increment gold and score points
                        gold += 50
                        scorePoint += 25
                        strGold = str(gold)
                        strScorePoint = str(scorePoint)
                            
        #delete bullets, use list(set()) to delete duplicated bullets first
        duplicatingList = list(set(duplicatingList))
        for i in duplicatingList:
            bulletPointer = player[0].bulletList.index(i)
            del (player[0].bulletList[bulletPointer])
            
        #handle the enemy's bullets
        for Eachenemy in enemy:
            for bullet in Eachenemy.shootList:
                pygame.draw.circle(screen,(255,0,0),(int(bullet[0]), int(bullet[1])), 10,0)
                if checkCollisionRect((bullet[0],bullet[1]),10,10,(play.x,play.y), play.imageX, play.imageY):
                    play.health -= bullet[3]
                    health = play.health
                    
                    #delete the bullet if the bullet colides with the player
                    enemyBulletPointer = Eachenemy.shootList.index(bullet)
                    del (Eachenemy.shootList[enemyBulletPointer])
                    
            #handle the enemy's bullets
        for Eachenemy in tank:
            for bullet in Eachenemy.shootList:
                pygame.draw.circle(screen,(0,0,255),(int(bullet[0]), int(bullet[1])), 20,0)
                if checkCollisionRect((bullet[0],bullet[1]),10,10,(play.x,play.y), play.imageX, play.imageY):
                    play.health -= bullet[3]
                    health = play.health
                    
                    #delete the bullet if the bullet colides with the player
                    enemyBulletPointer = Eachenemy.shootList.index(bullet)
                    del (Eachenemy.shootList[enemyBulletPointer])
                    
              
        #if the player drops to 0 health
        if play.health <=0 :
            Back = True
            while Back:
                end = pygame.image.load("EndofBattle.gif")
                screen.blit(end, (0,0))
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_b:
                                health = 20
                                Back =False
                                game =False
                    
                #quit the game loop
                
            
        
        pygame.display.update()
    return (health, gold, scorePoint)

#find background picture for menu
menuSea=pygame.image.load("menuSea.png")
cancel=pygame.image.load("cancel.png") #picture for the cancel button
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

introImg=pygame.image.load('IntroScreen.png')
introImg=pygame.transform.scale(introImg,(full_size))


#set boolean variables for each stage of the game
introscreen=True
interface=True


#Colours:
red=(230,0,0)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
lightYellow=(200,250,204)
orange=(255,165,0)
brightYellow=(244,219,3)
#create variables to represent status in the game
health=20
attack=1
mobility=10
gold=0
scorePoint=0

#A dictionary that is used to store the list of items in labratory
#"attack,health,mobility,Gold cosy,Score point"
items={"Doran's Blade":"1,0,0,150,100","Inifinity Edge":"2,0,1,300,150","Hextech Gun":"3,0,2,400,200","Fire cannon":"4,0,2,600,400","Relic shield":"0,10,0,300,150","Warmog's armor":"0,30,0,600,300","Boot of mobility":"0,0,3,200,100","Boot of swiftness":"0,0,4,400,200"}


#set sounds files
click = pygame.mixer.Sound(file="click.wav") #used for a sound effect

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
            
seaImg=pygame.image.load('Sea.png')

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
                        backG=pygame.image.load("Black.png")
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


#program cancel picture to cancel
#program diffculty levels
