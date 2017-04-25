background_image_filename = 'bg.jpg'
sprite_image_filename = 'bg1.png'
needle_filename = 'needle.png'

WIN_SIZE = (640, 640)

import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()
pygame.display.set_caption("prize")
screen = pygame.display.set_mode(WIN_SIZE, 0, 32)
background = pygame.image.load(background_image_filename).convert()     #background image
pan = pygame.image.load(sprite_image_filename).convert_alpha()          #circle pan
needle = pygame.image.load(needle_filename).convert_alpha()             #needle to rotate

clock = pygame.time.Clock()

needle_rotation = 0.
needle_rotation_speed = 0.
needle_pos = (320, 320)

END_LIMIT = random.randint(15, 25)
isRotated = False;# tag, indicates whether needle is rotating

def rotateNeedle():
    rotated_needle = pygame.transform.rotate(needle, needle_rotation)
    w, h = rotated_needle.get_size()
    needle_draw_pos = needle_pos[0] - w / 2, needle_pos[1] - h / 2
    screen.blit(rotated_needle, needle_draw_pos)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            exit()
    screen.blit(background, (0,0))
    pw,ph = pan.get_size()
    screen.blit(pan, ((WIN_SIZE[0] - pw) * 0.5, (WIN_SIZE[1] - ph) * 0.5))
    
    pressed_mouse = pygame.mouse.get_pressed()
    #if pressed_keys[K_UP] or pressed_mouse[0]:
    if pressed_mouse[0] and not isRotated:
        needle_rotation = 0.
        needle_rotation_speed = 480.
        isRotated = True
        END_LIMIT = random.randint(15, 100)
    
    rotateNeedle()
    
    #set fps 60
    time_passed = clock.tick(60)
    time_passed_seconds = time_passed / 1000.0

    #rotate with speed reducing
    needle_rotation -= needle_rotation_speed * time_passed_seconds
    needle_rotation_speed *= 0.995
    #terminate rotation on condition
    if needle_rotation_speed <= END_LIMIT:
        needle_rotation_speed = 0
        isRotated = False

    pygame.display.update()