import sys
import pygame


pygame.init()

BOARD_SIZE = 480
size = width, height = BOARD_SIZE, BOARD_SIZE
color = (17, 1, 51)
BLACK = (0, 145, 142)
WHITE = (255, 220, 52)
LINE_COLOR = (77, 213, 153)
screen = pygame.display.set_mode(size)

GRID_WIDTH = int(BOARD_SIZE / 3)

borad_condition = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

screen.fill(color)

for i in range(1, 3):
    pygame.draw.line(screen, LINE_COLOR, (GRID_WIDTH * i, 0), (GRID_WIDTH * i, BOARD_SIZE), 1)
    pygame.draw.line(screen, LINE_COLOR, (0, GRID_WIDTH * i), (BOARD_SIZE, GRID_WIDTH * i), 1)

def draw_piece():

    for y in range(3):
        for x in range(3):
            piece_con = borad_condition[y][x]
            if piece_con != 0 :
                if piece_con == 1:
                    piece_color = WHITE
                elif piece_con == -1:
                    piece_color = BLACK
                pygame.draw.circle(screen, piece_color,
                    (int((x + 0.5) * GRID_WIDTH), int((y + 0.5) * GRID_WIDTH)), int(GRID_WIDTH / 2) - 10)


is_white = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid = (int(event.pos[0] / (GRID_WIDTH + .0)),
                int(event.pos[1] / (GRID_WIDTH + .0)))
            print(grid)
            
            y, x = grid
            i, j = x, y

            if borad_condition[i][j] == 0:
                if is_white:
                    borad_condition[i][j] = 1
                else:
                    borad_condition[i][j] = -1
                is_white = not is_white

            draw_piece()

        pygame.display.flip()

pygame.quit()

