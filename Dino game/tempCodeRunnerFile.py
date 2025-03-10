import pygame
import random






# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0 

#player setup
player = pygame.Rect(40,screen.get_height() - 60,60,60)
gravity = 500
velocity_y = 0

#obstacoles setup
x = random.randint(60, screen.get_width())
obstacle = pygame.Rect(x, screen.get_height() - 60,60,60)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    
    
    
    
    pygame.draw.rect(screen, 'red', player,)
    pygame.draw.rect(screen, 'black', obstacle)
    pygame.draw.rect(screen, 'black', obstacle)
    

    #make obstacle move twoard you
    obstacle.x -= 300 * dt





    #Jump input
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        velocity_y = -300

    #apply gravity
    velocity_y += gravity * dt
    player.y += velocity_y * dt

      # Prevent the player from falling below the bottom of the screen
    if player.bottom > screen.get_height():
        player.bottom = screen.get_height()
        velocity_y = 0

   # Check if the obstacle is off-screen
    if obstacle.right < 0:
        x = random.randint(40, screen.get_width() - 60)  # Randomize new x position
        obstacle.topleft = (x, screen.get_height() - 60)











    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()