import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main Game Loop
    while True:
        log_state()
        
        for event in pygame.event.get():
            pass

        screen.fill('black')

        # Refresh Screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
