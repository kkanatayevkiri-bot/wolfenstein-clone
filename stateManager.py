from game import *
from menu import *

class StateManager:
    def __init__(self, engine):
        self.engine = engine
        self.states = {
            "menu": Menu(self.engine),
            "game": Game(self.engine)
        }
        self.state = self.states["menu"]

    def next_state(self):
        if self.state.done:
            self.state.done = False
            self.state = self.states[self.state.next]