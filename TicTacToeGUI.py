import sys
import pygame
from MinMaxAlgorithm import MinMaxAlgorithm, get_result


pygame.init()

BOARD_SIZE = 480
size = width, height = BOARD_SIZE, BOARD_SIZE
color = (17, 1, 51)
BLACK = (0, 145, 142)
WHITE = (255, 220, 52)
LINE_COLOR = (77, 213, 153)
screen = pygame.display.set_mode(size)

GRID_WIDTH = int(BOARD_SIZE / 3)

board_condition = [
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
            piece_con = board_condition[y][x]
            if piece_con != 0 :
                if piece_con == 1:
                    piece_color = WHITE
                elif piece_con == -1:
                    piece_color = BLACK
                pygame.draw.circle(screen, piece_color,
                    (int((x + 0.5) * GRID_WIDTH), int((y + 0.5) * GRID_WIDTH)), int(GRID_WIDTH / 2) - 10)


is_white = True
difficult = 7

if is_white:
    mma = MinMaxAlgorithm(-1, difficult)
else:
    mma = MinMaxAlgorithm(1, difficult)

if not is_white:
    # val, action = mma(board_condition)
    # board_condition[action[0]][action[1]] = 1
    board_condition[1][1] = 1
    draw_piece()

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

            if board_condition[i][j] == 0:
                if is_white:
                    board_condition[i][j] = 1
                    val, action = mma(board_condition)
                    if action:
                        mi, mj = action
                        board_condition[mi][mj] = -1
                else:
                    board_condition[i][j] = -1
                    val, action = mma(board_condition)
                    if action:
                        mi, mj = action
                        board_condition[mi][mj] = 1
                # is_white = not is_white

            draw_piece()

            result = get_result(board_condition)

            if result == 1:
                pass
            elif result == -1:
                pass
            elif result == 0:
                pass

        pygame.display.flip()

pygame.quit()

