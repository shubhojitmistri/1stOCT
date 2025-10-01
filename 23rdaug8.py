import pygame
import sys

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pygame.Rect(50, 50, 30, 30)
speed = [3, 3]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball = ball.move(speed)
    if ball.left < 0 or ball.right > width:
        speed[0] = -speed[0]
    if ball.top < 0 or ball.bottom > height:
        speed[1] = -speed[1]

    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (0, 255, 0), ball)
    pygame.display.flip()
    clock.tick(60)