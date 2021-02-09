import pygame
import random

'''
-Active and Inactive are two 'sides' of a grid. There are rows and columns for each side
-Inactive grid stores the next iteration of a grid, active grid gets drawn directly onto
the screen
'''

DEAD_CELL_COLOR = 255, 0, 255
CELL_COLOR = 0,0,255
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900
INACTIVE_SWITCH_CONSTANT = 2

class Board:
  def __init__(self):
    self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.__grid = []
    self.__active = 0

# GETTING STUFF

# Gets the screen for other classes
  def get_screen(self):
    # Just returns screen to whatever class that wants a screen
    return self.__screen

# Gets the current active grid
  def get_active(self):
    return self.__active

# Gets the grid
  def get_grid(self):
    return self.__grid


  # Init Grid
  def grid(self, row, col):
    # creates and stores the default active and inactive grid
    def make_grid():
      rows = []
      for r in range(row):
        # Creates a list of 0's, and appends to a list rows, resulting in r
        # lists of lists with col number of 0's
        column_list = [0] * col
        rows.append(column_list)
      # Essentially rows is a matrix, that is going to be
      return rows
    # Appends a grid to the first one of either inactive or active grid
    self.__grid.append(make_grid())
    # Appends a grid to the second one of either inactive or active grid
    self.__grid.append(make_grid())

# Sets a grid full of 0's or 1's
  def set_grid(self, row, col, value = None, grid = 0):
    for r in range(row):
      for c in range(col):
        if value is None:
          cell_value = random.randint(0, 1)
        else:
          cell_value = value
        # whatever number grid is, a value is added to the row and column at that grid
        # where grid is either inactive grid or active grid
        self.__grid[grid][r][c] = cell_value

# Updates the board with the new grid
  def update_board_state(self, row, col, cell):
    self.set_grid(row, col, 0, self.inactive_grid())
    for r in range(row - 1):
      for c in range(col - 1):
        # checks neighbors to decide whether or not a cell is alive or not FOR THE NEXT GENERATION
        next_gen = cell.check_neighbors(r, c, self.__grid, self.__active)
        # Next generation cell state is added to inactive grid
        self.__grid[self.inactive_grid()][r][c] = next_gen
      # inactive grid is then switched to active grid
    self.__active = self.inactive_grid()

# Switches self.__active between 1 and 0 in order for screen to iterate
  def inactive_grid(self):
    return (self.__active + 1) % INACTIVE_SWITCH_CONSTANT

# Resets the active and inactive grid to initial conditions, then draws cells
  def reset(self, row, col, cell, board):
    self.__active = 0
    self.set_grid(row, col, None, self.__active)
    self.set_grid(row, col, 0, self.inactive_grid())
    cell.refresh_cells(row, col, self.__grid, self.__active, board)