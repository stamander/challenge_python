import sys
import pygame
from random import randint
from math import sin, cos, radians
from pygame.locals import QUIT


def main():
  pygame.init()
  surface = pygame.display.set_mode((400,400))
  pygame.display.set_caption("mickey bounds")
  clock = pygame.time.Clock()
  x = 0
  y = 0
  dir = randint(20,70) #dirに発車角を代入
  print(dir)
  speed = 10
  while True:
    if x < 0 or x > 390: #跳ね返り処理
      dir = 180 - dir
      print(dir)


    if y<0 or y> 390:#跳ね返り処理　
      dir = -dir
      print(dir)
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    surface.fill((255,255,255))
    x+= cos(radians(dir)) * speed
    y+= sin(radians(dir)) * speed
    pygame.draw.circle(surface,(255,0,0),(int(x),int(y)),20)
    pygame.draw.circle(surface,(255,0,0),(int(x+20),int(y-20)),10)
    pygame.draw.circle(surface,(255,0,0),(int(x-20),int(y-20)),10)
    pygame.display.update()
    clock.tick(10)


if __name__ == '__main__':
  main()
