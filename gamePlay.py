import pygame 
from pygame.locals import *

from components.player import MainPlayer
from components.enemy import Enemy

from util.utils import *

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
