from base.piece import Piece

class Bishop(Piece): 
  def __init__(self, path, width, height):
    super().__init__(path, width, height)

  def get_moves(self, board, row, col) -> tuple:
    super().get_moves(board, row, col)

    valid_moves = []
    invalid_moves = []
    capture_moves = []

    # top right
    for i in range(1, 8): 
      r = row - i
      c = col + i

      if not board.is_valid_position(r, c): 
        break

      if board.is_target_empty(r, c): 
        valid_moves.append((r, c))
      else:
        capture_moves.append((r, c))
        break

    # bottom left 
    for i in range(1, 8): 
      r = row + i
      c = col - i

      if not board.is_valid_position(r, c): 
        break

      if board.is_target_empty(r, c): 
        valid_moves.append((r, c))
      else:
        capture_moves.append((r, c))
        break

    # top left
    for i in range(1, 8): 
      r = row - i
      c = col - i

      if not board.is_valid_position(r, c): 
        break

      if board.is_target_empty(r, c): 
        valid_moves.append((r, c))
      else:
        capture_moves.append((r, c))
        break

    # bottom right
    for i in range(1, 8): 
      r = row + i 
      c = col + i

      if not board.is_valid_position(r, c): 
        break

      if board.is_target_empty(r, c): 
        valid_moves.append((r, c))
      else:
        capture_moves.append((r, c))
        break

    return valid_moves, invalid_moves, capture_moves
