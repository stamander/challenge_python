import sys
import pygame
from pygame.locals import QUIT

def main():
  pygame.init()
  surface = pygame.display.set_mode((300,400))
  pygame.display.set_caption("Mickey move")
  clock = pygame.time.Clock()
  x = surface.get_rect().centerx
  y=400

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    surface.fill((255,255,255))
    if y < surface.get_rect().bottom +10:
      y -=10
    pygame.draw.circle(surface,(255,0,0),(x,y),20) #縁を描画
    pygame.draw.circle(surface,(255,0,0),(x+20,y-20),10)
    pygame.draw.circle(surface,(255,0,0),(x-20,y-20),10)
    pygame.display.update()
    clock.tick(10)


if __name__=='__main__':
  main()