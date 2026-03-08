
import enum
from re import escape
import pygame
import os 
import sys
import json
import random as r


# *** pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


# ***frames
activeF = 1
# *0 - test screen
# *1 - main screen
# *2 - roll screen
# *3 - enemy screen
# *3.1 - enemy add screen

# path variables 

base_path = os.path.dirname(__file__)
path = os.path.join(base_path, "enemies")

iEnemy = None

# *** Klase
class Enemy:
    def __init__(self, name, ac, hp, dex, ath, intel, wStats, note = 'No note'):
        self.name = name
        self.ac = ac
        self.hp = hp
        self.dex = dex
        self.ath = ath
        self.intel = intel
        self.wStats = wStats








# *** funkcijos
def drawButton(text, x, y, w, h, color = (0,0,0), fSize = 40):
    buttonRect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, buttonRect)

    font = pygame.font.SysFont(None, fSize)
    txt = font.render(text, True, (255, 255, 255))
    txt_rect = txt.get_rect(center=buttonRect.center)

    screen.blit(txt, txt_rect)
    return buttonRect





def viewFolder(path):
    stats = []
    for i in os.scandir(path):
        if i.is_file():
            print(f'File - {i.path}')
            if i.path.endswith('.json'):
                stats.append(i.path)
    return stats



#variables n' stuff
enemies = []

addEnemies = []
eScanned = False
dice = [('d20', 20), ('d12', 12), ('d10', 10), ('d8', 8), ('d6', 6), ('d4', 4)]

#base coordinates
baseXdice = 225
addXdice = 150

baseXaddE = 100
baseYaddE = 100

while running:


    rDice = []   #rendered Dice

    

    # uzpildyt ekrana
    screen.fill("purple")

    # render cia
    # --------------------------------frame'ai--------------------------------------

    # ------------------------------universal---------------------------------------
    backButton = drawButton('BACK', 1030, 0, 250, 50, (158, 2, 9))
    
    rollButton = drawButton('Roll', 830, 0, 200, 50)

    # --------------------------------0---------------------------------------------
    
    if activeF == 0:  
        testButton = drawButton("test", 50, 50, 500, 250)

    # -------------------------------1 = main screen -------------------------------

    if activeF == 1:
        addEnemyButton = drawButton('Add enemy', 580, 0, 250, 50)

    # --------------------------------2---------------------------------------------
    if activeF == 2:
        
        for index, die in enumerate(dice):
            dName, value = die
            addx = addXdice * index

            dButton = drawButton(dName, baseXdice + addx, 200, 100, 100)
            rDice.append((dButton, value))

    # --------------------------------3---------------------------------------------

    # --------------------------------3.1-------------------------------------------
    if activeF == 3.1:
        if eScanned == False:
            for fPath in fPaths:
                with open(fPath, 'r', encoding='UTF-8') as file:
                    data = json.load(file)
                data = json.dumps(data)
                stats = json.loads(data)
                enemy = Enemy(stats["name"], stats["ac"], stats["hp"], stats["dexterity"], stats["athletics"], stats["intelegence"], stats["wStats"], stats["note"])
                addEnemies.append(enemy)
            print(addEnemies)
            eScanned = True

        for index, enemy in enumerate(addEnemies):
            addX = 200 * index
            enemyButton = drawButton(enemy.name, baseXaddE + addX, baseYaddE, 200, 50)

        




        
            
        




            
        





    


        







    #event handling

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:

            if backButton.collidepoint(e.pos):
                activeF = 1
            elif rollButton.collidepoint(e.pos):
                activeF = 2


            if activeF == 0: #jei esam test frame'e
                if testButton.collidepoint(e.pos):
                    print('67 test')
            elif activeF == 1:
                if addEnemyButton.collidepoint(e.pos):
                    fPaths = viewFolder(path)
                    activeF = 3.1



            elif activeF == 2: 
                for button in rDice:
                    Button, value = button
                    if Button.collidepoint(e.pos):
                        print(r.randint(0, value))

            elif activeF == 3.1:
                for button in addEnemies:
                    if button.collidepoint(e.pos):
                        enemies.add




    # flip() parodytu display
    pygame.display.flip()

    clock.tick(30)  # FPS 30

pygame.quit()
