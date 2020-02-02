from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width,height=800,600

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0,0.0,1.0,0.0)
    glutWireTeapot(0.5)
    glFlush()
  

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(width,height)
glutInitWindowPosition(0,0)
glutCreateWindow(b'opengl window')
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
