import pygame as pg
from base.piece import Piece

pg.init()

class Tile: 
  def __init__(self, width, height, x, y, row, col):
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.row = row
    self.col = col

    self.color = ()

    self.child = None 

    self.rect = pg.Rect(x, y, width, height)

  def add_child(self, child: Piece): 
    self.child = child

  def remove_child(self): 
    self.child = None

  def is_empty(self):
    return self.child is None

  def is_clicked(self, mouse_pos): 
    if self.rect.collidepoint(mouse_pos): 
      return True

    return False

  def draw(self, master): 
    pg.draw.rect(master, self.color, self.rect)

    if self.child: 
      self.child.draw(master, self.x, self.y)

  def set_color(self, color): self.color = color

  def get_child(self) -> Piece: return self.child
  def get_row(self): return self.row
  def get_col(self): return self.col
  def get_rect(self): return self.rect
  
