import time
import pygame
import math

pygame.init()

screen = pygame.display.set_mode([1280, 720])

cube3d = [(1, 1, 1), 
        (1, 1, -1), 
        (1, -1, 1), 
        (1, -1, -1),
        (-1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1), 
        (-1, -1, -1)]

edges = [(0, 1),
        (0, 2),
        (0, 4),
        (1, 3),
        (1, 5),
        (2, 3),
        (2, 6),
        (3, 7),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7)]
        
# Makes Triangle 
#
#edges = [(0, 1),   
#          (0, 2),
#          (0, 3),
#          (1, 2),
#          (1, 3),
#          (2, 3)]

# cube3d = [(0, 0, 1),
#           (1, 0, 0),
#           (-0.58823529411,-0.8318903308, 0),
#           (-0.58823529411, 0.8318903308, 0)]

def rotate_xAxis(x, y, z):
    return x, y*math.cos(xtheta)+z*math.sin(xtheta), z*math.cos(xtheta)-y*math.sin(xtheta)

def rotate_yAxis(x, y, z):
    return x*math.cos(ytheta)-z*math.sin(ytheta), y, z*math.cos(ytheta)+x*math.sin(ytheta)

def rotate_zAxis(x, y, z):
    return x*math.cos(ztheta)+y*math.sin(ztheta), y*math.cos(ztheta)-x*math.sin(ztheta), z

def update():
    screen.fill((0, 0, 0))

    global xtheta, ytheta, ztheta

    xtheta = (xtheta+xSpeed)%(2*math.pi)

    ytheta = (ytheta+ySpeed)%(2*math.pi)

    ztheta = (ztheta+zSpeed)%(2*math.pi)

    cube2d = []
    for i in range(len(cube3d)):
        
        x_rot, y_rot, z_rot = rotate_zAxis(*rotate_yAxis(*rotate_xAxis(cube3d[i][0], cube3d[i][1], cube3d[i][2])))

        cube2d.append(((x_rot * fov / (fov + z_rot)) * 100 + screen.get_width() / 2,
                       (y_rot * fov / (fov + z_rot)) * 100 + screen.get_height() / 2))

    for i in range(len(edges)):
        pygame.draw.line(screen, (255, 255, 255), cube2d[edges[i][0]], cube2d[edges[i][1]])


    pygame.display.update()




running = True
prev = time.time()
lastcheck = time.time()
delta = 0
fps = 1/60
frames = 0
fov = 10
xtheta, ytheta, ztheta = 0, 0, 0
xSpeed, ySpeed, zSpeed = 0, 0, 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    curr = time.time()
    delta += (curr-prev)/fps
    prev = curr
    if delta >= 1:
        delta -= 1
        frames += 1
        update()
    # if time.time() - lastcheck >= 1:
    #     lastcheck = time.time()
    #     print("FPS: ", frames)
    #     frames = 0s
    keys = pygame.key.get_pressed() 

    if(keys[pygame.K_UP]):
        xSpeed += fps/5000
    if(keys[pygame.K_DOWN]):
        xSpeed -= fps/5000
    if(keys[pygame.K_LEFT]):
        ySpeed -= fps/5000
    if(keys[pygame.K_RIGHT]):
        ySpeed += fps/5000
    if(keys[pygame.K_j]):
        zSpeed += fps/5000
    if(keys[pygame.K_l]):
        zSpeed -= fps/5000


    xSpeed += xSpeed/30000*-1 #Resetting position
    ySpeed += ySpeed/30000*-1
    zSpeed += zSpeed/30000*-1


pygame.quit()