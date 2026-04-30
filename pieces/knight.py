from base.piece import Piece

class Knight(Piece): 
  def __init__(self, path, width, height):
    super().__init__(path, width, height)

  def get_moves(self, board, row, col) -> tuple:
    super().get_moves(board, row, col)

    moves = [
      (row - 2, col - 1), 
      (row - 2, col + 1), 
      (row + 2, col - 1), 
      (row + 2, col + 1), 

      (row - 1, col + 2), 
      (row + 1, col + 2), 
      (row - 1, col - 2), 
      (row + 1, col - 2), 
    ]
    
    valid_moves = []
    invalid_moves = []
    capture_moves = []

    for row, col in moves: 
      # prevent out of range movement
      if board.is_valid_position(row, col): 
        if board.is_target_empty(row, col):
          valid_moves.append((row, col))
        else:
          capture_moves.append((row, col))

    return valid_moves, invalid_moves, capture_moves
