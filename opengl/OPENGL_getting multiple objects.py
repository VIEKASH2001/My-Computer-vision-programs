import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()
    
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0,0, -10)

    object_passed=False

    while not object_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)

                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)

##            if event.type == pygame.MOUSEBUTTONDOWN:
##                if event.button == 4:#this means scroll up
##                    glTranslatef(0,0,1.0)
##
##                if event.button == 5:#this means scroll down
##                    glTranslatef(0,0,-1.0)

        x=glGetDoublev(GL_MODELVIEW_MATRIX)  #GIVES THE LOCATION OF CUBE IN COORDINATE MATRIX  
        print(x)#read the matrix and decode it for future references

        #these are the respective positions of the cube 
        camera_z=x[3][2]
        camera_y=x[3][2]
        camera_x=x[3][1]

        glTranslatef(0,0,0.1)
               
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()#to move the object in z direction automatically
        pygame.display.flip()
        pygame.time.wait(10)#delay for 10 milli seconds

        if(camera_z<0): #according to this if the image,s z coordinate is less than one the graphics will stop
            object_passed=True #this will make it come out of the loop


for x in range(10):#by doing this we can play the animation 10 times
    main()

