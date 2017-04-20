
# Include pygame
# Include pygame, which we got from pip
import pygame

# bring in the math module so we can use absolute value
from math import fabs

from random import randint

# Init pygame
# In order to use pygame, we have to run the init method
pygame.init()

# Create a screen with a size
screen = {
    "height": 500,
    "width": 800,
}

keys = {
    "right": 275,
    "left": 276,
    "up": 273,
    "down": 274,
    "w": 119,
    "a": 97,
    "s": 115,
    "d": 100
}

keys_down = {
    "right": False,
    "left": False,
    "up": False,
    "down": False,
    "w": False,
    "a": False,
    "s": False,
    "d": False
}

hero = {
    "x": 100,
    "y": 100,
    "speed": 10,
    "saves": 0,
    "height": 96,
    "width": 99
}

damsel = {
    "x": 200,
    "y": 200,
    "speed": 10
}

screen_size = (screen["width"], screen["height"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/city.jpg')
hero_image = pygame.image.load('images/ww.png')
hero_image_scaled = pygame.transform.scale(hero_image, (hero["width"],hero["height"]))
damsel_image = pygame.image.load('images/sm.png')
damsel_image_scaled = pygame.transform.scale(damsel_image, (99,136))

# Add music files
pygame.mixer.music.load("sounds/music.wav")
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound('sounds/win.wav')
lose_sound = pygame.mixer.Sound('sounds/lose.wav')


# /////////////////////////////////////////////////////
# ///////////////// MAIN GAME LOOP ////////////////////
# /////////////////////////////////////////////////////

game_on = True
# Create the game loop (while 1)
while game_on:
    # We are inside the main game loop. It will run as long as game_on is True
    #  ---EVENTS!---
    for event in pygame.event.get():
        # Add a quit event (requires sys)
        # Looping through all events that happened this game loop cycle
        if event.type == pygame.QUIT:
            # The user clicked on the red X to leave the game
            game.on = False
            # Update our boolean, so pygame can escape the loop
        elif event.type == pygame.KEYDOWN:
            # print event.key
            if event.key == keys['up']:
                keys_down['up'] = True
                # keys_down['w'] = True
            elif event.key == keys['down']:
                keys_down['down'] = True
                # keys_down['s'] = True
            elif event.key == keys['left']:
                keys_down['left'] = True
                # keys_down['a'] = True
            elif event.key == keys['right']:
                keys_down['right'] = True
                # keys_down['d'] = True
        elif event.type == pygame.KEYUP:
            if event.key == keys['up']:
                # the user let go of the key... and that key was the up arrow...
                keys_down['up'] = False
                # keys_down['w'] = False
            elif event.key == keys['down']:
                keys_down['down'] = False
                # keys_down['s'] = False
            elif event.key == keys['left']:
                keys_down['left'] = False
                # keys_down['a'] = False
            elif event.key == keys['right']:
                keys_down['right'] = False
                # keys_down['d'] = False

    # Update Hero position
    if keys_down['up']:
        # Add another if statement to keep player from moving off the top of the screen
        if hero['y'] > 0:
            hero['y'] -= hero['speed']
    elif keys_down['down']:
        # Add another if statement to keep player from moving off the bottom of the screen
        # You will need to make the char's Y position less than the height of the screen
        if hero['y'] < (screen['height'] - hero['height']):
            hero['y'] += hero['speed']
    if keys_down['left']:
        # Add another if statement to keep player from moving off the left side of the screen
        if hero['x'] > 0:
            hero['x'] -= hero['speed']
    elif keys_down['right']:
        # Add another if statement to keep player from moving off the right side of the screen
        # You will need to make the char's X position less than the width of the screen
        if hero['x'] < (screen['width'] - hero['width']):
            hero['x'] += hero['speed']


    # # Update Damsel position
    # if keys_down['w']:
    #     damsel['y'] -= damsel['speed']
    # elif keys_down['s']:
    #     damsel['y'] += damsel['speed']
    # if keys_down['a']:
    #     damsel['x'] -= damsel['speed']
    # elif keys_down['d']:
    #     damsel['x'] += damsel['speed']

# COLLISION DETECTION
    distance_between = fabs(hero['x'] - damsel['x']) + fabs(hero['y'] - damsel['y'])
    if (distance_between < 50):
    # the hero and damsel are touching!
        # print ("Collision!")
        # Generate random x > 0, x < screen['width']
        # Generate random y > 0, y < screen['height']
        rand_x = randint(0, screen['width'] - 200)
        rand_y = randint(0, screen['height'] - 200)
        damsel['x'] = rand_x
        damsel['y'] = rand_y
        # Update hero's wins
        hero['saves'] += 1
        win_sound.play()

    # ---RENDER!---
    # blit takes 2 arguments: (1) what? (2) where?
    # Screen.fill (pass bg_color)
    pygame_screen.blit(background_image, [0,0])

    # Draw the hero wins on the screen
    font = pygame.font.Font(None, 25)
    saves_text = font.render("Saves: %d" % (hero['saves']), True, (255,255,255))
    pygame_screen.blit(saves_text, [40,40])

    # draw the hero
    pygame_screen.blit(hero_image_scaled, [hero['x'],hero['y']])
    pygame_screen.blit(damsel_image_scaled, [damsel['x'],damsel['y']])

    # clear the screen for next time
    pygame.display.flip()






# Flip the screen and start over