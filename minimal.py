import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

#Colors
red = pygame.Color(255, 0, 0)
orange = pygame.Color(255, 128, 0)
yellow = pygame.Color(255, 255, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(255, 0, 255)

color_index = 0
colors = [red, orange, yellow, green, blue, purple]

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        while True:
            color_index +=1
            if color_index >= len(colors):
                color_index = 0
        screen.fill(colors[color_index])
        pygame.display.flip()

