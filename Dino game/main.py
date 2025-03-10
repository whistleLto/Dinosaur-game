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
can_jump = True
paused = False
score = 0
score_level_up = 0

# Label setup
font = pygame.font.Font(None, 36)  # Default font, size 36
label_text = "Score: 0"
text_surface = font.render(label_text, True, 'black')  # Render text with anti-aliasing
text_rect = text_surface.get_rect(topleft=(10, 10))  # Position the label at the top left


#obstacoles setup
x = random.randint(60, screen.get_width())
obstacle = pygame.Rect(x, screen.get_height() - 60,60,60)
speed = 300






while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    if score_level_up == 5:
        speed += 40
        score_level_up = 0
    
    
    
    pygame.draw.rect(screen, 'red', player,)
    pygame.draw.rect(screen, 'black', obstacle)
    screen.blit(text_surface, text_rect)
    

    #make obstacle move twoard you
    if paused == False:
        obstacle.x -= speed * dt





    #Jump input
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and can_jump == True and paused == False:
        velocity_y = -300
        can_jump = False

    #apply gravity
    if paused == False:
        velocity_y += gravity * dt
        player.y += velocity_y * dt

      # Prevent the player from falling below the bottom of the screen
    if player.bottom > screen.get_height():
        player.bottom = screen.get_height()
        velocity_y = 0
        can_jump = True

   # Reset obstacle when it moves off-screen
    if obstacle.right < 0:
        obstacle.left = screen.get_width()  # Respawn on the right edge
        score += 1
        score_level_up += 1
        label_text = f"score: {score}"
        text_surface = font.render(label_text, True, 'black')

    #detect collison
    if player.colliderect(obstacle):
        paused = True
        label_text = f"gameover: {score}, press space to restart the game"
        text_surface = font.render(label_text, True, 'black')
        if key[pygame.K_SPACE]:
            paused = False
            obstacle.x = random.randint(60, screen.get_width())
            obstacle.y = screen.get_height() - 60
            score = 0
            label_text = f"score: {score}"
            text_surface = font.render(label_text, True, 'black')












    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()