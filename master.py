import pygame
import sys
import time

# Pygame Initialization
pygame.init()

# Setting the window size
width = 300
height = 300
display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors that we will use in the game
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Cell coordinates
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# Fonts initialization
game_font = pygame.font.Font(None, 30)
winner_font = pygame.font.Font(None, 40)

# Drawing the game cells
def draw_board():
    for i in range(1, 3):
        # Horizontal lines
        pygame.draw.line(display_surface, white, (0, i * 100), (300, i * 100), 2)

        # Vertical lines
        pygame.draw.line(display_surface, white, (i * 100, 0), (i * 100, 300), 2)

# Drawing the cross
def draw_X(row, col):
    pygame.draw.line(display_surface, red, (col * 100 + 10, row * 100 + 10), (col * 100 + 90, row * 100 + 90), 2)
    pygame.draw.line(display_surface, red, (col * 100 + 90, row * 100 + 10), (col * 100 + 10, row * 100 + 90), 2)

# Drawing the nought
def draw_O(row, col):
    pygame.draw.circle(display_surface, white, (col * 100 + 50, row * 100 + 50), 40, 2)

# Checking if there's a winner
def check_for_winner():
    winner = None

    # Going through rows and columns
    for i in range(3):
        if all(board[i][j] == "X" for j in range(3)):
            winner = "X"

        elif all(board[i][j] == "O" for j in range(3)):
            winner = "O"

        elif all(board[j][i] == "X" for j in range(3)):
            winner = "X"

        elif all(board[j][i] == "O" for j in range(3)):
            winner = "O"

    # Checking diagonals
    if all(board[i][i] == "X" for i in range(3)):
        winner = "X"

    elif all(board[i][i] == "O" for i in range(3)):
        winner = "O"

    elif all(board[i][2-i] == "X" for i in range(3)):
        winner = "X"

    elif all(board[i][2-i] == "O" for i in range(3)):
        winner = "O"

    return winner

# Drawing the winner's window
def draw_winner_window(winner):
    winner_text = winner_font.render("{} wins!".format(winner), True, black)
    pygame.draw.rect(display_surface, black, (75, 100, 150, 100))
    pygame.draw.rect(display_surface, white, (80, 105, 140, 90))
    display_surface.blit(winner_text, (width/2 - winner_text.get_width()/2, height/2 - winner_text.get_height()/2))
    pygame.display.update()
    time.sleep(2)

# Main game loop
def gameLoop():
    global board

    # Determining who starts the game with a cross
    turn = "X"
    running = True

    # Drawing the game field
    draw_board()

    while running:
        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Determining the position of the mouse click
                x, y = pygame.mouse.get_pos()

                # Determining the row and column of the selected cell
                row = y // 100
                col = x // 100

                # Checking that the cell is free
                if board[row][col] == "":
                    board[row][col] = turn

                    # Drawing the cross or nought
                    if turn == "X":
                        draw_X(row, col)
                        turn = "O"
                    elif turn == "O":
                        draw_O(row, col)
                        turn = "X"

        # Checking if there's a winner
        winner = check_for_winner()
        if winner is not None:
            draw_winner_window(winner)
            running = False

        # Updating the screen
        pygame.display.update()

    # Closing the window
    pygame.quit()
    sys.exit()

# Starting the game
gameLoop()