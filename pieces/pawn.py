import pygame as pg
from base.piece import Piece

pg.init()

class Pawn(Piece): 
  def __init__(self, path, width, height): 
    super().__init__(path, width, height)
    
    self.is_first_move = True

  def get_possible_moves(self, board, row, col):
    super().get_possible_moves(board, row, col)

    moves = []
    
    if board.is_target_empty(row - 1, col):
      moves.append((row - 1, col))

      if board.is_target_empty(row - 2, col) and self.is_first_move:
        moves.append((row - 2, col))
        self.is_first_move = False

    return moves 
