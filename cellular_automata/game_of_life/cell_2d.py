"""
Self class for a 2D cellular automaton.
"""


class Cell:
    def __init__(self, state, y, x):
        self.state = None
        self.prev_state = state
        self.y = y
        self.x = x

    def neighbor_states(self, cells):
        neighbors = 0
        for col in [self.y-1, self.y, self.y+1]:
            for row in [self.x-1, self.x, self.x+1]:
                if col == self.y and row == self.x or col < 0 or row < 0:
                    continue
                else:
                    try:
                        neighbors += cells[col][row].prev_state
                    except IndexError:  # edges
                        continue

        return neighbors

    def update_state(self):
        if self.state is not None:
            self.prev_state = self.state
            self.state = None
