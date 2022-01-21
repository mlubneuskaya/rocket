import pygame
from random import randint
from rocket import Rocket, AutoPilotRocket
from vector import Vector


pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Rockets')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)  # nie rozumiem tez, dlaczego nie widac icon

rockets = pygame.sprite.Group()
auto_pilot_rocket = pygame.image.load('images/autopilotrocket.png')
for i in range(2):
    delay = randint(30, 100)
    vector = Vector(randint(-10, 10), randint(-10, 10))
    rocket = AutoPilotRocket(randint(300, 700), randint(400, 600), auto_pilot_rocket, screen, delay, vector)
    rockets.add(rocket)

rocket_image = pygame.image.load('images/rocket.png')
player = Rocket(500, 700, rocket_image)
step = 10
players = pygame.sprite.Group()
players.add(player)

explosion = pygame.image.load('images/explosion.png')
rockets_to_remove = []
running = True
while running:
    for r in rockets_to_remove:
        r.kill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player.get_position()[1] - step > 0:
                player.update(Vector(0, -step))
            if event.key == pygame.K_DOWN and player.get_position()[1] + step < screen.get_height():
                player.update(Vector(0, step))
            if event.key == pygame.K_RIGHT and player.get_position()[0] + step < screen.get_width():
                player.update(Vector(step, 0))
            if event.key == pygame.K_LEFT and player.get_position()[0] - step > 0:
                player.update(Vector(-step, 0))
        for r in rockets:
            if player.get_distance(r) < 50:
                r.update(Vector(0, 0), explosion)
                rockets_to_remove.append(r)
    screen.fill((0, 0, 0))
    rockets.draw(screen)
    players.draw(screen)
    for r in rockets:
        r.update(r.vector)
    pygame.display.update()
