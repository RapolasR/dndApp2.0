
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

# path variables 

base_path = os.path.dirname(__file__)
path = os.path.join(base_path, "enemies")

iEnemy = None

# *** Klase
class Enemy:
    def __init__(self, name):
        self.name = name

# *** funkcijos
def drawButton(text, x, y, w, h, color = (0,0,0), fSize = 40):
    buttonRect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, buttonRect)

    font = pygame.font.SysFont(None, fSize)
    txt = font.render(text, True, (255, 255, 255))
    txt_rect = txt.get_rect(center=buttonRect.center)

    screen.blit(txt, txt_rect)
    return buttonRect

def find_all_enemies(path):
    files = []
    if not os.path.isdir(path):
        return files
    for entry in os.scandir(path):
        if entry.is_file() and entry.name.lower().endswith('.json'):
            files.append(entry.path)
    return files


def load_enemy_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None


def load_all_enemies(path):
    files = find_all_enemies(path)
    loaded = []
    for fp in files:
        data = load_enemy_file(fp)
        if data is not None:
            loaded.append((fp, data))
    return loaded



#variables n' stuff
enemies = []    
dice = [('d20', 20), ('d12', 12), ('d10', 10), ('d8', 8), ('d6', 6), ('d4', 4)]


baseXdice = 225
addXdice = 150


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
            elif activeF ==1:
                if addEnemyButton.collidepoint(e.pos):
                        print('addEnemy Clicked')
                        loaded = load_all_enemies(path)
                        print(loaded)



            elif activeF == 2: 
                for button in rDice:
                    Button, value = button
                    if Button.collidepoint(e.pos):
                        print(r.randint(0, value))




    # flip() parodytu display
    pygame.display.flip()

    clock.tick(30)  # FPS to 30

pygame.quit()