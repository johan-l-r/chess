import pygame as pg
from base.piece import Piece

pg.init()

class Pawn(Piece): 
  def __init__(self, path, width, height): 
    super().__init__(path, width, height)
