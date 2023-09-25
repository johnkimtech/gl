import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1),
)
edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
)

surfaces = (
    (0, 1, 2, 3),
    (0, 3, 7, 4),
    (0, 1, 5, 4),
    (6, 5, 4, 7),
    (6, 2, 3, 7),
    (6, 2, 1, 5),
)

# colors for vertices
from itertools import product
colors = tuple(product([1,0],[1,0],[1,0]))

def draw_cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3fv((0, 1, 0))
        for vertex in surface:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv((0, 0, 0))
        for vertex in edge:
            glColor3fv(colors[-vertex])
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    rotation_angle = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    rotation_angle += 5
                elif event.key == pygame.K_1:
                    rotation_angle -= 5

        glRotatef(rotation_angle, 2, 1, 2)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(20)


main()
