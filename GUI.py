'''
Caleb Qi
cqi2@binghamton.edu
Section A52
CA: Elizabeth Voroshylo
FINAL PROJECT
'''

'''
Game Of Life: Rules are as follows.

1. Any live cell with fewer than two live neighbours dies, as if by
underpopulation.
2. Any live cell with two or three live neighbours lives on to the next
generation.
3. Any live cell with more than three live neighbours dies, as if by
overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if
by reproduction.

Program should be able to
1. Allow user to pause, resume, speed up, slowdown, reset, and play wagner
2. Cells should die and be born according to rules, for infinite generations
3. Play Klarinettenkonzert A-Dur, K. 622:2.Adagio by Wolfgang Amadeus Mozart in background

TRICKS:
1. Board state (grid) will be encoded with a list. A list with lists in it
the first index of the list will indicate row, and the second index will indicate
individual cells in that row, so basically columns. 1 will indicate alive, 0 indicates ded
2. Will detect surrounding cells through
surrounding = ((row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
               (row    , col - 1),                 (row    , col + 1),
               (row + 1, col - 1), (row + 1, col), (row + 1, col + 1))

METHODS:

# Animation Controls HANDLERS INSIDE GUI

def pause() 
use while loop to pause and resume

def resume()
use while loop to pause and resume

def speed_up()
speeds up....

def slows_down()
slows down....

# Makes board into desired state and sends to board function

def kill()kills all cells that need to be dead at once
returns board state

def spawn()spawns all cells that need to be born at once
returns board state

def reset() clear board. ez.

PARTS:
1. Board(color, board state(list))
carries out generations of cells
2. Cell(board state)
figures out next generation(with algorithms) calls kill and spawn,
sends board back to board()
3. GUI()
Creates gui on the screen.

ATP:
1. Animation executes according to rules of game of life, indefinitely
2. When buttons are clicked, they work.
3. Song plays when GUI is run the first time
4. When reset is pressed, goes back to 1 and loops
'''

# IMPORTS
from Board import Board
from Cell import Cell
import pygame
import sys

# CONSTANTS
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
INIT_FPS = 10

TEXT1_POSITION = 100, 800
TEXT2_POSITION = 400, 800
TEXT3_POSITION = 700, 800
TEXT4_POSITION = 1000, 800
TEXT5_POSITION = 1250, 800

BUTTONY = 800
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 100
BUTTON1_CORNER = 0
BUTTON2_CORNER = 300
BUTTON3_CORNER = 600
BUTTON4_CORNER = 900
BUTTON5_CORNER = 1200

# GAME OF LIFE CONSTANTS
CELL_SIDE = 10
DEAD_CELL_COLOR = 255, 0, 255
CELL_COLOR = 0, 0, 255
SPEED_INCREMENT = 5

# COLORS AND FONT
AQUA = 0, 128, 128
CYAN = 0, 255, 255
GREEN = 127, 255, 0
BLUE = 61, 89, 171
GOLD = 255, 193, 37
WHITE = 255,255,255
FONT_SIZE = 30

# SOUND COMPONENT
MIXER_INIT = [22050, 16, 2, 4096]
VOLUME = 0.75
LOOP_SONG = -1

class GUI:
  def __init__(self):
    pygame.mixer.pre_init(MIXER_INIT[0], MIXER_INIT[1], MIXER_INIT[2], MIXER_INIT[3])
    pygame.init()
    pygame.font.init()

    # Initializes Other Classes
    self.__row = int(SCREEN_HEIGHT / CELL_SIDE)
    self.__col = int(SCREEN_WIDTH / CELL_SIDE)

    # Instantiating object variables
    self.__max_fps = INIT_FPS
    self.__pause = False
    self.__board = Board()
    self.__cell = Cell()
    self.__board.grid(self.__row, self.__col)
    self.__board.set_grid(self.__row, self.__col)
    self.__screen = self.__board.get_screen()

    # Creates GUI
    self.__reset_button = pygame.draw.rect\
                          (self.__screen, AQUA,(BUTTON1_CORNER, BUTTONY, BUTTON_WIDTH, BUTTON_HEIGHT))
    self.__accelerate_button = pygame.draw.rect(self.__screen, CYAN, (BUTTON2_CORNER, BUTTONY, BUTTON_WIDTH, BUTTON_HEIGHT))
    self.__deccelerate_button = pygame.draw.rect(self.__screen, GREEN, (BUTTON3_CORNER, BUTTONY, BUTTON_WIDTH, BUTTON_HEIGHT))
    self.__pause_resume_button = pygame.draw.rect(self.__screen, BLUE, (BUTTON4_CORNER, BUTTONY, BUTTON_WIDTH, BUTTON_HEIGHT))
    self.__let_there_be_wagner = pygame.draw.rect(self.__screen, GOLD, (BUTTON5_CORNER, BUTTONY, BUTTON_WIDTH, BUTTON_HEIGHT))

    # BUTTON TEXTS
    font = pygame.font.SysFont('Ariel', FONT_SIZE)
    text1 = font.render('RESET', True, WHITE)
    self.__screen.blit(text1, TEXT1_POSITION)
    text2 = font.render('ACCELERATE', True, WHITE)
    self.__screen.blit(text2, TEXT2_POSITION)
    text3 = font.render('DECELERATE', True, WHITE)
    self.__screen.blit(text3, TEXT3_POSITION)
    text4 = font.render('PAUSE/RESUME', True, WHITE)
    self.__screen.blit(text4, TEXT4_POSITION)
    text5 = font.render('LET THERE BE WAGNER', True, WHITE)
    self.__screen.blit(text5, TEXT5_POSITION)

    # Initializing Mixer and Music Component
    pygame.display.flip()
    pygame.mixer.music.load('Klarinettenkonzert A-Dur_K._6222._II._Adagio_by_Wolfgang_Amadeus_Mozart.mp3')
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.play(LOOP_SONG)


# EVENT HANDLER FUNCTION

  def handle_events(self):

    # Acesses the list of default pygame events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.display.quit()
        sys.exit()

      # If mouse pressed, checks which button is pressed by seeing if mouse
      # position collides with the button

      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        # gets mouse position
        # checks if mouse position is over the button, then calls handlers
        if self.__reset_button.collidepoint(mouse_pos):
          # prints current location of mouse
          print('reset button was pressed at {0}'.format(mouse_pos))
          self.reset()
          
        if self.__accelerate_button.collidepoint(mouse_pos):
          # prints current location of mouse
          print('accelerate button was pressed at {0}'.format(mouse_pos))
          self.speed_up(SPEED_INCREMENT)
          
        if self.__deccelerate_button.collidepoint(mouse_pos):
          # prints current location of mouse
          print('deccelerate button was pressed at {0}'.format(mouse_pos))
          self.slow_down(SPEED_INCREMENT)
          
        if self.__pause_resume_button.collidepoint(mouse_pos):
          # prints current location of mouse
          print('pause or resume button was pressed at {0}'.format(mouse_pos))
          self.pause()

        if self.__let_there_be_wagner.collidepoint(mouse_pos):
          print('THHERE WILL NOW BE WAGNER {0}'.format(mouse_pos))
          self.wagner()


# EVENT HANDLERS

  def pause(self):
      if self.__pause == True:
          self.__pause = False
      else:
          self.__pause = True

# Effects of acceleration is subtle
  def speed_up(self, fps):
      self.__max_fps += fps

# Effects of deceleration is subtle
  def slow_down(self, fps):
      self.__max_fps -= fps

# Calls the reset function in board. Done this way because calling these variables
# from board would be much more cumbersome
  def reset(self):
      row = self.__row
      col = self.__col
      board = self.__board
      cell = self.__cell
      board.reset(row, col, cell, board)

# Name says it all
  def wagner(self):
      pygame.mixer.music.load('Tannhauser Overture_Richard_Wagner-(Valery_Gergiev-Wiener Philharmoniker).mp3')
      pygame.mixer.music.play(-1)

# MAIN LOOP REFERENCED FROM 
  def run(self):

      # Initializing all necessary variables
      board = self.__board
      cell = self.__cell
      clock = pygame.time.Clock()
      while True:
          # Pause condition
          if not self.__pause:
              # Edit the board state
              board.update_board_state(self.__row, self.__col, cell)
              # Implement board state
              cell.refresh_cells(self.__row, self.__col, board.get_grid(), board.get_active(), board)
          self.handle_events()
          clock.tick(self.__max_fps)

GUI().run()
