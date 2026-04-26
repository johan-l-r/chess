import pygame as pg

from base.piece import Piece 

pg.init()

class Highlight: 
  def __init__(self, hint_size): 
    # semitransparent colors
    self.VALID_MOVE = (52, 235, 125, 128)
    self.INVALID_MOVE = (107, 107, 107, 128)
    self.CAPTURE_MOVE = (161, 14, 14, 128)

    self.tile_size = hint_size

    self.highlights = []

  def create_highlights(self, board, row, col, piece): 
    valid_moves = piece.get_moves(board, row, col)[0]
    invalid_moves = piece.get_moves(board, row, col)[1]

    for row, col in valid_moves:
      tile = pg.Surface(
        (self.tile_size, self.tile_size), 
        pg.SRCALPHA
      )

      tile.fill(self.VALID_MOVE)
      self.highlights.append((row, col, tile))

  def clear_hilights(self): self.highlights.clear()

  def draw(self, master): 
    for row, col, hint in self.highlights: 
      master.blit(hint, (col * self.tile_size, row * self.tile_size))

