import pygame as pg

pg.init()

class Pawn:
  def __init__(self, path, width, height):
    self.image = pg.image.load(path)
    self.image = pg.transform.scale(self.image, (width, height))

  def draw(self, master: pg.Surface, x, y): 
    master.blit(self.image, (x, y))
