import pygame
import sys
import random

DEAD_CELL_COLOR = 255, 0, 255
CELL_COLOR = 0,0,255
CELL_SIDE = 10
OVERPOP_DISCRIMINANT = 3
UNDERPOP_DISCRIMINANT = 2
STABLE_POP = 3

class Cell:
  def __init__(self):
    self.__cell_value = 0

# Sees whether an INDIVIDUAL cell, the one at grid, row, col, is alive or not
# if the cell that is in that grid, that row, and that col is a 1, then it is alive, etc
  def get_cell(self, row, col, grid, active):
    try:
      cell_value = grid[active][row][col]
    except:
      cell_value = 0
    return cell_value

  
  # Draws the new board if cell is 1, then make cell have alive color, if dead, make it have dead color
  def refresh_cells(self, row, col, grid, active, board):

    self.clear_screen(board)
    for c in range(col):
      for r in range(row):
        if grid[active][r][c] == 1:
          color = CELL_COLOR
        else:
          color = DEAD_CELL_COLOR
        pygame.draw.circle(board.get_screen(), color, \
                          (int(c * CELL_SIDE + CELL_SIDE / 2), int(r * CELL_SIDE + CELL_SIDE / 2)), int(CELL_SIDE / 2), 0)
    pygame.display.flip()

  # Check Cell Neighbors
  def check_neighbors(self, row, col, grid, active):
    # List of 9 surrounding cells
    surrounding = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                   (row    , col - 1),                 (row    , col + 1),
                   (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    num_alive_neighbors = 0

  # counts number of alive neighbors for evaluating whether this cell should die or live
    for i in surrounding:
      num_alive_neighbors += self.get_cell(i[0], i[1], grid, active)

    # Application of Game of Life criteria
    if grid[active][row][col] == 1: # alive
      if num_alive_neighbors > OVERPOP_DISCRIMINANT or \
         num_alive_neighbors < UNDERPOP_DISCRIMINANT:
        return 0
      else:
        return 1
    elif grid[active][row][col] == 0 and num_alive_neighbors == STABLE_POP:
      return 1
    #print(num_alive_neighbors)
    # Returns a grid of next generation cells(unupdated)
    return grid[active][row][col]

  def clear_screen(self, board):
    # Clears screen duh
    # Does so by setting all the color of cells on screen to dead cells
    screen = board.get_screen()
    screen_2 = pygame.Surface.copy(screen)
    screen_2.fill(CELL_COLOR)
    pygame.display.flip()
