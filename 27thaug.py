import pygame
import random
pygame.init()

screen = pygame.display.set_mode((600, 400))
player = pygame.Rect(300, 200, 40, 40)
zombies = [pygame.Rect(random.randint(0, 560), random.randint(0, 360), 40, 40) for _ in range(5)]
clock = pygame.time.Clock()

def move_zombie(zombie, player):
    if zombie.x < player.x: zombie.x += 1
    elif zombie.x > player.x: zombie.x -= 1
    if zombie.y < player.y: zombie.y += 1
    elif zombie.y > player.y: zombie.y -= 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 5
    if keys[pygame.K_RIGHT]: player.x += 5
    if keys[pygame.K_UP]: player.y -= 5
    if keys[pygame.K_DOWN]: player.y += 5

    for zombie in zombies:
        move_zombie(zombie, player)

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for zombie in zombies:
        pygame.draw.rect(screen, (100, 0, 0), zombie)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()