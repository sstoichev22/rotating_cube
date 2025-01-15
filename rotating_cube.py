import time
import pygame
import math

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([1280, 720])
font = pygame.font.SysFont('Arial', 30)

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



def rotate_x(x, y, z):
    x_rot = x
    y_rot = y * math.cos(xtheta) - z * math.sin(xtheta)
    z_rot = y * math.sin(xtheta) + z * math.cos(xtheta)
    return x_rot, y_rot, z_rot

def rotate_y(x, y, z):
    x_rot = x * math.cos(ytheta) + z * math.sin(ytheta)
    y_rot = y
    z_rot = z * math.cos(ytheta) - x * math.sin(ytheta)
    return x_rot, y_rot, z_rot

def rotate_z(x, y, z):
    x_rot = x * math.cos(ztheta) - y * math.sin(ztheta)
    y_rot = x * math.sin(ztheta) + y * math.cos(ztheta)
    z_rot = z
    return x_rot, y_rot, z_rot

def update():
    screen.fill((0, 0, 0))

    global xtheta, ytheta, ztheta

    xtheta = (xtheta+xspeed)%(2*math.pi)

    ytheta = (ytheta+yspeed)%(2*math.pi)

    ztheta = (ztheta+zspeed)%(2*math.pi)
    
    cube2d = []
    for i in range(len(cube3d)):
        x_rot, y_rot, z_rot = rotate_x(*rotate_y(*rotate_z(cube3d[i][0], cube3d[i][1], cube3d[i][2])))
        cube2d.append(((x_rot * fov / (fov + z_rot)) * 100 + screen.get_width() / 2,
                       (y_rot * fov / (fov + z_rot)) * 100 + screen.get_height() / 2))

    for i in range(len(edges)):
        pygame.draw.line(screen, (255, 255, 255), cube2d[edges[i][0]], cube2d[edges[i][1]])

    currvar_text = font.render(currvar, True, (255, 255, 255))
    screen.blit(currvar_text, (3*screen.get_width()/4, screen.get_height()/2))

    x_text = font.render("x:%.5f"%xtheta, True, (255, 255, 255))
    screen.blit(x_text, (3*screen.get_width()/4, screen.get_height()/2+50))

    y_text = font.render("y:%.5f"%ytheta, True, (255, 255, 255))
    screen.blit(y_text, (3*screen.get_width()/4, screen.get_height()/2+100))

    z_text = font.render("z:%.5f"%ztheta, True, (255, 255, 255))
    screen.blit(z_text, (3*screen.get_width()/4, screen.get_height()/2+150))

    pygame.display.update()




running = True
prev = time.time()
lastcheck = time.time()
delta = 0
fps = 1/60
frames = 0
fov = 10
xtheta, ytheta, ztheta = 0, 0, 0
xspeed, yspeed, zspeed = 0, 0, 0
currvar = 'x'

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
    #     frames = 0

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT]):
        if currvar == 'x':
            xspeed -= fps/1000
        if currvar == 'y':
            yspeed -= fps/1000
        if currvar == 'z':
            zspeed -= fps/1000
    if(keys[pygame.K_RIGHT]):
        if currvar == 'x':
            xspeed += fps/1000
        if currvar == 'y':
            yspeed += fps/1000
        if currvar == 'z':
            zspeed += fps/1000
    if(keys[pygame.K_x]):
        currvar = 'x'
    if(keys[pygame.K_y]):
        currvar = 'y'
    if(keys[pygame.K_z]):
        currvar = 'z'
    print("x:%f"%xspeed,"\ny:%f"%yspeed,"\nz:%f"%zspeed)

    xspeed += xspeed/75000*-1
    yspeed += yspeed/75000*-1
    zspeed += zspeed/75000*-1


pygame.quit()