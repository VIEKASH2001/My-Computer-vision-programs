#opengl cannot display on windows by itself
#so for this sole purpose we use packages like glut,glfw
#these are called modern opengl
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#window width and height
width,height=800,600

def draw():
    #clear screen first always GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT
    #glClear(GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClearDepth(1.0)
    #reset your position
    glLoadIdentity()
    #buffer swaping is done for the purpose of double buffering
    glutSwapBuffers()

#initialization
glutInit()
#specify the type of window
glutInitDisplayMode(GLUT_RGBA)
#set window size and height
glutInitWindowSize(width,height)
#set window position
glutInitWindowPosition(0,0)
#create window
window=glutCreateWindow(b'opengl window')
#set the function callback to display what has to be drawn
glutDisplayFunc(draw)
#to perform what has to be done in the window
glutIdleFunc(draw)
#main loop: the whole glut functions will be repeating itself again and again
glutMainLoop()
