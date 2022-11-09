import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model

width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

rend.target.z = -5

face = Model("seraphine.obj", "seraphine.bmp")

face.position.z -= 5
face.scale.x = 2
face.scale.y = 2
face.scale.z = 2

rend.scene.append( face )

zoomCounter = 50
vertCounter = 200
horiCounter = 200
isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            
            elif event.key == pygame.K_z:
                rend.filledMode()
            elif event.key == pygame.K_x:
                rend.wireframeMode()
            
            elif event.key == pygame.K_1: #Shader default
                rend.setShaders(vertex_shader, fragment_shader)
            
            elif event.key == pygame.K_2: #Toon Shader
                rend.setShaders(vertex_shader, toon_shader)
            
            elif event.key == pygame.K_3: #Glow Shader
                rend.setShaders(vertex_shader, glow_shader)
            
            elif event.key == pygame.K_4: #Pink Jelly
                rend.setShaders(vertex_shader, pinkJelly_shader)
            elif event.key == pygame.K_5: #Pulsating shader
                rend.setShaders(pulse_vertex_shader, pulse_fragment_shader)


    if keys[K_a]:
        if vertCounter > 0:
            rend.camPosition.x -= 10 * deltaTime
            vertCounter -= 4
        else:
            print("Limite de movimiento horizontal izquierdo alcanzado")

    elif keys[K_d]:
        if vertCounter <= 400:
            rend.camPosition.x += 10 * deltaTime
            vertCounter += 4
        else:
            print("Limite de movimiento horizontal derecho alcanzado")
    
    elif keys[K_w]:
        if vertCounter <= 400:
            rend.camPosition.y += 10 * deltaTime
            vertCounter += 3
        else:
            print("Limite de movimiento vertical superior alcanzado")
    
    elif keys[K_s]:
        if vertCounter > 0:
            rend.camPosition.y -= 10 * deltaTime
            vertCounter -= 3
        else:
            print("Limite de movimiento vertical inferior alcanzado")

    if keys[K_e]: #Zoom in
        if zoomCounter <= 100:
            rend.camPosition.z -= 10 * deltaTime
            zoomCounter += 1
        else:
            print("Limite de zoom in alcanzado")


    elif keys[K_q]: #Zoom out
        if zoomCounter > 0:
            rend.camPosition.z += 10*deltaTime
            zoomCounter -= 1
        else:
            print("Limite de zoom out alcanzado")

    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime

    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime

    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime
    #print(deltaTime)

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
