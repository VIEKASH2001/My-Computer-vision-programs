import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cv2
import numpy as np


camera = cv2.VideoCapture(0)
pygame.init()
screen = pygame.display.set_mode([640,480])
#DOUBLEBUF|OPENGLBLIT
while True:
    ret, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)#this converts the numpy arry to surface, pygame can take up only surfaces
    screen.blit(frame, (0,0))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            cv2.destroyAllWindows()
            quit()
