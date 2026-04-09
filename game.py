import pygame as pg
from components.board import Board

pg.init()

class Game: 
  def __init__(self):
    self.WINDOW_WIDTH = 720
    self.WINDOW_HEIGHT = 720

    self.board = Board() 
    self.window = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

    self.running = False

  def run(self):
    self.running = True

    while self.running:
      for e in pg.event.get(): 
        if e.type == pg.QUIT: 
          self.running = False

        self.board.handle_event(e)

      self.board.update()
      self.board.draw(self.window)

      pg.display.flip()
