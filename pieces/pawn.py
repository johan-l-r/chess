import pygame as pg
from base.piece import Piece

pg.init()

class Pawn(Piece): 
  def __init__(self, path, width, height, original_row): 
    super().__init__(path, width, height)
    
    self.original_row = original_row

  def get_possible_moves(self, board, row, col) -> list:
    super().get_possible_moves(board, row, col)

    moves = [
      (row - 1, col), 
      (row - 2, col) # two tiles movement
    ]

    # if initial position changed then remove two tile movement
    if self.original_row != row: 
      moves.remove((row - 2, col))

    valid_moves = []
    
    for row, col in moves: 
      if board.is_target_empty(row, col): 
        valid_moves.append((row, col))

    return valid_moves
