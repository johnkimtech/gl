import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from itertools import product
import random
import numpy as np


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

# static colors
# colors = tuple(product([1, 0], [1, 0], [1, 0]))


def random_colors(num_vertices=8, num_channels=3):
    return [
        [random.random() for __ in range(num_channels)] for _ in range(num_vertices)
    ]


# random colors

colors = random_colors()


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


def print_model_view_matrix():
    model_view_mat = glGetDoublev(GL_MODELVIEW_MATRIX)
    print(type(model_view_mat))
    print(model_view_mat)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # print_model_view_matrix()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    # print_model_view_matrix()
    glTranslatef(0.0, 0.0, -5)
    # print_model_view_matrix()
    rotation_angle = 1
    # exit()
    rotating = False

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
                elif event.key == pygame.K_c:
                    global colors
                    colors = random_colors()
                elif event.key == pygame.K_p:
                    # calculate
                    model_view_mat = glGetDoublev(GL_MODELVIEW_MATRIX)  # 4x4
                    vertx = np.array(vertices)  # 6x3
                    vertx = np.pad(vertx, ((0, 0), (0, 1)), constant_values=1)  # 6x4
                    transformed_vertx = vertx @ model_view_mat
                    print(transformed_vertx[:, :3])
                elif event.key == pygame.K_r:
                    rotating = not rotating

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEWHEEL:
                # print(event)
                # if event.button == pygame.BUTTON_WHEELDOWN:
                if event.y > 0:
                    glTranslatef(0, 0, 1)
                if event.y < 0:
                    glTranslatef(0, 0, -1)

        if rotating:
            glRotatef(rotation_angle, 0, 0, 0)
            # glRotatef(rotation_angle, 2, 1, 2)
        # print_model_view_matrix()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(20)


main()
