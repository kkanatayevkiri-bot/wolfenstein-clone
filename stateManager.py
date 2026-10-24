from game import *
from menu import *
from gameOver import *
from winscreen import *

class StateManager:
    def __init__(self, engine):
        self.engine = engine
        self.states = {
            "menu": Menu(self, self.engine),
            "game": Game(self.engine),
            "gameover": GameOver(self, self.engine),
            "win": WinScreen(self, self.engine)
        }
        self.state = self.states["menu"]

    def next_state(self):
        if self.state.done:
            self.state.done = False
            if self.state.curr == 'gameover' or self.state.curr == 'win':
                self.states['game'].new_game()
            self.state = self.states[self.state.next]