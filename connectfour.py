def check(board, player):
  won = ""
  for row in range(1, 7):
    for col in range(7):
      if board[row][col] == player:
        if row < 4:
          if board[row + 1][col] == player:
            if board[row + 2][col] == player:
              if board [row + 3][col] == player:
                won = player
                break
          if col < 4:
            if board[row + 1][col + 1] == player:
              if board[row + 2][col + 2] == player:
                if board[row + 3][col + 3] == player:
                  won = player
                  break
        if col < 4:
          if board[row][col + 1] == player:
            if board[row][col + 2] == player:
              if board[row][col + 3] == player:
                won = player
                break
          if row > 3:
            if board[row - 1][col + 1] == player:
              if board [row - 2][col + 2] == player:
                if board [row - 3][col + 3] == player:
                  won = player
                  break
    if player == won:
      break
  if player != won and board[1][0] != "O":
    if board[1][1] != "O":
      if board[1][2] != "O":
        if board[1][3] != "O":
          if board[1][4] != "O":
            if board[1][5] != "O":
              if board[1][6] != "O":
                won = "0"
  return won
 
def place(board, player):
  select = True
  colchoice = raw_input("Choose the column in which to place your piece: ")
  while select:
    if len(colchoice) != 1:
      colchoice = raw_input("Please enter a valid column: ")
    elif ord(colchoice) < ord("1") or ord(colchoice) > ord("7"):
      colchoice = raw_input("Please enter a valid column: ")
    else:
      if board[1][int(colchoice) - 1] != "O":
        colchoice = raw_input("That column is full. Choose another column in which to place your piece: ")
      else:
        select = False
  placed = False
  x = 6
  while not placed:
    if board[x][int(colchoice[0]) - 1] == "O":
      board[x][int(colchoice[0]) - 1] = player
      placed = True
    else:
      x -= 1
  return board
 
def play(board, turn):
  turn += 1
  if turn % 2 != 0:
    player = "1"
  else:
    player = "2"
  showboard(board)
  print "It is turn " + str(turn) + ", player " + player + " to play."
  board = place(board, player)
  return turn, player, board
 
def showboard(board):
  for row in board:
    print " ".join(row)
 
def startgame():
  won = ""
  turn = 0
  player = ""
  board = []
  board.append([str(num) for num in range (1,8)])
  for i in range(6):
    board.append(["O"] * 7)
  return won, turn, player, board
 
won = "no"
print "Welcome to Connect Four."
while 1 == 1:
  if won == "no":
    dummy = raw_input("Press any key to begin the game.")
    won, turn, player, board = startgame()
  elif won != "":
    if won == "0":
      print "The game ends in a draw."
    else:
      print "Player " + player + " has won the game."
    won = "no"
  else:
    turn, player, board = play(board, turn)
    won = check(board, player)
    if won != "":
      showboard(board)