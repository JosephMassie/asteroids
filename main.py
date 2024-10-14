import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    drawables = pygame.sprite.Group()
    updateables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawables, updateables)
    Shot.containers = (shots, drawables, updateables)
    Asteroid.containers = (asteroids, drawables, updateables)
    AsteroidField.containers = (updateables)

    AsteroidField()
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateables:
            obj.update(dt)
        
        for ast in asteroids:
            for bullet in shots:
                hit = pygame.sprite.collide_circle(ast, bullet)
                if hit:
                    print(f"hit @ {bullet.position}")
                    ast.kill()
                    bullet.kill()

        screen.fill((20, 20, 20))
        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(MAX_FPS) / 1000

if __name__ == "__main__":
    main()