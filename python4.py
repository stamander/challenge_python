import sys 
import pygame
from pygame.locals import QUIT


def main():
  pygame.init() #pygame初期化
  surface = pygame.display.set_mode((300,300)) #描写用のウインドウ初期化
  pygame.display.set_caption("Hello pygame") #ウィンドウにタイトルを設定
  clock = pygame.time.Clock() #クロックオブジェクトでフレームレイトを指定
  font = pygame.font.Font(None, 30) #filename,sizeの順 ここではnoneを指定
  text = font.render("Hello Pygame",True,(10,10,10)) #renderメソッドを使って指定した文字を新規Surfaceに追加
  textpos = text.get_rect()
  textpos.centerx = surface.get_rect().centerx #x座標の中心
  textpos.centery = surface.get_rect().centery #y座標の中心

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    surface.fill((255,255,255))
    surface.blit(text,textpos)
    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()




