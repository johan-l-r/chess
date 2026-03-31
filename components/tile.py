import pygame as pg

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

    self.rect = pg.Rect(x, y, width, height)

  def add(self): 
    pass

  def draw(self, master):
    pg.draw.rect(master, self.color, self.rect)

  def set_color(self, color): 
    self.color = color

  def get_row(self): return self.row
  def get_col(self): return self.col
