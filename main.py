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
from components.player import MainPlayer
from components.enemy import Enemy
from screens.gameGuide import gameGuide, gameGuide2
from screens.menu import menu

#make a function for labratory
def labratory(attack, health,mobility,gold,scorePoint):
    labPic=pygame.image.load("assets/images/Labratory.png") #load the background image
    
    #preset some attributes information as place holders
    Name=None                 
    buyReady=None   
    attackInfo=None
    healthInfo=None
    mobilityInfo=None
    goldInfo=None
    scorePointInfo=None

    #load the images of weapons
    HexCan=pygame.image.load("assets/images/Hextech.png") #load the image of hextech gun
    HexCan=pygame.transform.scale(HexCan,(150,100))  #transform the scale of the image to appropriate size

    FireCan=pygame.image.load("assets/images/FireCannon.png")
    FireCan=pygame.transform.scale(FireCan,(150,100))

    InfinityEdge=pygame.image.load("assets/images/Infinity edge.png")
    InfinityEdge=pygame.transform.scale(InfinityEdge,(150,115))

    DoranBlade=pygame.image.load("assets/images/Doran's Blade.png")
    DoranBlade=pygame.transform.scale(DoranBlade,(150,100))

    War=pygame.image.load("assets/images/Warmog.png")
    War=pygame.transform.scale(War,(150,100))

    Relic=pygame.image.load("assets/images/Relic Shield.png")
    Relic=pygame.transform.scale(Relic,(100,80))
    
    Mobility=pygame.image.load("assets/images/Mobility.png")
    Mobility=pygame.transform.scale(Mobility,(150,100))

    Swift=pygame.image.load("assets/images/Swift.png")
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
                            
                        
                
def battleIntro(battle, attack,health, mobility):
    
    if battle == "AsiaUnion":
        Pic = pygame.image.load("assets/images/AsiaUnion.png")
        pygame.mixer.music.load("assets/sounds/Hell March.mp3")
        
    elif battle == "SovietUnion":
        Pic = pygame.image.load("assets/images/SovietUnion.png")
        pygame.mixer.music.load("assets/sounds/SovietMarch.mp3")
        
    elif battle == "MiddleEastUnion":
        Pic = pygame.image.load("assets/images/MiddleEastUnion.png")
        pygame.mixer.music.load("assets/sounds/TheMass.mp3")
        
    elif battle == "NorthAmericaUnion":
        Pic = pygame.image.load("assets/images/NorthAmericaUnion.png")
        pygame.mixer.music.load("assets/sounds/OCanada.mp3")
        

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
    
    screen = pygame.display.set_mode((width, height)) # set up screen
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

    hole=pygame.image.load("assets/images/hole.gif")

    game=True
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
            Finish = pygame.image.load("assets/images/BattleComplete.gif")
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
                end = pygame.image.load("assets/images/EndofBattle.gif")
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


#program cancel picture to cancel
#program diffculty levels
