board = [[" " for _ in range(3)] for _ in range(3)]

def draw_board():
  print("  0 1 2")
  for i, row in enumerate(board):
    print(i, *row)

def get_move(player):
  while True:
    try:
      row = int(input(f"{player}, enter row: "))
      col = int(input(f"{player}, enter col: "))
      if row in range(3) and col in range(3):
        if board[row][col] == " ":
          return row, col
        else:
          print("That space is already occupied. Please try again.")
      else:
        print("Invalid move. Please try again.")
    except ValueError:
      print("Invalid input. Please try again.")

def game_over():
  # Check rows
  for row in board:
    if row == ["X", "X", "X"]:
      return "X"
    elif row == ["O", "O", "O"]:
      return "O"
  # Check columns
  for col in range(3):
    if board[0][col] == "X" and board[1][col] == "X" and board[2][col] == "X":
      return "X"
    elif board[0][col] == "O" and board[1][col] == "O" and board[2][col] == "O":
      return "O"
  # Check diagonals
  if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
    return "X"
  elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
    return "O"
  if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
    return "X"
  elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
    return "O"
  # Check for draw
  for row in board:
    if " " in row:
      return False
  return "Draw"

def play_game():
  draw_board()
  while not game_over():
    row, col = get_move("X")
    board[row][col] = "X"
    draw_board()
    if game_over():
      break
    row, col = get_move("O")
    board[row][col] = "O"
    draw_board()
  result = game_over()
  if result == "X":
    print("X wins!")
  elif result == "O":
    print("O wins!")
  else:
    print("It's a draw!")

play_game()
