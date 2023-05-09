import pygame,sys
from Sprites import *
from Generation import *

w_width = 1280
w_length = 720
FPS = 60
Tilesize = 32
FLOOR_MAP = []
for i in list(floor_map().values()):
  FLOOR_MAP.append(i)
print(FLOOR_MAP)



class Level:
  def __init__(self):
    self.visible_sprites = pygame.sprite.Group()
    self.obstacle_sprites = pygame.sprite.Group()
    self.display_surface = pygame.display.get_surface()
    self.create_map()

  def create_map(self):
    for row_index,row in enumerate(FLOOR_MAP):
      for col_index, col in enumerate(row):
        x = col_index*Tilesize
        y = row_index*Tilesize
        if col == 1:
          self.visible_sprites.add(Tile((x,y),[self.visible_sprites,self.obstacle_sprites]))
        if col == -1:
          self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
          self.visible_sprites.add(self.player)

  
  def run(self):
    # update and run the game
    self.visible_sprites.draw(self.display_surface)
    self.visible_sprites.update()


class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((w_width, w_length))
        pygame.display.set_caption('Crows')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)  # <-- maximum framerate


if __name__ == '__main__':
    game = Game()
    game.run()
