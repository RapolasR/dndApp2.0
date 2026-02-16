
import pygame

# *** pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


# ***frames
activeF = 1
# *0 - test screen
# *1 - main screen



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


#stuff
enemies = []




while running:




    

    # uzpildyt ekrana
    screen.fill("purple")

    # render cia
    # --------------------------------frame'ai--------------------------------------

    # --------------------------------0---------------------------------------------
    
    if activeF == 0:  
        testButton = drawButton("test", 50, 50, 500, 250)

    # --------------------------------1---------------------------------------------

    if activeF == 1: 
        if enemies == []:
            print(67)







    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if activeF == 0: #jei esam test frame'e
                if testButton.collidepoint(e.pos):
                    print('67 test')




    # flip() parodytu display
    pygame.display.flip()

    clock.tick(30)  # FPS to 30

pygame.quit()