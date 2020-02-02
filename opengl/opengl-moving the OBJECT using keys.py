import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

#TO MOVE THE OBJECT ITSELF WE HAVE TO MODIFY THE VERTICES
#in order to make this process easier create a class to draw these shapes
#by changing the coordinates of vertices the perspective can also be changed 

class Pyramid:
    vertices = [
        [1, -1, -1],
        [1, -1, 1],
        [-1, -1, 1],
        [-1, -1, -1],
        [0, 1, 0]
    ]

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (1, 4),
        (1, 2),
        (2, 4),
        (2, 3),  # (2,3)
        (3, 4)
    )

    def __init__(self, mul=1):
        self.edges = Pyramid.edges
        self.vertices = list(numpy.multiply(numpy.array(Pyramid.vertices), mul))

    def draw(self):
        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(0, 1, 0)
        glEnd()

    def move(self, x, y, z):
        self.vertices = list(map(lambda vert: (vert[0] + x, vert[1] + y, vert[2] + z), self.vertices))


def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(70, (display[0]/display[1]), 0.1, 50)
    #glRotatef(90,1,0,0) #this will also help in changing the perspective if added
    glTranslatef(0,0,-20)

    p = Pyramid(2)

    vel = 0.1
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            p.move(-vel, 0, 0)
        if keys[pygame.K_RIGHT]:
            p.move(vel, 0, 0)
        if keys[pygame.K_UP]:
            p.move(0, vel, 0)
        if keys[pygame.K_DOWN]:
            p.move(0, -vel, 0)
        if keys[pygame.K_t]:
            p.move(0, 0, vel)
        if keys[pygame.K_g]:
            p.move(0, 0, -vel)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        p.draw()
        pygame.display.flip()


main()
