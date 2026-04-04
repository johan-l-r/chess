from os import truncate
import pygame as pg 

from components.tile import Tile
from pieces.pawn import Pawn

pg.init()

class Board: 
  def __init__(self): 
    self.tile_size = 64
    self.MAX_TILES = 8

    self.selected_tile = None

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

    self.coordinates[6][0].add_child(Pawn(
      "./assets/imgs/pawn.png", 
      self.tile_size, 
      self.tile_size
    ))
    self.coordinates[1][0].add_child(Pawn(
      "./assets/imgs/pawn.png", 
      self.tile_size, 
      self.tile_size
    ))

  def is_target_empty(self, row, col): 
    if self.coordinates[row][col].is_empty():
      return True 

    return False

  def move_piece(self, current_tile: Tile, target_tile: Tile): 
    target_tile.add_child(current_tile.get_child())
    current_tile.remove_child()

  def handle_clicked_tile(self, tile): 
    if self.selected_tile is None:  
      if not tile.is_empty(): 
        self.selected_tile = tile

    else:
      piece = self.selected_tile.get_child()
      moves = piece.get_possible_moves(
        self,
        self.selected_tile.get_row(), 
        self.selected_tile.get_col()
      )

      target = (tile.get_row(), tile.get_col())

      if target in moves: 
        self.move_piece(self.selected_tile, tile)

      self.selected_tile = None

  def handle_event(self, event):
    if event.type == pg.MOUSEBUTTONDOWN: 
      mouse_pos = pg.mouse.get_pos() 

      for row in self.coordinates: 
        for tile in row: 
          if tile.is_clicked(mouse_pos): 
            self.handle_clicked_tile(tile)

  def draw(self, master: pg.Surface): 
    for row in self.coordinates:
      for tile in row: 
        if (tile.get_row() + tile.get_col()) % 2 == 0:
          tile.set_color((242, 212, 148))
        else:
          tile.set_color((107, 77, 12))

        tile.draw(master)
