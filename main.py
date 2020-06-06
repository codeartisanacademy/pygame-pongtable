import pygame
from paddle import Paddle
from ball import Ball

# initialize pygame library
pygame.init()

# setup our window
screen = pygame.display.set_mode([500, 800])

sprite_group = pygame.sprite.Group()

# create the object paddle
paddle = Paddle((255, 255, 255), 100, 10)
paddle.rect.x = (screen.get_width()/2) - (paddle.rect.width/2)
paddle.rect.y = 600

# create the ball
ball = Ball((0,0,0), 10, 10)
ball.rect.x = 345
ball.rect.y = 195

sprite_group.add(paddle)
sprite_group.add(ball)

clock = pygame.time.Clock()

running = True

while running:

    # events : click a button, swipe, pinch, tap
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(10)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(10, screen.get_width())
    # screen background color
    screen.fill((0, 255, 0))

    sprite_group.draw(screen)
    
    # display the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    