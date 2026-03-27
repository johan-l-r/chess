import pygame as pg 

pg.init()

class Board: 
  def __init__(self): 
    self.tile_size = 64
    self.MAX_TILES = 8

  def draw(self, master: pg.Surface): 
    color = (0, 0, 0)

    for i in range(self.MAX_TILES): 
      for j in range(self.MAX_TILES):
        tile = pg.Rect(i * self.tile_size, j * self.tile_size, self.tile_size, self.tile_size) 

        if (i + j) % 2 != 0: 
          color = (255, 255, 255)
        else:
          color = (0, 0, 0)

        pg.draw.rect(master, color, tile)

