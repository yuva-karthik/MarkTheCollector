import pygame as pyg
import random as rn
import math as mt
import time as tm

# Initialize Pygame
pyg.init()

# Load assets
icon = pyg.image.load('gameIcon.png')
p_avtr = pyg.image.load('mark.png')
c_avtr = pyg.image.load('dollar.png')
bg = pyg.image.load('grassbg.jpg')
bmb_avtr = pyg.image.load('bomb.png')
font = pyg.font.Font('Bear-Hug.ttf', 32)

# Window setup
class Window:
    def __init__(self):
        self.wn = pyg.display.set_mode((800, 600))
        pyg.display.set_caption("Mark the Collector")
        pyg.display.set_icon(icon)

screen = Window()
s1 = screen.wn

# Helper functions
def draw_image(image, pos):
    s1.blit(image, pos)

def check_collision(x1, y1, x2, y2, threshold=35):
    return mt.hypot(x1 - x2, y1 - y2) < threshold

def should_switch_bomb_position(score):
    return score % 2 == 0 or score % 3 == 0

def display_message(message, pos, color='green'):
    msg = font.render(message, True, color)
    s1.blit(msg, pos)

# Game variables
pX, pY = 400, 300
pX_change, pY_change = 0, 0
cX, cY = rn.randint(0, 738), rn.randint(60, 538)
bX, bY = rn.randint(80, 738), rn.randint(80, 518)
score = 0
move_speed = 0.3
game_over = False
pause = False

# Main loop
while True:
    s1.fill('black')
    s1.blit(bg, (0, 0))

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            exit()

        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_SPACE:
                pause = not pause
                if pause:
                    pX_change, pY_change = 0, 0
            if not pause:
                if event.key in {pyg.K_UP, pyg.K_w}:
                    pY_change = -move_speed
                if event.key in {pyg.K_DOWN, pyg.K_s}:
                    pY_change = move_speed
                if event.key in {pyg.K_RIGHT, pyg.K_d}:
                    pX_change = move_speed
                if event.key in {pyg.K_LEFT, pyg.K_a}:
                    pX_change = -move_speed

    # Update player position with boundaries
    pX = max(0, min(pX + pX_change, 738))
    pY = max(60, min(pY + pY_change, 538))

    # Check collisions
    if check_collision(pX, pY, cX, cY):
        score += 1
        cX, cY = rn.randint(0, 738), rn.randint(60, 538)
        if should_switch_bomb_position(score):
            bX, bY = rn.randint(0, 738), rn.randint(80, 518)
        if score % 12 == 0:
            move_speed += 0.1

    if check_collision(pX, pY, bX, bY):
        game_over = True

    if check_collision(bX, bY, cX, cY, 64):
        bX, bY = rn.randint(0, 738), rn.randint(80, 518)

    # Draw everything
    draw_image(c_avtr, (cX, cY))
    draw_image(bmb_avtr, (bX, bY))
    draw_image(p_avtr, (pX, pY))

    display_message(f'SCORE: {score}', (300, 10), 'yellow')

    if pause:
        display_message('PAUSE', (350, 300), 'blue')
    if game_over:
        display_message('<--GAME OVER-->', (260, 300))
        pause = True

    pyg.display.flip()
