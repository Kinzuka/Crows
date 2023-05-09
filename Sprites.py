## Tile
import pygame


class Tile(pygame.sprite.Sprite):
  def __init__(self,pos,groups):
    super().__init__(groups)
    self.size = (32,32)
    self.image = pygame.transform.scale(pygame.image.load('/Users/siddharth/Desktop/Python/kenney_tiny-dungeon/Tiles/tile_0014.png').convert_alpha(),self.size)
    self.rect = self.image.get_rect(topleft = pos)

class Player(pygame.sprite.Sprite):
  def __init__(self,pos,groups,obstacle_sprites):
    super().__init__(groups)
    self.size = (32,32)
    self.image = pygame.transform.scale(pygame.image.load('/Users/siddharth/Desktop/Python/kenney_tiny-dungeon/Tiles/tile_0097.png').convert_alpha(),self.size)
    self.rect = self.image.get_rect(topleft = pos)
    self.obstacle_sprites = obstacle_sprites

    self.direction = pygame.math.Vector2()
    self.speed = 0.005

  def input(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
      self.direction.y = 1
    elif key[pygame.K_DOWN]:
      self.direction.y = -1
    else: self.direction.y = 0
    
    
    if key[pygame.K_RIGHT]:
      self.direction.x = 1
    elif key[pygame.K_LEFT]:
      self.direction.x = -1
    else: self.direction.x = 0
  
    
  def collision(self,direction):
    if direction == 'horizontal':
      for sprite in self.obstacle_sprites:
        if sprite.rect.colliderect(self.rect):
          if self.direction.x>0:
            self.rect.right = sprite.rect.left
          if self.direction.x<0:
            self.rect.left = sprite.rect.right
    if direction == 'vertical':
      for sprite in self.obstacle_sprites:
          if self.direction.y>0:
            self.rect.bottom = sprite.rect.top
          if self.direction.y<0:
            self.rect.top = sprite.rect.bottom
  
  def move(self,speed):
    if self.direction.magnitude() != 0:
      self.direction = self.direction.normalize()
    self.rect.x+=self.direction.x*speed
    self.collision('horizontal')
    self.rect.y+=self.direction.y*speed
    self.collision('vertical')
    
    #self.rect.centre+=self.direction*speed


  def update(self):
    self.input()
    self.move(self.speed)
    