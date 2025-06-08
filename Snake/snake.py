import pygame # pip3 install pygame
import time
import random

# Initialize the pygame library
pygame.init()

# Set screen size
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Set title
pygame.display.set_caption('Snake Game')

# Colors (RGB format)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake block size and speed
block_size = 20
snake_speed = 10

# Clock to control speed
clock = pygame.time.Clock()

# Font for score
font = pygame.font.SysFont(None, 35)

# Score display function
def show_score(score):
    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, [10, 10])

# Snake drawing function
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting position of snake
    x = width / 2
    y = height / 2

    # Movement direction
    x_change = 0
    y_change = 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Random food position
    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(black)
            msg = font.render("You lost! Press Q to Quit or R to Restart", True, red)
            screen.blit(msg, [width / 6, height / 3])
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        x += x_change
        y += y_change

        # If snake hits the wall
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(black)

        # Draw food
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        # Update snake's position
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # If snake hits itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        # Eat food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()