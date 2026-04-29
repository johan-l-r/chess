import pygame as pg

from base.piece import Piece 

pg.init()

class Highlight: 
  def __init__(self, hint_size): 
    # semitransparent colors
    self.VALID_MOVE = (22, 128, 46, 128)
    self.INVALID_MOVE = (107, 107, 107, 128)
    self.CAPTURE_MOVE = (196, 64, 27, 128)

    self.tile_size = hint_size

    self.highlights = []

  def create_highlights(self, board, row, col, piece): 
    valid_moves, invalid_moves, capture_moves = piece.get_moves(board, row, col)

    for row, col in valid_moves:
      tile = pg.Surface(
        (self.tile_size, self.tile_size), 
        pg.SRCALPHA
      )

      tile.fill(self.VALID_MOVE)
      self.highlights.append((row, col, tile))

    for row, col in capture_moves: 
      tile = pg.Surface(
        (self.tile_size, self.tile_size), 
        pg.SRCALPHA
      )

      tile.fill(self.CAPTURE_MOVE)
      self.highlights.append((row, col, tile))

  def clear_hilights(self): self.highlights.clear()

  def draw(self, master, center_x, center_y): 
    for row, col, hint in self.highlights: 
      master.blit(hint, (col * self.tile_size + center_x, row * self.tile_size + center_y))

