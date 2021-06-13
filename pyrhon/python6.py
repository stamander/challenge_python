import pygame
print(pygame)

import sys
import pygame
from pygame.locals import QUIT


def main():
  pygame.init()
  surface = pygame.display.set_mode((400,300))
  clock = pygame.time.Clock()
  icon = pygame.image.load("/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pygame/pygame_icon.bmp").convert()
  (x,y) = (
    surface.get_rect().centerx - icon.get_rect().width/2,\
    surface.get_rect().centery - icon.get_rect().height/2
    )



  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        
        sys.exit()


    surface.fill((0,0,255))
    surface.blit(icon,(x,y))
    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()