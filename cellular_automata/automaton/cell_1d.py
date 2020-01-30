"""
Self class for a 1D cellular automaton.
"""


class Cell:
    def __init__(self, state, pos):
        self.state = state
        self.pos = pos

    def neighbor_states(self, cells):
        left = cells[self.pos-1].state
        right = cells[self.pos+1].state
        return f'{left}{self.state}{right}'
