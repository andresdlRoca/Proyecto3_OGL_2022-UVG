import pygame
from pygame.locals import *
from pygame import mixer
from shaders import *

from gl import Renderer, Model

width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()
pygame.display.set_caption('Proyecto 3 OGL - Graficas por computadora')
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
pauseState = False

#Background music
mixer.music.load("backgroundsong.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.5)
#Sound effects
selectsfx = mixer.Sound("select.mp3")
selectsfx.set_volume(0.2)
seraphine = mixer.Sound("seraphine.mp3")
fallguy = mixer.Sound("fallguy.mp3")
mario = mixer.Sound("mario.mp3")
stormtrooper = mixer.Sound("stormtrooper.mp3")
limit = mixer.Sound("limit.mp3")
limit.set_volume(0.1)
mousepos = 0

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
            
            elif event.key == pygame.K_LCTRL:
                mousepos = pygame.mouse.get_pos()
            
        elif event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                if zoomCounter <= 80:
                    rend.camPosition.z -= 30 * deltaTime
                    zoomCounter += 3
                else:
                    limit.play()
            elif event.y == -1:
                if zoomCounter > 0:
                    rend.camPosition.z += 30*deltaTime
                    zoomCounter -= 3
                else:
                    limit.play()
        
        elif event.type == pygame.MOUSEMOTION:
            # print(pygame.mouse.get_pos())
            # mousepos = pygame.mouse.get_pos()
            
            if keys[K_LCTRL] and pygame.mouse.get_pos()[0] < mousepos[0]:
                if horiCounter > 0:
                    rend.camPosition.x -= 20 * deltaTime
                    horiCounter -= 8
                else:
                    limit.play()

            elif keys[K_LCTRL] and pygame.mouse.get_pos()[0] > mousepos[0]:
                if horiCounter <= 400:
                    rend.camPosition.x += 20 * deltaTime
                    horiCounter += 8
                else:
                    limit.play()
            
            if keys[K_LCTRL] and pygame.mouse.get_pos()[1] < mousepos[1]:
                if vertCounter <= 400:
                    rend.camPosition.y += 20 * deltaTime
                    vertCounter += 6
                else:
                    limit.play()

            elif keys[K_LCTRL] and pygame.mouse.get_pos()[1] > mousepos[1]:
                if vertCounter > 0:
                    rend.camPosition.y -= 20 * deltaTime
                    vertCounter -= 6
                else:
                    limit.play()

            # if(pygame.mouse.get_pos()[0] < mousepos[0]):

            # elif event.key == pygame.K_1: #Shader default
            #     rend.setShaders(vertex_shader, fragment_shader)
            
            # elif event.key == pygame.K_2: #Toon Shader
            #     rend.setShaders(vertex_shader, toon_shader)
            
            # elif event.key == pygame.K_3: #Glow Shader
            #     rend.setShaders(vertex_shader, glow_shader)
            
            # elif event.key == pygame.K_4: #Pink Jelly
            #     rend.setShaders(vertex_shader, pinkJelly_shader)
            # elif event.key == pygame.K_5: #Pulsating shader
            #     rend.setShaders(pulse_vertex_shader, pulse_fragment_shader)

    #General camera controls
    if keys[K_a]:
        if horiCounter > 0:
            rend.camPosition.x -= 10 * deltaTime
            horiCounter -= 4
        else:
            limit.play()
    elif keys[K_d]:
        if horiCounter <= 400:
            rend.camPosition.x += 10 * deltaTime
            horiCounter += 4
        else:
            limit.play()

    elif keys[K_w]:
        if vertCounter <= 400:
            rend.camPosition.y += 10 * deltaTime
            vertCounter += 3
        else:
            limit.play()

    elif keys[K_s]:
        if vertCounter > 0:
            rend.camPosition.y -= 10 * deltaTime
            vertCounter -= 3
        else:
            limit.play()

    if keys[K_e]: #Zoom in
        if zoomCounter <= 80:
            rend.camPosition.z -= 10 * deltaTime
            zoomCounter += 1
        else:
            limit.play()

    elif keys[K_q]: #Zoom out
        if zoomCounter > 0:
            rend.camPosition.z += 10*deltaTime
            zoomCounter -= 1
        else:
            limit.play()

    if keys[K_p]:
        if pauseState == False:
            mixer.music.pause()
            pauseState = True
        else:
            mixer.music.unpause()
            pauseState = False
    
    # if keys[K_f]: #Left circular
    #     # if rend.camPosition.z >= -5.5 <=0:
    #     #     rend.camPosition.z -= 10 * deltaTime
    #     #     rend.camPosition.x -= 10 * deltaTime 
    #     # elif rend.camPosition.z <= -5.5:
    #     #     rend.camPosition.z -= 10 * deltaTime
    #     #     rend.camPosition.x += 10*deltaTime
        

    # elif keys[K_g]: #Right circular

    #     # if rend.camPosition.z >= -5.5 <= 0: 
    #     #     rend.camPosition.z -= 10 * deltaTime
    #     #     rend.camPosition.x += 10 * deltaTime
    #     # elif rend.camPosition.z <= -5.5:
    #     #     rend.camPosition.z += 10 * deltaTime
    #     #     rend.camPosition.x += 10 * deltaTime    
    #     print(rend.camPosition.x)

    #Light control
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime

    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime
    
    #Shaders
    if keys[K_1]: #Shader default
        selectsfx.play()
        rend.setShaders(vertex_shader, fragment_shader)

    elif keys[K_2]: #Toon shader
        selectsfx.play()
        rend.setShaders(vertex_shader, toon_shader)

    elif keys[K_3]: #Glow/negative shader
        selectsfx.play()
        rend.setShaders(vertex_shader, glow_shader)

    elif keys[K_4]: #Pink jelly shader
        selectsfx.play()
        rend.setShaders(vertex_shader, pinkJelly_shader)
    
    elif keys[K_5]: #Pulse shader
        selectsfx.play()
        rend.setShaders(pulse_vertex_shader, pulse_fragment_shader)


    if keys[K_LSHIFT] and keys[K_1]:
        seraphine.play()
        rend.scene.clear()
        face = Model("seraphine.obj", "seraphine.bmp")

        face.position.z -= 5
        face.scale.x = 2
        face.scale.y = 2
        face.scale.z = 2

        rend.scene.append( face )
        print("Modelo 1")
    
    elif keys[K_LSHIFT] and keys[K_2]:
        fallguy.play()
        rend.scene.clear()
        face = Model("fallguy.obj", "seraphine.bmp")

        face.position.z -= 5
        face.position.y -= 1
        face.scale.x = 2
        face.scale.y = 2
        face.scale.z = 2
        rend.scene.clear()
        rend.scene.append( face )
        print("Modelo 2")

    elif keys[K_LSHIFT] and keys[K_3]:
        seraphine.play()
        rend.scene.clear()
        # rend.target.z = -20
        face = Model("girl.obj", "girl.bmp")
        face.position.y -= 5
        face.position.z -= 5
        face.scale.x = 0.05
        face.scale.y = 0.05
        face.scale.z = 0.05

        rend.scene.append( face )
        print("Modelo 3")

    elif keys[K_LSHIFT] and keys[K_4]:
        mario.play()
        rend.scene.clear()

        face = Model("mario.obj", "bone.bmp")

        face.position.z -= 5
        face.position.y -= 5
        face.scale.x = 1
        face.scale.y = 1
        face.scale.z = 1

        rend.scene.append( face )
        print("Modelo 4")

    elif keys[K_LSHIFT] and keys[K_5]:
        stormtrooper.play()
        rend.scene.clear()

        face = Model("stormtrooper.obj", "stormtrooper.bmp")

        face.position.z -= 5
        face.position.y -= 3
        face.scale.x = 2
        face.scale.y = 2
        face.scale.z = 2

        rend.scene.append( face )
        print("Modelo 5")

    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime
    #print(deltaTime)

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
