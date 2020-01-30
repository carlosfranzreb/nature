from cell_2d import Cell
import pygame
import sys
import random


SCREEN = pygame.Rect(0, 0, 640, 480)


def random_grid(width, height):
    return [[Cell(random.randint(0, 1), y, x) for x in
            range(int(SCREEN[2]/width))] for y in range(int(SCREEN[3]/height))]


def gliders_grid(width, height):
    grid = []
    for y in range(int(SCREEN[3]/height)):
        grid.append([])
        for x in range(int(SCREEN[2]/width)):
            grid[-1].append(Cell(0, y, x))

    for y in range(0, len(grid), 6):
        try:
            grid[y+1][2] = Cell(1, y+1, 2)
            grid[y+2][3] = Cell(1, y+2, 3)
            for i in range(3):
                grid[y+3][i+1] = Cell(1, y+3, i+1)

        except IndexError:
            break

    return grid


def main(grid, width=10, height=10):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN[2:4])

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                neighbors = grid[y][x].neighbor_states(grid)

                if grid[y][x].prev_state == 1:
                    square = pygame.Rect(grid[y][x].x*width,
                                         grid[y][x].y*height, width, height)
                    pygame.draw.rect(screen, (0, 0, 0), square)

                    if neighbors not in [2, 3]:
                        grid[y][x].state = 0

                elif grid[y][x].prev_state == 0 and neighbors == 3:
                    grid[y][x].state = 1

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                grid[y][x].update_state()

        pygame.display.flip()
        pygame.time.Clock().tick(50)  # cap the framerate


def print_grid(grid):
    for row in grid:
        string = ""
        for cell in row:
            string += str(cell.prev_state) + "\t"
        print(string)


if __name__ == '__main__':
    width, height = (5, 5)
    grid = gliders_grid(width, height)
    main(grid, width, height)
