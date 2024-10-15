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
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for obj in updateables:
            obj.update(dt)
        
        
        for ast in asteroids:
            if player.is_colliding(ast):
                player.kill()
                print("you died")
                running = False

            for bullet in shots:
                hit = ast.is_colliding(bullet)
                if hit:
                    print(f"hit @ {bullet.position}")
                    ast.kill()
                    bullet.kill()

        screen.fill((20, 20, 20))
        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(MAX_FPS) / 1000
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()