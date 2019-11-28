import pygame 
from pygame.locals import *

# change sys path to root
import sys
sys.path.append('../')

from util.utils import *

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
                            print(ReadF)
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
