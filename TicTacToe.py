# ------------------- Global Variables -------------------
# Set up the board:
board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]

# Initialize the game status to running:
game_still_going = True

# Initialize who won:
winner = None

# Initialize whose turn is it:
current_player = "X"

# Function for creating a board:
def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])

# Function for starting the game:
def play_game():

	# Display the initial board:
	display_board()

	while game_still_going:

		# Handle a single turn:
		handle_turn(current_player)

		# Check if the game has ended:
		check_if_game_over()

		# Flip to the next player:
		flip_player()

	# The game has ended(this is outside the main game loop):
	if winner == "X" or winner == "O":
		print(winner + " won.")
	elif winner == None:
		print("Tie.")

# Handle a single turn of a player:
def handle_turn(player):

	print(player + "'s turn.")
	# Get the position from the player:
	position = input("Choose a position from 1-9: ")

	# Initiate valid input flag to false:
	valid = False
	while not valid:

		# Prompt the user for a number again if not in range:
		while position not in ["1", "2", "3", "4", "5", "6", "7", 
			"8", "9"]:
			position = input("Invalid input." + 
				" Choose a position from 1-9: ")

		# Subtract 1 from position and cast to an int to match index:
		position = int(position) - 1

		# Change valid input flag to true:
		if board[position] == "-":
			valid = True
		else:
			print("You can't go there. Go again.")

	# Change the placeholder of the desired position to an "X":
	board[position] = player

	# Display the updated board:
	display_board()


def check_if_game_over():
	check_for_winner()
	check_for_tie()
	return

def check_for_winner():
	# Set up global variables:
	global winner

	# Check rows:
	row_winner = check_rows()
	# Check columns:
	column_winner = check_columns()
	# Check diagonals:
	diagonal_winner = check_diagonals()
	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		# Nobody won
		winner = None
	return

def check_rows():
	# Set up global variables:
	global game_still_going

	# Check if any of the rows are a win:
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"

	# Check if any rows have a win, flag that there is a win:
	if row_1 or row_2 or row_3:
		game_still_going = False
	# Return the winner (X or O)
	if row_1:
		return board[0]
	if row_2:
		return board[3]
	if row_3:
		return board[3]
	return

def check_columns():
	# Set up global variables:
	global game_still_going

	# Check if any of the rows are a win:
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"

	# Check if any rows have a win, flag that there is a win:
	if column_1 or column_2 or column_3:
		game_still_going = False
	# Return the winner (X or O)
	if column_1:
		return board[0]
	if column_2:
		return board[1]
	if column_3:
		return board[2]
	return

def check_diagonals():
	# Set up global variables:
	global game_still_going

	# Check if any of the rows are a win:
	diagonal_1 = board[0] == board[4] == board[8] != "-"
	diagonal_2 = board[2] == board[4] == board[6] != "-"

	# Check if any rows have a win, flag that there is a win:
	if diagonal_1 or diagonal_2:
		game_still_going = False
	# Return the winner (X or O)
	if diagonal_1:
		return board[0]
	if diagonal_2:
		return board[2]
	return


def check_for_tie():
	# Set up global variables:
	global game_still_going
	if "-" not in board:
		game_still_going = False
	return

def flip_player():
	# Set up global variables:
	global current_player

	# Switch the player:
	if current_player == "X":
		current_player = "O"
	elif current_player == "O":
		current_player = "X"
	return

play_game()
