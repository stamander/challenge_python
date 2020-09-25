import sys 
import pygame
from pygame.locals import QUIT

def main():
  pygame.init() #pygame初期化
  surface = pygame.display.set_mode((300,400)) #描写用のウインドウ初期化
  pygame.display.set_caption("Pygame draw")
  clock = pygame.time.Clock()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    surface.fill((255,255,255))
    pygame.draw.rect(surface,(255,255,0),(50,10,80,40),5) #pygame.draw.rect(surface,color,rect,width = 0)
    pygame.draw.rect(surface,(0,255,255),(150,10,80,40))


    pygame.draw.circle(surface,(255,0,255),(100,100),20,5) #pygame.draw.cicle(surface,color,pos(座標),radius,width = 0)
    pygame.draw.circle(surface,(255,0,255),(80,80),15,5)
    pygame.draw.circle(surface,(255,0,255),(120,80),15,5)

    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()
