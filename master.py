import pygame
import sys
import time

# Constants
BOARD_SIZE = 3
WIDTH = 300
HEIGHT = 300

# Pygame Initialization
pygame.init()

# Setting the window size
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors that we will use in the game
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Cell coordinates
board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Fonts initialization
game_font = pygame.font.Font(None, 30)
winner_font = pygame.font.Font(None, 40)

def draw_board():
   for i in range(1, BOARD_SIZE):
       # Horizontal lines
       pygame.draw.line(display_surface, white, (0, i * WIDTH // BOARD_SIZE), (WIDTH, i * WIDTH // BOARD_SIZE), 2)

       # Vertical lines
       pygame.draw.line(display_surface, white, (i * WIDTH // BOARD_SIZE, 0), (i * WIDTH // BOARD_SIZE, HEIGHT), 2)

def draw_X(row, col):
   pygame.draw.line(display_surface, red, (col * WIDTH // BOARD_SIZE + 10, row * HEIGHT // BOARD_SIZE + 10), (col * WIDTH // BOARD_SIZE + 90, row * HEIGHT // BOARD_SIZE + 90), 2)
   pygame.draw.line(display_surface, red, (col * WIDTH // BOARD_SIZE + 90, row * HEIGHT // BOARD_SIZE + 10), (col * WIDTH // BOARD_SIZE + 10, row * HEIGHT // BOARD_SIZE + 90), 2)

def draw_O(row, col):
   pygame.draw.circle(display_surface, white, (col * WIDTH // BOARD_SIZE + WIDTH // (2*BOARD_SIZE), row * HEIGHT // BOARD_SIZE + HEIGHT // (2*BOARD_SIZE)), WIDTH // (2*BOARD_SIZE), 2)

def check_for_winner(board):
   winner = None

   # Going through rows and columns
   for i in range(BOARD_SIZE):
       if all(cell == "X" for cell in board[i]) or all(board[j][i] == "X" for j in range(BOARD_SIZE)):
           winner = "X"
       elif all(cell == "O" for cell in board[i]) or all(board[j][i] == "O" for j in range(BOARD_SIZE)):
           winner = "O"

   # Checking diagonals
   if all(board[i][i] == "X" for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - i - 1] == "X" for i in range(BOARD_SIZE)):
       winner = "X"
   elif all(board[i][i] == "O" for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - i - 1] == "O" for i in range(BOARD_SIZE)):
       winner = "O"

   return winner

# Drawing the winner's window
def draw_winner_window(winner):
   winner_text = winner_font.render("{} wins!".format(winner), True, black)
   winner_surface = pygame.Surface((150, 100))
   winner_surface.fill(white)
   winner_surface.blit(winner_text, (75 - winner_text.get_width()/2, 50 - winner_text.get_height()/2))
   pygame.draw.rect(winner_surface, black, (0, 0, 150, 100), 2)
   display_surface.blit(winner_surface, (75, 100))
   pygame.display.update(pygame.Rect(75, 100, 150, 100))
   time.sleep(3)

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
        winner = check_for_winner(board)
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