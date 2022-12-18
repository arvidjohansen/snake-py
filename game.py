import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Set the window title
pygame.display.set_caption('Snake')

# Set the window background color
bg_color = (0, 0, 0)

# Set the snake color
snake_color = (255, 255, 255)

# Set the snake size
snake_size = 10

# Set the initial snake position
snake_pos = [100, 50]

# Set the initial snake body
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the initial direction
direction = 'RIGHT'
change_to = direction

# Set the food color
food_color = (255, 0, 0)

# Set the food size
food_size = 10

# Set the initial food position
food_pos = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
food_spawn = True

# Set the game speed
speed = pygame.time.Clock()

# Set the score
score = 0

# Set the font
font = pygame.font.SysFont('times new roman', 15)

# Set the game over flag
game_over = False

# Set the window
window = pygame.display.set_mode(window_size)

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validate direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
    food_spawn = True

    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > window_size[0]-snake_size or snake_pos[1] < 0 or snake_pos[1] > window_size[1]-snake_size:
        game_over = True
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # Draw the window
    window.fill(bg_color)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(window, snake_color, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(window, food_color, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))

    # Draw the score
    score_text = font.render('Score: ' + str(score), True, snake_color)
    window.blit(score_text, (10, 10))

    # Refresh the window
    pygame.display.update()

    # Set the game speed
    speed.tick(10)

# Game over message
game_over_text = font.render('Game Over!', True, snake_color)
window.blit(game_over_text, (window_size[0] // 2 - game_over_text.get_width() // 2, window_size[1] // 2 - game_over_text.get_height() // 2))
pygame.display.update()

# Wait for a key press to close the window
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()