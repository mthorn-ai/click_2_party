import pygame
import random
import time
import math
from pygame.locals import *

screen = pygame.display.set_mode((750, 750))
surface = pygame.display.get_surface()
Pi = math.pi
pygame.display.set_caption("party time")


def set_background_color(x, y, z):
    screen.fill((x, y, z))
    pygame.display.flip()


def normal_face():
    set_background_color(200, 212, 252)
    pygame.draw.circle(surface, (255, 255, 255), (250, 300), 50)
    pygame.draw.circle(surface, (0, 0, 0), (250, 300), 25)
    pygame.draw.circle(surface, (255, 255, 255), (500, 300), 50)
    pygame.draw.circle(surface, (0, 0, 0), (500, 300), 25)
    pygame.draw.circle(surface, (0, 0, 0), (375, 375), 300, 3)
    pygame.draw.arc(screen, (0, 100, 115), [175, 350, 400, 200], (7 * Pi) / 6, (11 * Pi) / 6, 10)
    pygame.display.flip()


normal_face()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONUP:
                print("click registered")
                for i in range(25):
                    set_background_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    if i % 2 == 0:
                        pygame.draw.circle(surface, (0, 0, 0), (350, 375), 300, 3)
                        pygame.draw.circle(surface, (255, 255, 255), (225, 300), 100)
                        pygame.draw.circle(surface, (255, 255, 255), (475, 300), 100)
                        pygame.draw.arc(screen, (255, 255, 255), [150, 300, 400, 300], Pi, 0, 500)
                    else:
                        pygame.draw.circle(surface, (0, 0, 0), (400, 375), 300, 3)
                        pygame.draw.circle(surface, (0, 0, 0), (275, 300), 100)
                        pygame.draw.circle(surface, (0, 0, 0), (525, 300), 100)
                        pygame.draw.arc(screen, (0, 0, 0), [200, 300, 400, 300], Pi, 0, 500)
                    pygame.display.flip()
                    time.sleep(0.09)
                normal_face()


if __name__ == "__main__":
    main()
