import pygame

# Default values
SIZE = width, height = 740, 580
SPEED = [2, 2]
SPEED2 = [1, 1]
BLACK = 21, 239, 245


def adjust_fps(fps, SPEED):
    return [int(v * 60 / fps) for v in SPEED]


def game_loop(fps, screen, image, image2):
    position = image.get_rect()
    position2 = image2.get_rect()
    clock = pygame.time.Clock()
    while True:
        # check input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                exit()
        # update game state
        position = position.move(adjust_fps(fps, SPEED))
        if position.left < 0 or position.right > SIZE[0]:
            SPEED[0] = -SPEED[0]
        if position.top < 0 or position.bottom > SIZE[1]:
            SPEED[1] = -SPEED[1]

        position2 = position2.move(adjust_fps(fps, SPEED2))
        if position2.left < 0 or position2.right > SIZE[0]:
            SPEED2[0] = -SPEED2[0]
        if position2.top < 0 or position2.bottom > SIZE[1]:
            SPEED2[1] = -SPEED2[1]
        # draw game objects
        screen.fill(BLACK)
        screen.blit(image, position)
        screen.blit(image2, position2)
        pygame.display.flip()
        # wait for fps
        clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    image = pygame.image.load("joker.png")
    image2 = pygame.image.load("comida.png")
    picture = pygame.transform.scale(image2, (180, 120))
    game_loop(60, screen, image, picture)
