import pygame

WIDTH, HEIGHT =  576, 1024
FPS = 120 # frames per second

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS) # FPS == 120 Frames per Second

# 14:23
 
