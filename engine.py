import pygame
import sys
from settings import *
from stateManager import *

class Engine:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(WINDOW)
        self.clock = pygame.time.Clock()
        self.del_time = 1
        self.running = True

        self.statemanager = StateManager(self)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #event of it self of the 'X' button window
                self.running = False
            self.statemanager.state.input(event)

    def update(self):
        self.handle_events()
        self.statemanager.state.update()
        self.statemanager.next_state()
        self.del_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}') #regular f string with attribute and method

    def draw(self):
        self.statemanager.state.draw() #because the fill already in that function!
        pygame.display.flip()
        

    def run(self):
        while self.running:
            self.update()
            self.draw()

if __name__ == "__main__":
    engine = Engine()
    engine.run()
pygame.quit()
sys.exit()