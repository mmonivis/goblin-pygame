import pygame
from math import fabs
from random import randint

# GLOBAL CONSTANTS ---

pygame.init()

screen = {
    "height": 650,
    "width": 1152,
}

keys = {
    "right": 275,
    "left": 276,
    "up": 273,
    "down": 274,
    # "w": 119,
    # "a": 97,
    # "s": 115,
    # "d": 100
}

keys_down = {
    "right": False,
    "left": False,
    "up": False,
    "down": False,
    # "w": False,
    # "a": False,
    # "s": False,
    # "d": False
}

hero = {
    "x": 100,
    "y": 100,
    "speed": 10,
    "wins": 0,
    "height": 126,
    "width": 99
}

enemy = {
    "x": 200,
    "y": 200,
    "speed": 2,
    "direction": "N"
}

directions = ['N','S','E','W','NE','NW','SE','SW']

tick = 0

screen_size = (screen["width"], screen["height"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('./images/ff7bg.jpg')
hero_image = pygame.image.load('./images/cloud.png')
hero_image_scaled = pygame.transform.scale(hero_image, (hero["width"],hero["height"]))
enemy_image = pygame.image.load('./images/seph.png')
enemy_image_scaled = pygame.transform.scale(enemy_image, (130,130))

# Music files
pygame.mixer.music.load("sounds/music.wav")
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound('sounds/win.wav')
lose_sound = pygame.mixer.Sound('sounds/lose.wav')

# END GLOBAL CONSTANTS ---


def main():

    tick = 0

    game_on = True
    while game_on:
        tick += 1
        #  ---EVENTS!--- Keystrokes OR Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.on = False
            elif event.type == pygame.KEYDOWN:
                for keystroke in keys:
                    if event.key == keys[keystroke]:
                        keys_down[keystroke] = True
            elif event.type == pygame.KEYUP:
                for keystroke in keys:
                    if event.key == keys[keystroke]:
                        keys_down[keystroke] = False
        # --- END EVENTS ---

        def movements():


            # HERO MOVEMENTS WITHIN SCREEN
            if keys_down['up']:
                if hero['y'] > 0:
                    hero['y'] -= hero['speed']
            elif keys_down['down']:
                if hero['y'] < (screen['height'] - hero['height']):
                    hero['y'] += hero['speed']
            if keys_down['left']:
                if hero['x'] > 0:
                    hero['x'] -= hero['speed']
            elif keys_down['right']:
                if hero['x'] < (screen['width'] - hero['width']):
                    hero['x'] += hero['speed']

            # ENEMY MOVEMENTS
            if (enemy['direction'] == 'N'):
                enemy['y'] -= enemy['speed']
            elif (enemy['direction'] == 'S'):
                enemy['y'] += enemy['speed']
            elif (enemy['direction'] == 'E'):
                enemy['x'] += enemy['speed']
            elif (enemy['direction'] == 'W'):
                enemy['x'] -= enemy['speed']
            elif (enemy['direction'] == 'NE'):
                enemy['y'] -= enemy['speed']
                enemy['x'] += enemy['speed']
            elif (enemy['direction'] == 'NW'):
                enemy['y'] -= enemy['speed']
                enemy['x'] -= enemy['speed']
            elif (enemy['direction'] == 'SE'):
                enemy['y'] += enemy['speed']
                enemy['x'] += enemy['speed']
            elif (enemy['direction'] == 'SW'):
                enemy['y'] += enemy['speed']
                enemy['x'] -= enemy['speed']

            # KEEP ENEMY IN SCREEN
            if (enemy['x'] > screen['width']):
                enemy['x'] = 0
            elif (enemy['x'] < 0):
                enemy['x'] = screen['width']
            if (enemy['y'] > screen['height']):
                enemy['y'] = 0
            elif (enemy['y'] < 0):
                enemy['y'] = screen['height']

            # KEEP ENEMY FROM SPAZZING
            if (tick % 60 == 0):
                new_dir_index = randint(0,len(directions)-1)
                enemy['direction'] = directions[new_dir_index]

        movements()

        def collision():

            # COLLISION DETECTION
            distance_between = fabs(hero['x'] - enemy['x']) + fabs(hero['y'] - enemy['y'])
            if (distance_between < 50):
                rand_x = randint(0, screen['width'] - 200)
                rand_y = randint(0, screen['height'] - 200)
                enemy['x'] = rand_x
                enemy['y'] = rand_y
                hero['wins'] += 1 # Update hero wins
                win_sound.play()

        collision()

    # --- RENDER ---
        pygame_screen.blit(background_image, [0,0])

        font = pygame.font.Font(None, 25)
        wins_text = font.render("Wins: %d" % (hero['wins']), True, (255,255,255))
        pygame_screen.blit(wins_text, [40,40])

        pygame_screen.blit(hero_image_scaled, [hero['x'],hero['y']])
        pygame_screen.blit(enemy_image_scaled, [enemy['x'],enemy['y']])

        pygame.display.flip()

main()