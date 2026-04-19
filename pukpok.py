import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Пинг-понг")

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)

# Параметры ракеток
paddle_width = 15
paddle_height = 100
paddle_speed = 7

# Ракетка 1 (управление W, S)
paddle1_x = 50
paddle1_y = (screen_height - paddle_height) // 2
paddle1 = pygame.Rect(paddle1_x, paddle1_y, paddle_width, paddle_height)

# Ракетка 2 (управление стрелочками)
paddle2_x = screen_width - 50 - paddle_width
paddle2_y = (screen_height - paddle_height) // 2
paddle2 = pygame.Rect(paddle2_x, paddle2_y, paddle_width, paddle_height)

# Параметры мяча
ball_size = 15
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5
ball_speed_y = 5
ball = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

# Счет
score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)

# Игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение ракеток
    keys = pygame.key.get_pressed()

    # Ракетка 1 (W, S)
    if keys[pygame.K_w]:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s]:
        paddle1.y += paddle_speed

    # Ракетка 2 (стрелочки вверх/вниз)
    if keys[pygame.K_UP]:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2.y += paddle_speed

    # Ограничение движения ракеток границами экрана
    paddle1.y = max(0, min(paddle1.y, screen_height - paddle_height))
    paddle2.y = max(0, min(paddle2.y, screen_height - paddle_height))

    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Отскок мяча от верхнего и нижнего края экрана
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Отскок мяча от ракеток
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Если мяч выходит за левый или правый край экрана (гол)
    if ball.left <= 0:
        score2 += 1
        ball.x = screen_width // 2
        ball.y = screen_height // 2
        ball_speed_x *= -1  # Направление мяча в центр
        ball_speed_y *= -1  # Случайное начальное направление по Y

    if ball.right >= screen_width:
        score1 += 1
        ball.x = screen_width // 2
        ball.y = screen_height // 2
        ball_speed_x *= -1  # Направление мяча в центр
        ball_speed_y *= -1  # Случайное начальное направление по Y

    # Отрисовка
    screen.fill(black)  # Фон
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height)) # Разделительная линия

    # Отрисовка счета
    score_text1 = font.render(str(score1), True, white)
    score_text2 = font.render(str(score2), True, white)
    screen.blit(score_text1, (screen_width // 4, 10))
    screen.blit(score_text2, (screen_width * 3 // 4 - score_text2.get_width(), 10))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(60)

# Завершение Pygame
pygame.quit()
