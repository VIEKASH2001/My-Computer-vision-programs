import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

#for surfaces we have to do like edges, we have 3 elements for each triangular surface
#quads are used to draw surfaces
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
        (2, 3),  
        (3, 4)
    )

    surfaces = (
        (1,2,4),
        (0,1,2,3),
        (0,1,4),
        (0,3,4),
        (2,3,4)
    )

    colors=( #this is done in order to get different colors for each surfaces
        (0,1,0),
        (1,0,0),
        (0,0,1),
        (0,1,0),
        (1,0,0),
      )  
    def __init__(self, mul=1):
        self.edges = Pyramid.edges
        self.vertices = list(numpy.multiply(numpy.array(Pyramid.vertices), mul))#list wil convert the datatype to list as the gl functions can take in only lists
        self.surfaces = Pyramid.surfaces
        self.colors=Pyramid.colors
        
    def draw(self):
        self.draw_sides() #invoking the below function in here
        glLineWidth(10)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
               # glColor3f(0, 1, 0)#edges in green color
                glVertex3fv(self.vertices[vertex])

        glEnd()

    def draw_sides(self):
        glBegin(GL_QUADS)
        x=0#gives surface count for the pupose of colouring
        for surface in self.surfaces:
            for vertex in surface:
                glColor3f(self.colors[x][0],self.colors[x][1],self.colors[x][2])#surfaces with different colors 
                glVertex3fv(self.vertices[vertex])
            x+=1
        glEnd()

    def move(self, x, y, z):
        self.vertices = list(map(lambda vert: (vert[0] + x, vert[1] + y, vert[2] + z), self.vertices))


def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0,0,-20)
    glEnable(GL_DEPTH_TEST)#makes the image solid... to have a solid image include this also

    p = Pyramid(2)#2 is the multiplicative factor

    vel = 0.1
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN: #THIS IS JUST TO CHECK WETHER THE KEYS OR MOUSE IS PRESSED. IF ONLY KEYS ARE USED THEN NO NEED TO USE THIS
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
