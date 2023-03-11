#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a window for the game
screen = pygame.display.set_mode((300, 300))

# Set the caption for the window
pygame.display.set_caption("Tic Tac Toe")

# Create a font for rendering the X and O symbols
font = pygame.font.SysFont(None, 100)

# Initialize the game board with empty spaces
board = [[" ", " ", " "] for _ in range(3)]

# Define the two players
players = ["X", "O"]

# Set the current player to be the first player in the list
current_player = players[0]

# Set the game over flag to False
game_over = False

# Define the colors for the winner and tie messages
winner_color = (255, 0, 0) # Red
tie_color = (0, 0, 255) # Blue
white = (255, 255, 255) 
# Function to draw the tic-tac-toe board
def draw_board():
    # Fill the screen with white
    screen.fill(white)
    
    # Draw the horizontal and vertical lines
    for i in range(1, 3):
        pygame.draw.line(screen, (0,0, 0), (0, i*100), (300, i*100), 3)
        pygame.draw.line(screen, (0, 0, 0), (i*100, 0), (i*100, 300), 3)
    
    # Draw the X and O symbols
    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                text = font.render(board[i][j], True, (0, 0, 0))
                screen.blit(text, (j*100 + 50 - text.get_width()//2, i*100 + 50 - text.get_height()//2))

# Function to check if a player has won
def check_win(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Main game loop
while True:
    # Clear the game board
    board = [[" ", " ", " "] for _ in range(3)]
    
    # Set the current player to be the first player in the list
    current_player = players[0]
    
    # Set the game over flag to False
    game_over = False
    
    # Draw the initial board
    draw_board()
    pygame.display.update()
    
    # Wait for the player to click on a cell
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Check for mouse click events
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                row, col = y//100, x//100
                
                 # Check if the cell is already occupied
                if board[row][col] == " ":
                    board[row][col] = current_player
                    draw_board()
                    pygame.display.update()
                    # Check if the current player has won
                    if check_win(current_player):
                        winner_text = font.render(f"{current_player} wins!", True, winner_color)
                        winner_rect = winner_text.get_rect(center=(150, 150))
                        screen.fill(white)
                        screen.blit(winner_text, winner_rect)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        game_over = True
                        break
                    # Switch to the other player's turn
                    elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                        tie_text = font.render("Tie!", True, tie_color)
                        tie_rect = tie_text.get_rect(center=(150, 150))
                        screen.fill(white)
                        screen.blit(tie_text, tie_rect)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        game_over = True
                        break
                    # Switch to the other player's turn
                    else:
                        current_player = players[(players.index(current_player)+1)%2]
        # Add a small delay to reduce CPU usage
        pygame.time.wait(10) 


# In[ ]:





# In[ ]:




