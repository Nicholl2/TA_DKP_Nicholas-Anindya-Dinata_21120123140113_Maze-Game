import pygame
import sys
import random

class MazeGame:
    def __init__(self):
        pygame.init()
        self.RES = self.WIDTH, self.HEIGHT = 1200, 800
        self.TILE = 50
        self.COLS, self.ROWS = self.WIDTH // self.TILE, self.HEIGHT // self.TILE
        self.sc = pygame.display.set_mode(self.RES)
        pygame.display.set_caption("Maze Game")
        self.clock = pygame.time.Clock()
        self.RED = pygame.Color('red')
        self.BLACK = pygame.Color('black')
        self.WHITE = pygame.Color('white')
        self.ORANGE = pygame.Color('chocolate1')
        self.GREEN = pygame.Color('forestgreen')
        self.TURQUOISE = pygame.Color('paleturquoise')
        self.BLUE = pygame.Color('blue')
        self.CREAM = pygame.Color('bisque2')
        self.player_pos = [self.TILE, self.TILE]
        self.enemy_pos = [self.TILE * (self.COLS - 1), self.TILE]
        self.finish_pos = [self.TILE * (self.COLS - 2), self.TILE * (self.ROWS - 2)]
        self.outer_walls = [
            pygame.Rect(0, 0, self.WIDTH, self.TILE),
            pygame.Rect(0, self.HEIGHT - self.TILE, self.WIDTH, self.TILE),
            pygame.Rect(0, 0, self.TILE, self.HEIGHT),
            pygame.Rect(self.WIDTH - self.TILE, 0, self.TILE, self.HEIGHT)
        ]
        self.maze = [
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
        self.background_image = pygame.image.load("Assets/Awan1.jpeg")
        self.background_image = pygame.transform.scale(self.background_image, (self.WIDTH, self.HEIGHT))
        self.title_font = pygame.font.Font("Assets/Copyduck.ttf", 72)
        self.start_font = pygame.font.Font('Assets/04B_30__.TTF', 48)
        self.menu_font = pygame.font.Font('Assets/04B_30__.TTF', 48)
        self.player_image = pygame.image.load("Assets/Siput.png")
        self.player_image = pygame.transform.scale(self.player_image, (self.TILE, self.TILE))
        self.enemy_image = pygame.image.load("Assets/Kelelawar.png")
        self.enemy_image = pygame.transform.scale(self.enemy_image, (self.TILE, self.TILE))
        self.wall_image = pygame.image.load("Assets/Pohon.jpg")
        self.wall_image = pygame.transform.scale(self.wall_image, (self.TILE, self.TILE))

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        return textrect

    def main_menu(self):
        while True:
            self.sc.blit(self.background_image, (0, 0))
            self.draw_text('Maze Game', self.title_font, self.ORANGE, self.sc, 400, 100)
            start_rect = self.draw_text('START', self.start_font, self.GREEN, self.sc, 500, 250)
            keluar_rect = self.draw_text('KELUAR', self.menu_font, self.RED, self.sc, 480, 400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.game_loop()
                    elif event.key == pygame.K_2:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if start_rect.collidepoint((mouse_x, mouse_y)):
                        self.game_loop()
                    elif keluar_rect.collidepoint((mouse_x, mouse_y)):
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(30)

    def game_loop(self):
        self.player_pos = [self.TILE * 1, self.TILE * 1]
        self.enemy_pos = [self.TILE * (self.COLS - 1), self.TILE]
        enemy_move_counter = 0
        enemy_move_delay = 30

        while True:
            self.sc.fill(self.CREAM)
            self.draw_grid()

            for wall in self.outer_walls:
                pygame.draw.rect(self.sc, self.BLACK, wall)

            player_rect = pygame.Rect(self.player_pos[0], self.player_pos[1], self.TILE, self.TILE)
            enemy_rect = pygame.Rect(self.enemy_pos[0], self.enemy_pos[1], self.TILE, self.TILE)
            finish_rect = pygame.Rect(self.finish_pos[0], self.finish_pos[1], self.TILE, self.TILE)

            self.sc.blit(self.player_image, player_rect.topleft)
            self.sc.blit(self.enemy_image, enemy_rect.topleft)
            pygame.draw.rect(self.sc, self.ORANGE, finish_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    new_pos = self.move_player(event.key, self.player_pos)
                    new_player_rect = pygame.Rect(new_pos[0], new_pos[1], self.TILE, self.TILE)
                    if not self.is_collision(new_player_rect, self.outer_walls) and not self.is_collision(new_player_rect, self.maze):
                        self.player_pos = new_pos

            if enemy_move_counter == 0:
                enemy_new_pos = self.move_enemy(self.player_pos, self.enemy_pos)
                self.enemy_pos = enemy_new_pos
                enemy_move_counter = enemy_move_delay
            else:
                enemy_move_counter -= 10

            if player_rect.colliderect(finish_rect):
                self.draw_text('Kau Menang!', self.title_font, self.ORANGE, self.sc, 480, 400)
                pygame.display.flip()
                pygame.time.wait(2000)
                self.main_menu()

            if player_rect.colliderect(enemy_rect):
                self.draw_text('Kau Kalah!', self.title_font, self.RED, self.sc, 480, 400)
                pygame.display.flip()
                pygame.time.wait(2000)
                self.main_menu()

            pygame.display.flip()
            self.clock.tick(30)

    def draw_grid(self):
        for y in range(self.ROWS):
            for x in range(self.COLS):
                rect = pygame.Rect(x * self.TILE, y * self.TILE, self.TILE, self.TILE)
                if y < len(self.maze) and x < len(self.maze[y]) and self.maze[y][x] == 1:
                    self.sc.blit(self.wall_image, rect.topleft)
                pygame.draw.rect(self.sc, self.GREEN, rect, 1)

    def move_player(self, key, player_pos):
        x, y = player_pos
        if key == pygame.K_LEFT:
            x -= self.TILE
        elif key == pygame.K_RIGHT:
            x += self.TILE
        elif key == pygame.K_UP:
            y -= self.TILE
        elif key == pygame.K_DOWN:
            y += self.TILE
        return [x, y]

    def is_collision(self, rect, walls):
        if isinstance(walls, list) and isinstance(walls[0], list):
            for y in range(len(walls)):
                for x in range(len(walls[y])):
                    if walls[y][x] == 1:
                        maze_rect = pygame.Rect(x * self.TILE, y * self.TILE, self.TILE, self.TILE)
                        if rect.colliderect(maze_rect):
                            return True
        else:
            for wall in walls:
                if rect.colliderect(wall):
                    return True
        return False

    def move_enemy(self, player_pos, enemy_pos):
        enemy_x, enemy_y = enemy_pos
        possible_moves = []
        if enemy_x < player_pos[0]:
            possible_moves.append((enemy_x + self.TILE, enemy_y))
        elif enemy_x > player_pos[0]:
            possible_moves.append((enemy_x - self.TILE, enemy_y))
        if enemy_y < player_pos[1]:
            possible_moves.append((enemy_x, enemy_y + self.TILE))
        elif enemy_y > player_pos[1]:
            possible_moves.append((enemy_x, enemy_y - self.TILE))
        random.shuffle(possible_moves)
        for move in possible_moves:
            new_enemy_rect = pygame.Rect(move[0], move[1], self.TILE, self.TILE)
            if not self.is_collision(new_enemy_rect, self.outer_walls) and not self.is_collision(new_enemy_rect, self.maze):
                return move
        alternative_moves = [
            (enemy_x + self.TILE, enemy_y),
            (enemy_x - self.TILE, enemy_y),
            (enemy_x, enemy_y + self.TILE),
            (enemy_x, enemy_y - self.TILE)
        ]
        random.shuffle(alternative_moves)
        for move in alternative_moves:
            new_enemy_rect = pygame.Rect(move[0], move[1], self.TILE, self.TILE)
            if not self.is_collision(new_enemy_rect, self.outer_walls) and not self.is_collision(new_enemy_rect, self.maze):
                return move
        return enemy_pos

if __name__ == "__main__":
    game = MazeGame()
    game.main_menu()
