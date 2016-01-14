import pygame
 
pygame.init()
 
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
PI = 3.141592653
 

size = (400, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Title")
 
done = False
clock = pygame.time.Clock()
 
def recursived(start):
    pygame.draw.rect(screen, BLACK, [start, start, 400-2*start, 500-2*start], 1)
    if start <= 200:
        recursived(start+5)
  
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
 
    screen.fill(WHITE)
    recursived(0)
    
    pygame.display.flip()
 

    clock.tick(60)
     
 
pygame.quit()

