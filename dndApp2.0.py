
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


#frames
activeF = 0
# 0 - test screen




class Enemy:
    def __init__(self, name):
        self.name = name


def drawButton(text, x, y, w, h, color = (0,0,0), fSize = 40):
    buttonRect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, buttonRect)

    font = pygame.font.SysFont(None, fSize)
    txt = font.render(text, True, (255, 255, 255))
    txt_rect = txt.get_rect(center=buttonRect.center)

    screen.blit(txt, txt_rect)
    return buttonRect

while running:




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # uzpildyt ekrana
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    
    if activeF == 0:
        testButton = drawButton("test", 50, 50, 500, 250)







    # flip() parodytu display
    pygame.display.flip()

    clock.tick(30)  # FPS to 30

pygame.quit()