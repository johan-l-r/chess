import pygame as pg

pg.init()

class Game: 
  def __init__(self):
    self.WINDOW_WIDTH = 1280
    self.WINDOW_HEIGHT = 720

    self.window = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

    self.running = False

  def run(self):
    self.running = True

    while self.running:
      for e in pg.event.get(): 
        if e.type == pg.QUIT: 
          self.running = False
