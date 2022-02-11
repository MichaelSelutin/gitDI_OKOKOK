board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]

current_player = "X"
winner = None
game_running = True

def print_board(board):
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])

#board:
def player_input(board):
	inp = int(input("Enter a number between 1 and 9: "))
	if inp >= 1 and inp <= 9 and board[inp-1] == "-":
		board[inp-1] = current_player
	else:
		print("something wrong, try again")

#player input:

#check for win or tie
def check_horizontal(board):
	global winner
	if board[0] == board[1] == board[2] and board[1] != "-":
		winner = board[0]
		return True
	elif board[3] == board[4] == board[5] and board[4] != "-":
		winner = board[3]
		return True
	elif board[6] == board[7] == board[8] and board[6] != "-":
		winner = board[7]
		return True

def check_row(board):
	global winner
	if board[0] == board[3] == board[6] and board[0] != "-":
		winner = board[0]
		return True
	elif board[1] == board[4] == board[7] and board[1] != "-":
		winner = board[1]
		return True
	elif board[2] == board[5] == board[8] and board[2] != "-":
		winner = board[2]
		return True

def check_diagonal(board):
	global winner
	if board[0] == board[4] == board[8] and board[0] != "-":
		winner = board[0]
		return True
	elif board[2] == board[4] == board[6] and board[2] != "-":
		winner = board[4]
		return True

def check_tie(board):
	if "-" not in board:
		print_board(board)
		print("its a tie!")
		game_running = False

def check_win():
	if check_diagonal(board) or check_row(board) or check_horizontal(board):
		print(f"The winner is {winner}")

#switch player
def switch_player():
	global current_player
	if current_player == "X":
		current_player = "O"
	else:
		current_player = "X"

while game_running:
			print_board(board)
			player_input(board)
			check_win()
			check_tie(board)
			switch_player()
