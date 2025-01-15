keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT]):
        speed -= fps/1000
    if(keys[pygame.K_RIGHT]):
        speed += fps/1000