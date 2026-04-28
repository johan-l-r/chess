import pygame as pg
from base.piece import Piece

pg.init()

class Pawn(Piece): 
  def __init__(self, path, width, height, original_row): 
    super().__init__(path, width, height)
    
    self.original_row = original_row

  def get_moves(self, board, row, col) -> tuple:
    super().get_moves(board, row, col)

    valid_moves = []
    invalid_moves = []
    capture_moves = []

    # capture logic
    if not board.is_target_empty(row - 1, col + 1): 
      capture_moves.append((row - 1, col + 1))
    if not board.is_target_empty(row - 1, col - 1): 
      capture_moves.append((row - 1, col - 1))

    # prevent piece jumping
    if board.is_target_empty(row - 1, col):
      valid_moves.append((row - 1, col))
      
      if board.is_target_empty(row - 2, col) and self.original_row == row: 
        valid_moves.append((row - 2, col))
      else:
        invalid_moves.append((row - 2, col))
    else:
      invalid_moves.append((row - 1, col))

    return valid_moves, invalid_moves, capture_moves
