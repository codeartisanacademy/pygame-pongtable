import pygame
from paddle import Paddle

# initialize pygame library
pygame.init()

# setup our window
screen = pygame.display.set_mode([500, 800])

sprite_group = pygame.sprite.Group()
paddle = Paddle((255, 255, 255), 100, 10)
paddle.rect.x = 100
paddle.rect.y = 600
sprite_group.add(paddle)

running = True

while running:

    # events : click a button, swipe, pinch, tap
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False

    # screen background color
    screen.fill((0, 255, 0))

    sprite_group.draw(screen)
    
    # display the screen
    pygame.display.flip()

pygame.quit()
    