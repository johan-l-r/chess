from os import truncate
import pygame as pg 

from components.tile import Tile
from highlight import Highlight
from pieces.pawn import Pawn
from pieces.knight import Knight

pg.init()

class Board: 
  def __init__(self, window_width, window_height): 
    self.tile_size = 64
    self.MAX_TILES = 8
    self.BOARD_SIZE = self.tile_size * self.MAX_TILES

    self.center_x = (window_width - self.BOARD_SIZE) // 2
    self.center_y = (window_height - self.BOARD_SIZE) // 2

    self.selected_tile = None

    self.hilight = Highlight(self.tile_size)

    self.coordinates = []
    self.possible_moves = []

    # fill matrix with coordinates
    for i in range(self.MAX_TILES): 
      row = []

      for j in range(self.MAX_TILES): 
        tile = Tile(
          self.tile_size, 
          self.tile_size,
          j * self.tile_size + self.center_x, 
          i * self.tile_size + self.center_y, 
          i, 
          j
        )
        row.append(tile)

      self.coordinates.append(row)

    self.coordinates[6][0].add_child(Pawn(
      "./assets/imgs/pawn.png", 
      self.tile_size, 
      self.tile_size, 
      6
    ))
    self.coordinates[5][1].add_child(Pawn(
      "./assets/imgs/pawn.png", 
      self.tile_size, 
      self.tile_size, 
      6
    ))
    self.coordinates[6][1].add_child(Pawn(
      "./assets/imgs/pawn.png", 
      self.tile_size, 
      self.tile_size, 
      5
    ))
    self.coordinates[7][1].add_child(Knight(
      "./assets/imgs/knight.png", 
      self.tile_size, 
      self.tile_size
    ))

    self.color_board()

  def color_board(self): 
    for row in self.coordinates: 
      for tile in row: 
        # set color one time
        if (tile.get_row() + tile.get_col()) % 2 == 0:
          tile.set_color((131, 122, 105))
        else:
          tile.set_color((179, 170, 153))

  def is_target_empty(self, row, col): 
    return self.coordinates[row][col].is_empty()

  def is_valid_position(self, row, col): 
    if row >= 0 and col >= 0 and \
      row < self.MAX_TILES and col < self.MAX_TILES:
      return True 

    return False 

  def move_piece(self, current_tile: Tile, target_tile: Tile): 
    target_tile.add_child(current_tile.get_child())
    current_tile.remove_child()

  def select_tile(self, tile): 
    self.hilight.clear_hilights()
    self.selected_tile = tile

    if tile is None: 
      return

    piece = tile.get_child()


    self.hilight.create_highlights(
      self, 
      tile.get_row(), 
      tile.get_col(), 
      piece
    )

    self.possible_moves = piece.get_moves(
      self, 
      tile.get_row(), 
      tile.get_col()
    )[0]

  def handle_clicked_tile(self, tile): 
    if self.selected_tile is None:  
      if not tile.is_empty(): 
        self.select_tile(tile)
    else:
      if not tile.is_empty(): 
        # if another piece is clicked then reselect tile
        self.select_tile(tile)

        return

      target = (tile.get_row(), tile.get_col())

      # deselect tile if target is not a possible move
      if tile.is_empty() and target not in self.possible_moves: 
        self.select_tile(None)

      if target in self.possible_moves: 
        self.move_piece(self.selected_tile, tile)

      self.selected_tile = None
      self.possible_moves = []
      self.hilight.clear_hilights() # clear highlight list after piece movement

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

    self.hilight.draw(master, self.center_x, self.center_y)

