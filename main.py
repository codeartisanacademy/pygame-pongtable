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
font = pygame.font.SysFont("Arial", 60)
score = 0

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

    # if the ball hit the right wall
    if ball.rect.x >= screen.get_width():
        ball.velocity[0] = -ball.velocity[0]

    # if the ball hit the left wall
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]

    # if the ball hit top wall
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]
    
    #display the score
    
    score_text = font.render(str(score), 1, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    # if the ball hit the bottom
    if ball.rect.y >= screen.get_height():
        gameover_text = font.render("Game Over", 1, (255,0,0))
        screen.blit(gameover_text, (screen.get_width()/2, screen.get_height()/2))
        ball.stop()
        print(score)

    if pygame.sprite.collide_mask(ball, paddle):
        score += 1
        ball.bounce()

    sprite_group.update()
    sprite_group.draw(screen)



    # display the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    