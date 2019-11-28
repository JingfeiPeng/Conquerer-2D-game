import pygame 
from pygame.locals import *

# change sys path to root
import sys
sys.path.append('../')


from util.utils import *

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
                            
                  