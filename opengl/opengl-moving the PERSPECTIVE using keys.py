import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#drawing a square pyramid
vertices=((1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(0,0,1)) #take them im tupels, so here it is tuple of tuples
edges=((0,1),(0,3),(0,4),(1,4),(1,2),(2,4),(2,3),(3,4))#here 0,1,2,3,4 are the numberings given to the vertices and (0,1) means the connection between 0 and 1

def pyramid():
    glLineWidth(5)#fixing the line width to 5 pixels
    glBegin(GL_LINES)#it starts drawing lines
    #this for loop draws the vertices and edges (the connection of edges is done automatically)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])#this draws the vertices
            glColor3f(1,0,0)#(R,G,B)
    glEnd()#to end the process

#now pygame is used to draw the window for displaying this object    
pygame.init()#to initialize pygame
display=(400,400)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)#(display window size, <a parameter to say the computer that we are using opengl in the window>)
gluPerspective(70, (display[0]/display[1]),0.1,50)#to mention the perspective in which we want to view it (field of view in degree, aspect ratio= width/height=800/800 in here but we can put it as our own like 1/2 or so, z-near(just a small value), z-far(a big value))
glTranslatef(0,0,-5)#usually our view is in the (0,0,0) from here we can just see the inside of the shape so in order to see from outside we translate along the z coordinate
clock=pygame.time.Clock()#to set the frame rate
vel =0.1#this is the velocity or the distance that the object is translated in each click of keys
#this loop facilitates the game/graphics
while True:
    clock.tick(60)#frame rate is set as 60
    #this loop is just to quit out of the window and also to rotate the shape (all the details of the events are listed in here)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#if we press the close button in window it comes out
            pygame.quit()
            quit()
    #to rotate the perspective        
    #glRotatef(2,1,1,3) #to rotate the object in the window (rotation speed, x rotation, y rotation , z rotation)
    #WHEN WE ROTATE THE PERSPECTIVE OF THE IMAGE CHANGES BUT THE OBJECT DOESNT CHANGE
    #SAME WAY IF WE WANT TO CONTROL OBJECT MOVEMENTS WITH KEYS WE CAN DO THAT BY CHANGING THE PERSPECTIVE ALONE
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        glTranslatef(-vel,0,0)#left is negative direction so -vel
    if keys[pygame.K_RIGHT]:
        glTranslatef(vel,0,0)
    if keys[pygame.K_UP]:
        glTranslatef(0,vel,0)
    if keys[pygame.K_DOWN]:
        glTranslatef(0,-vel,0)
    if keys[pygame.K_t]:#t key for forward
        glTranslatef(0,0,vel)
    if keys[pygame.K_g]:#g key for backward
        glTranslatef(0,0,-vel)   
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)#clear the display so that we can redraw the display on the same window so that images of each frame donot pile up on each other
    pyramid()#generates the graphics
    pygame.display.flip()#updates the display that is it creates the generated graphics in the window
    
            

