import pygame
import sys
import random
import math
from cell_1d import Cell


SCREEN = pygame.Rect(0, 0, 1400, 800)


def random_ca(start="random"):
    rows = int(SCREEN[3]/10)
    cols = int(SCREEN[2]/10)

    if start == "random":
        automaton = [Cell(random.randint(0, 1), i) for i in range(cols)]
        grid = [[0 for _ in range(cols)] for _ in range(rows)]

    elif start == "middle":
        automaton = [Cell(0, i) for i in range(cols)]
        middle = math.floor(len(automaton)/2)
        automaton[middle] = Cell(1, middle)
        grid = [[0 for _ in range(cols)] for _ in range(rows)]
        grid[0][middle] = pygame.Rect(middle*10, 0, 10, 10)

    rule_set = [random.randint(0, 1) for _ in range(8)]

    return (automaton, rule_set, grid)


def wolfram_ca(width=10, height=10):
    rows = int(SCREEN[3]/height)
    cols = int(SCREEN[2]/width)

    automaton = [Cell(0, i) for i in range(cols)]
    middle = math.floor(len(automaton)/2)
    automaton[middle] = Cell(1, middle)

    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    grid[0][middle] = pygame.Rect(middle*width, 0, width, height)

    rule_set = [0, 1, 0, 1, 1, 0, 1, 0]

    return (automaton, rule_set, grid)


def fill_grid(automaton, rule_set, grid, width=10, height=10):
    for lvl in range(1, len(grid)):  # first level = initial state
        new_states = [0]  # left edge
        for i in range(1, len(automaton)-1):  # ignore edges
            states = automaton[i].neighbor_states(automaton)
            idx = bin_to_dec(states)
            new_states.append(rule_set[idx])

        new_states.append(0)  # right edge
        for i in range(len(new_states)):
            automaton[i].state = new_states[i]
            if new_states[i] == 1:  # save white rectangle in grid
                grid[lvl][i] = pygame.Rect(i*width, lvl*height, width, height)

    return grid


def main(grid):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN[2:4])

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        for row in grid:
            for cell in row:
                if cell != 0:
                    pygame.draw.rect(screen, (0, 0, 0), cell)

        pygame.display.flip()
        pygame.time.Clock().tick(1)  # cap the framerate


def bin_to_dec(string):
    num = 0
    length = len(string)
    for i in range(length):
        num += int(string[i]) * 2**(length - i - 1)
    return num


if __name__ == '__main__':
    automaton, rule_set, grid = wolfram_ca(10, 10)
    grid = fill_grid(automaton, rule_set, grid, 10, 10)
    main(grid)
