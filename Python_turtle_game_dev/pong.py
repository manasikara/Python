# just a Pong game. Source --> https://www.youtube.com/watch?v=HNCAi0sjAz8

import pygame

# variables and constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = (600)
HEIGHT = (600)

pygame.init()
game_font = pygame.font.SysFont('Ubuntu', 40)

delay = 30
paddle_speed = 20
paddle_width = 10
paddle_height = 100

p1_x_position = 10
p1_y_position = HEIGHT / 2 - paddle_height / 2

p2_x_position = WIDTH - paddle_width - 10
p2_y_position = HEIGHT / 2 - paddle_height / 2

pl1_score = 0
pl2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False
