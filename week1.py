import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np


# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Create a simple vertex shader
vertex_shader = """
#version 330 core
layout(location = 0) in vec4 position;
void main()
{
    gl_Position = position;
}
"""

# Create a simple fragment shader
fragment_shader = """
#version 330 core
out vec4 color;
void main()
{
    color = vec4(1.0, 0.0, 0.0, 1.0); // Red color
}
"""

# Create and compile shaders
vertex_shader_id = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vertex_shader_id, vertex_shader)
glCompileShader(vertex_shader_id)

fragment_shader_id = glCreateShader(GL_FRAGMENT_SHADER)
glShaderSource(fragment_shader_id, fragment_shader)
glCompileShader(fragment_shader_id)

# Create a shader program and link shaders
shader_program_id = glCreateProgram()
glAttachShader(shader_program_id, vertex_shader_id)
glAttachShader(shader_program_id, fragment_shader_id)
glLinkProgram(shader_program_id)

# Create vertices for a simple triangle
vertices = np.array([
    0.0,  1.0, 0.0,
   -1.0, -1.0, 0.0,
    1.0, -1.0, 0.0
], dtype=np.float32)

# Create a Vertex Array Object (VAO)
vao = glGenVertexArrays(1)
glBindVertexArray(vao)

# Create a Vertex Buffer Object (VBO)
vbo = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, vertices, GL_STATIC_DRAW)

# Specify the attribute pointer
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
glEnableVertexAttribArray(0)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Use the shader program
    glUseProgram(shader_program_id)

    # Bind the VAO
    glBindVertexArray(vao)

    # Draw the triangle
    glDrawArrays(GL_TRIANGLES, 0, 3)

    # Unbind the VAO and shader program
    glBindVertexArray(0)
    glUseProgram(0)

    pygame.display.flip()
    pygame.time.wait(10)
