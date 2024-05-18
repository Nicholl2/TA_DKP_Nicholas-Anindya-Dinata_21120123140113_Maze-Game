import pygame
import sys
import random

pygame.init()

RES = WIDTH, HEIGHT = 1200, 800
TILE = 50
COLS, ROWS = WIDTH // TILE, HEIGHT // TILE

sc = pygame.display.set_mode(RES)
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

RED = pygame.Color('red')
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
ORANGE = pygame.Color('chocolate1')
GREEN = pygame.Color('forestgreen')
TURQUOISE = pygame.Color('paleturquoise')
BLUE = pygame.Color('blue')
CREAM = pygame.Color('bisque2')

player_pos = [TILE, TILE]
enemy_pos = [TILE * (COLS - 1), TILE]  
finish_pos = [TILE * (COLS - 2), TILE * (ROWS - 2)]  

outer_walls = [
    pygame.Rect(0, 0, WIDTH, TILE),  
    pygame.Rect(0, HEIGHT - TILE, WIDTH, TILE),  
    pygame.Rect(0, 0, TILE, HEIGHT),  
    pygame.Rect(WIDTH - TILE, 0, TILE, HEIGHT)
]

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]
]

background_image = pygame.image.load("Assets/Awan1.jpeg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
title_font = pygame.font.Font("Assets/Copyduck.ttf", 72)
start_font = pygame.font.Font('Assets/04B_30__.TTF', 48)
menu_font = pygame.font.Font('Assets/04B_30__.TTF', 48)
player_image = pygame.image.load("Assets/Siput.png")
player_image = pygame.transform.scale(player_image, (TILE, TILE))
enemy_image = pygame.image.load("Assets/Kelelawar.png")
enemy_image = pygame.transform.scale(enemy_image, (TILE, TILE))
wall_image = pygame.image.load("Assets/Pohon.jpg")
wall_image = pygame.transform.scale(wall_image, (TILE, TILE))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect

def main_menu():
    while True:
        sc.blit(background_image, (0, 0))
        draw_text('Maze Game', title_font, ORANGE, sc, 400, 100)
        start_rect = draw_text('START', start_font, GREEN, sc, 500, 250)
        keluar_rect = draw_text('KELUAR', menu_font, RED, sc, 480, 400)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_rect.collidepoint((mouse_x, mouse_y)):
                    game_loop()
                elif keluar_rect.collidepoint((mouse_x, mouse_y)):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(30)

def game_loop():
    global player_pos, enemy_pos
    player_pos = [TILE * 1, TILE * 1]
    enemy_pos = [TILE * (COLS - 1), TILE]  

    enemy_move_counter = 0
    enemy_move_delay = 30 

    while True:
        sc.fill(CREAM)
        draw_grid()

        for wall in outer_walls:
            pygame.draw.rect(sc, BLACK, wall)

        player_rect = pygame.Rect(player_pos[0], player_pos[1], TILE, TILE)
        enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], TILE, TILE)
        finish_rect = pygame.Rect(finish_pos[0], finish_pos[1], TILE, TILE)

        sc.blit(player_image, player_rect.topleft)
        sc.blit(enemy_image, enemy_rect.topleft)
        pygame.draw.rect(sc, ORANGE, finish_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                new_pos = move_player(event.key, player_pos)
                new_player_rect = pygame.Rect(new_pos[0], new_pos[1], TILE, TILE)
                if not is_collision(new_player_rect, outer_walls) and not is_collision(new_player_rect, maze):
                    player_pos = new_pos

        if enemy_move_counter == 0:
            enemy_new_pos = move_enemy(player_pos, enemy_pos)
            enemy_pos = enemy_new_pos
            enemy_move_counter = enemy_move_delay
        else:
            enemy_move_counter -= 10

        if player_rect.colliderect(finish_rect):
            draw_text('Kau Menang!', title_font, ORANGE, sc, 450, 400)
            pygame.display.flip()
            pygame.time.wait(2000)
            main_menu()

        if player_rect.colliderect(enemy_rect):
            draw_text('Kau Kalah!', title_font, RED, sc, 450, 400)
            pygame.display.flip()
            pygame.time.wait(2000)
            main_menu()

        pygame.display.flip()
        clock.tick(30)

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * TILE, y * TILE, TILE, TILE)
            if y < len(maze) and x < len(maze[y]) and maze[y][x] == 1:
                sc.blit(wall_image, rect.topleft)
            pygame.draw.rect(sc, GREEN, rect, 1)

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

def is_collision(rect, walls):
    if isinstance(walls, list) and isinstance(walls[0], list):  
        for y in range(len(walls)):
            for x in range(len(walls[y])):
                if walls[y][x] == 1:
                    maze_rect = pygame.Rect(x * TILE, y * TILE, TILE, TILE)
                    if rect.colliderect(maze_rect):
                        return True
    else:  
        for wall in walls:
            if rect.colliderect(wall):
                return True
    return False

def move_enemy(player_pos, enemy_pos):
    enemy_x, enemy_y = enemy_pos

    possible_moves = []
    if enemy_x < player_pos[0]:
        possible_moves.append((enemy_x + TILE, enemy_y)) 
    elif enemy_x > player_pos[0]:
        possible_moves.append((enemy_x - TILE, enemy_y))  

    if enemy_y < player_pos[1]:
        possible_moves.append((enemy_x, enemy_y + TILE))  
    elif enemy_y > player_pos[1]:
        possible_moves.append((enemy_x, enemy_y - TILE))  

    random.shuffle(possible_moves)

    for move in possible_moves:
        new_enemy_rect = pygame.Rect(move[0], move[1], TILE, TILE)
        if not is_collision(new_enemy_rect, outer_walls) and not is_collision(new_enemy_rect, maze):
            return move

    alternative_moves = [
        (enemy_x + TILE, enemy_y),
        (enemy_x - TILE, enemy_y),
        (enemy_x, enemy_y + TILE),
        (enemy_x, enemy_y - TILE)
    ]
    random.shuffle(alternative_moves)
    for move in alternative_moves:
        new_enemy_rect = pygame.Rect(move[0], move[1], TILE, TILE)
        if not is_collision(new_enemy_rect, outer_walls) and not is_collision(new_enemy_rect, maze):
            return move

    return enemy_pos

if __name__ == "__main__":
    main_menu()
