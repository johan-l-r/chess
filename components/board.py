import pygame as pg 

from components.tile import Tile
from pieces.pawn import Pawn

pg.init()

class Board: 
  def __init__(self): 
    self.tile_size = 64
    self.MAX_TILES = 8

    self.coordinates = []

    # fill matrix with coordinates
    for i in range(self.MAX_TILES): 
      row = []

      for j in range(self.MAX_TILES): 
        self.tile = Tile(
          self.tile_size, 
          self.tile_size,
          j * self.tile_size,  
          i * self.tile_size, 
          i, 
          j
        )
        row.append(self.tile)

      self.coordinates.append(row)

  def handle_event(self, event):
    if event.type == pg.MOUSEBUTTONDOWN:
      mouse_pos = pg.mouse.get_pos()

      for row in self.coordinates:
        for tile in row: 
          if tile.get_rect().collidepoint(mouse_pos):
            # testing
            print(f"row {tile.get_row()} col {tile.get_col()}")

  def draw(self, master: pg.Surface): 
    for row in self.coordinates:
      for tile in row: 
        if (tile.get_row() + tile.get_col()) % 2 == 0:
          tile.set_color((242, 212, 148))
        else:
          tile.set_color((107, 77, 12))

        tile.draw(master)
