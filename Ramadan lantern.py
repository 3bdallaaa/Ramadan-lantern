#Mohamed Abdalla

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np

def myInit():
    glClearColor(0.8, 0.8, 0.8, 1) 
    gluOrtho2D(-250, 250, -250, 250) 

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.7, 0.1, 0.0) 
    glBegin(GL_POLYGON) # Base
    glVertex2f(-55, -180) #up right
    glVertex2f(55, -180) #up left
    glVertex2f(100, -210) #down right
    glVertex2f(-100, -210) #down left
    glEnd() 

    glBegin(GL_POLYGON) # Hat
    glVertex2f(-60, 160) #up right
    glVertex2f(60, 160) #up left
    glVertex2f(130, 70) #down right
    glVertex2f(-130, 70) #down left
    glEnd() 

    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON) # Body
    glVertex2f(100, 70) #up right
    glVertex2f(-100, 70) #up left
    glVertex2f(-50, -180) #down right
    glVertex2f(50, -180) #down left
    glEnd()
    
    glColor3f(0.9, 1, 0.2) 
    glBegin(GL_POLYGON) #Inner right
    glVertex2f(80, 40) #up right
    glVertex2f(4, 40) #up left
    glVertex2f(4, -140) #down left
    glVertex2f(45, -140) #down right
    glEnd()

    glBegin(GL_POLYGON) #Inner left
    glVertex2f(-80, 40) #up right
    glVertex2f(-4, 40) #up left
    glVertex2f(-4, -140) #down left
    glVertex2f(-45, -140) #down right
    glEnd()
    
    #Upper Ring
    glColor3f(0, 0, 0) #Black
    glBegin(GL_TRIANGLE_STRIP)
    inner_radius = 20 
    outer_radius = 25 
    for i in range(0, 361, 10):
        x = outer_radius * math.cos(math.radians(i))
        y = outer_radius * math.sin(math.radians(i)) +185 #position on y-axis
        glVertex2f(x, y)
        x = inner_radius * math.cos(math.radians(i))
        y = inner_radius * math.sin(math.radians(i)) +185
        glVertex2f(x, y)
    glEnd()
    glFlush()
    
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(450, 100) #mkan el window 3al screen
glutCreateWindow("Ramadan lantern") #title el window

myInit()
glutDisplayFunc(display)
glutMainLoop()
