import pygame 
from pygame.locals import *

# change sys path to root
import sys
sys.path.append('../')


from util.utils import *

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
