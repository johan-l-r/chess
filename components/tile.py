import pygame as pg

pg.init()

class Tile: 
  def __init__(self, width, height, x, y, coordinate):
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.coordinate  = coordinate
    self.color = (255, 255, 255)

    self.rect = pg.Rect(x, y, width, height)

  def draw(self, master):
    pg.draw.rect(master, self.color, self.rect)

  def set_color(self, color): 
    self.color = color

  def get_coordinate(self): return self.coordinate
