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


xSpeed, ySpeed, zSpeed = 0, 0, 0

def rotate_point(x, y, z): #Unused
    x_rot = x
    y_rot = y * math.cos(theta) - z * math.sin(theta)
    z_rot = y * math.sin(theta) + z * math.cos(theta)
    
    x_final = x_rot * math.cos(theta) - y_rot * math.sin(theta)
    y_final = x_rot * math.sin(theta) + y_rot * math.cos(theta)
    z_final = z_rot

    return x_final, y_final, z_final

def rotate_xAxis(x, y, z):
    return 0, y*math.cos(xSpeed)+z*math.sin(xSpeed), z*math.cos(xSpeed)-y*math.sin(xSpeed)

def rotate_yAxis(x, y, z):
    return x*math.cos(ySpeed)-z*math.sin(ySpeed), 0, z*math.cos(ySpeed)+x*math.sin(ySpeed)

def rotate_zAxis(x, y, z):
    return x*math.cos(zSpeed)+y*math.sin(zSpeed), y*math.cos(zSpeed)-x*math.sin(zSpeed), 0

def add_rotations(xx, xy, xz, yx, yy, yz, zx, zy, zz): #For Simplicity
    return xx+yx+zx, xy+yy+zy, xz+yz+zz

def update():
    screen.fill((0, 0, 0))


    # global theta
    # theta = (theta + speed)# + (2*math.pi/(360*2))) 
    # ^^^^ Probably need something like this to fix rotation, maybe setup vel/accel?

    cube2d = []
    for i in range(len(cube3d)):
        #x_rot, y_rot, z_rot = rotate_point(cube3d[i][0], cube3d[i][1], cube3d[i][2])
        x_rot, y_rot, z_rot = add_rotations(*rotate_xAxis(cube3d[i][0], cube3d[i][1], cube3d[i][2]), *rotate_yAxis(cube3d[i][0], cube3d[i][1], cube3d[i][2]), *rotate_zAxis(cube3d[i][0], cube3d[i][1], cube3d[i][2]))
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
theta = 0
accel = 1.0 #Values above 1.0000009 tend to break rotation

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
        xSpeed += fps/1000
    if(keys[pygame.K_DOWN]):
        xSpeed -= fps/1000
    if(keys[pygame.K_LEFT]):
        ySpeed -= fps/1000
    if(keys[pygame.K_RIGHT]):
        ySpeed += fps/1000
    if(keys[pygame.K_j]):
        zSpeed += fps/1000
    if(keys[pygame.K_l]):
        zSpeed -= fps/1000


    xSpeed *= accel #Unused
    ySpeed *= accel 
    zSpeed *= accel 

    #print(xSpeed)

    xSpeed += xSpeed/30000*-1 #Resetting position
    ySpeed += ySpeed/30000*-1
    zSpeed += zSpeed/30000*-1


pygame.quit()