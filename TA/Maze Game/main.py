import pygame
import sys

pygame.init()

RES = WIDTH, HEIGHT = 1200, 900
TILE = 50
COLS, ROWS = WIDTH // TILE, HEIGHT // TILE

sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

RED = pygame.Color('red')
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

player_pos = [TILE // 2, TILE // 2]

walls = [
    pygame.Rect(TILE * 3, TILE * 3, TILE, TILE * 6),
    pygame.Rect(TILE * 7, TILE * 2, TILE * 2, TILE),
    pygame.Rect(TILE * 10, TILE * 4, TILE, TILE * 4)
]

background_image = pygame.image.load("Assets/Awan1.jpeg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

font = pygame.font.SysFont('Arial', 48)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        sc.blit(background_image, (0, 0))
        draw_text('MAZE GAME', font, RED, sc, 500, 100)
        draw_text('1. Mulai', font, BLACK, sc, 500, 250)
        draw_text('2. Keluar', font, BLACK, sc, 500, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop()
                elif event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(30)

def game_loop():
    while True:
        sc.fill(BLACK)
        draw_grid()

        for wall in walls:
            pygame.draw.rect(sc, WHITE, wall)

        player_rect = pygame.Rect(player_pos[0], player_pos[1], TILE, TILE)
        pygame.draw.rect(sc, RED, player_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                new_pos = move_player(event.key, player_pos)
                new_player_rect = pygame.Rect(new_pos[0], new_pos[1], TILE, TILE)
                if not is_collision(new_player_rect, walls):
                    player_pos = new_pos

        pygame.display.flip()
        clock.tick(30)

def draw_grid():
    for x in range(0, WIDTH, TILE):
        for y in range(0, HEIGHT, TILE):
            rect = pygame.Rect(x, y, TILE, TILE)
            pygame.draw.rect(sc, WHITE, rect, 1)

def move_player(key, player_pos):
    x, y = player_pos
    if key == pygame.K_LEFT:
        x -= TILE
    elif key == pygame.K_RIGHT:
        x += TILE
    elif key == pygame.K_UP:
        y -= TILE
    elif key == pygame.K_DOWN:
        y += TILE
    return [x, y]

def is_collision(player_rect, walls):
    for wall in walls:
        if player_rect.colliderect(wall):
            return True
    return False

if __name__ == "__main__":
    main_menu()
