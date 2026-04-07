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
    self.possible_moves = []

    # fill matrix with coordinates
    for i in range(self.MAX_TILES): 
      row = []

      for j in range(self.MAX_TILES): 
        tile = Tile(
          self.tile_size, 
          self.tile_size,
          j * self.tile_size,  
          i * self.tile_size, 
          i, 
          j
        )
        row.append(tile)

      self.coordinates.append(row)

    self.coordinates[6][0].add_child(Pawn(
      "./assets/imgs/pawn.png", 
      self.tile_size, 
      self.tile_size
    ))
    self.coordinates[6][1].add_child(Pawn(
      "./assets/imgs/pawn.png", 
      self.tile_size, 
      self.tile_size
    ))

    self.color_board()

  def color_board(self): 
    for row in self.coordinates: 
      for tile in row: 
        # set color one time
        if (tile.get_row() + tile.get_col()) % 2 == 0:
          tile.set_color((242, 212, 148))
        else:
          tile.set_color((107, 77, 12))

  def is_target_empty(self, row, col): 
    if self.coordinates[row][col].is_empty():
      return True 

    return False

  def highlight_moves(self): 
    if self.selected_tile is not None: 
      for row, col in self.possible_moves: 
        if (row + col) % 2 == 0: 
          self.coordinates[row][col].set_color((52, 235, 125))
        else: 
          self.coordinates[row][col].set_color((35, 166, 87))
    else: 
      self.color_board()

  def move_piece(self, current_tile: Tile, target_tile: Tile): 
    target_tile.add_child(current_tile.get_child())
    current_tile.remove_child()

  def handle_clicked_tile(self, tile): 
    if self.selected_tile is None:  
      if not tile.is_empty(): 
        # select tile and calculate moves
        self.selected_tile = tile

        piece = self.selected_tile.get_child()

        self.possible_moves = piece.get_possible_moves(
          self,
          self.selected_tile.get_row(), 
          self.selected_tile.get_col()
        )
    else:
      if not tile.is_empty(): 
        # if another piece is clicked then reselect tile
        self.selected_tile = tile

        piece = tile.get_child()

        self.possible_moves = piece.get_possible_moves(
          self,
          tile.get_row(), 
          tile.get_col()
        )
        return 

      target = (tile.get_row(), tile.get_col())

      if target in self.possible_moves: 
        self.move_piece(self.selected_tile, tile)

      self.selected_tile = None
      self.possible_moves = []

    self.highlight_moves()

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
        tile.draw(master)
