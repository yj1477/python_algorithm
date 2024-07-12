import pygame
import sys
import random

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("躲避方块游戏")

PLAYER_SIZE = 40
player_pos = [WIDTH // 2, HEIGHT - PLAYER_SIZE - 10]

FALLING_BLOCK_SIZE = 30
FALLING_BLOCK_SPEED = 3
falling_blocks = []

CLOCK = pygame.time.Clock()
FPS = 100

score = 0
font = pygame.font.Font("msyh.ttf", 36)

def create_falling_block():
    x = random.randint(0, WIDTH - FALLING_BLOCK_SIZE)
    y = 0
    return [x, y]

def handle_events():
    global score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_pos[0] > 0:
                player_pos[0] -= 10
            if event.key == pygame.K_RIGHT and player_pos[0] < WIDTH - PLAYER_SIZE:
                player_pos[0] += 10
            if event.key == pygame.K_RETURN:
                return False
    return True

def update_game():
    global falling_blocks, score
    to_remove = []
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - PLAYER_SIZE:
        player_pos[0] += 10
    for block in falling_blocks:
        block[1] += FALLING_BLOCK_SPEED
        if block[1] > HEIGHT:
            to_remove.append(block)
            score += 1
    for block in to_remove:
        falling_blocks.remove(block)
    if len(falling_blocks) < 5 and random.random() < 0.1:
        falling_blocks.append(create_falling_block())

def draw_game():
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    for block in falling_blocks:
        pygame.draw.rect(screen, RED, (block[0], block[1], FALLING_BLOCK_SIZE, FALLING_BLOCK_SIZE))
    score_text = font.render("得分：" + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

def check_collision():
    for block in falling_blocks:
        if (player_pos[0] < block[0] + FALLING_BLOCK_SIZE and player_pos[0] + PLAYER_SIZE > block[0]) and (player_pos[1] < block[1] + FALLING_BLOCK_SIZE and player_pos[1] + PLAYER_SIZE > block[1]):
            return True
    return False

def main_game_loop():
    start_screen = True
    while start_screen:
        screen.fill(BLACK)
        font = pygame.font.Font("msyh.ttf", 36)  # 加载字体文件
        text = font.render("按回车键开始游戏", True, BLUE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        start_screen = handle_events()

    while True:
        handle_events()
        update_game()
        draw_game()
        if check_collision():
            break
        CLOCK.tick(FPS)

if __name__ == "__main__":
    main_game_loop()