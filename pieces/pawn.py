import pygame as pg
from base.piece import Piece

pg.init()

class Pawn(Piece): 
  def __init__(self, path, width, height): 
    super().__init__(path, width, height)
    
    self.is_first_move = True

  def move(self, current_row, current_col, target_row, target_col) -> bool:
    super().move(current_row, current_col, target_row, target_col)

    # only move vertically
    if target_col != current_col: 
      return False
    
    if target_row == current_row - 1: 
      self.is_first_move = False
      return True

    if target_row == current_row - 2 and self.is_first_move: 
      self.is_first_move = False
      return True

    return False
