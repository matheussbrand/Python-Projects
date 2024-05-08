import pygame
import random
import sys

# Constantes para dimensões da janela e propriedades da cobra
WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 10
SNAKE_SPEED = 15

# Valores de cor RGB para vários elementos no jogo
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Inicializar o Pygame
pygame.init()

# Criar a janela de exibição do jogo
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")  # Titulo da janela

# Objeto relógio para controlar a taxa de quadros
clock = pygame.time.Clock()

# Fontes para exibir mensagens e pontuações
message_font = pygame.font.SysFont("ubuntu", 30)
score_font = pygame.font.SysFont("ubuntu", 30)


# Função para imprimir a pontuação na tela
def print_score(score, last_score):
    # Renderiza o texto da pontuação com a fonte e cor especificadas
    current_score_text = score_font.render("Score: " + str(score), True, ORANGE)
    last_score_text = score_font.render("Last Score: " + str(last_score), True, ORANGE)
    # Blit o texto da pontuação na superfície de exibição do jogo
    game_display.blit(current_score_text, [10, 10])
    game_display.blit(last_score_text, [10, 40])


# Função para desenhar a cobra na tela
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        # Desenhar cada segmento da cobra como um retângulo
        pygame.draw.rect(
            game_display, WHITE, [pixel[0], pixel[1], snake_size, snake_size]
        )


# Função para exibir a tela de fim de jogo
def game_over_screen(score, last_score):
    # Preencher a tela com a cor preta
    game_display.fill(BLACK)
    # Renderizar e exibir a mensagem de fim de jogo
    game_over_message = message_font.render(
        "Game Over! Press Enter.", True, RED
    )
    game_display.blit(game_over_message, [WIDTH / 6, HEIGHT / 3])
    # Print da pontuação na tela
    print_score(score, last_score)
    pygame.display.update()


# Função para executar o jogo
def run_game():
    # Inicializar variáveis para o estado do jogo
    last_score = 0
    snake_length = 1
    snake_speed = SNAKE_SPEED

    # Inicializar posição e velocidade da cobra
    x, y = WIDTH / 2, HEIGHT / 2
    x_speed, y_speed = 0, 0

    # Lista para armazenar os pixels da cobra
    snake_pixels = []

    # Gerar posição inicial do alvo para a cobra
    target_x, target_y = (
        random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10,
        random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10,
    )

    # Main loop do jogo
    while True:
        # Loop de manipulação de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -SNAKE_SIZE
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = SNAKE_SIZE
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -SNAKE_SIZE
                elif event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = SNAKE_SIZE

        # Verifique se a cobra atinge a parede ou a si mesma
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over_screen(snake_length - 1, last_score)
            last_score = max(last_score, snake_length - 1)
            snake_length = 1
            snake_speed = SNAKE_SPEED
            x, y = WIDTH / 2, HEIGHT / 2
            x_speed, y_speed = 0, 0
            snake_pixels = []
            target_x, target_y = (
                random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10,
                random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10,
            )

        # Atualiza a posição da cobra
        x += x_speed
        y += y_speed

        # Limpa a tela
        game_display.fill(BLACK)
        # Desenha o alvo
        pygame.draw.rect(
            game_display, ORANGE, [target_x, target_y, SNAKE_SIZE, SNAKE_SIZE]
        )

        # Adiciona a posição atual à lista de pixels da cobra
        snake_pixels.append([x, y])

        # Mantém o comprimento da cobra sob controle
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        # Verificador de colisão da cobra com o corpo
        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_over_screen(snake_length - 1, last_score)
                last_score = max(last_score, snake_length - 1)
                snake_length = 1
                snake_speed = SNAKE_SPEED
                x, y = WIDTH / 2, HEIGHT / 2
                x_speed, y_speed = 0, 0
                snake_pixels = []
                target_x, target_y = (
                    random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10,
                    random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10,
                )

        # Desenho da cobra
        draw_snake(SNAKE_SIZE, snake_pixels)
        # Print the score
        print_score(snake_length - 1, last_score)

        # Update de tela
        pygame.display.update()

        # Verificador de que a cobra acertou o alvo
        if x == target_x and y == target_y:
            # Alvo aleatório
            target_x, target_y = (
                random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10,
                random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10,
            )
            # Comprimento da cobra
            snake_length += 1
            # Aumento da valocidade a cada 5 pontos
            if snake_length % 5 == 0:
                snake_speed += 1

        # Frame rate
        clock.tick(snake_speed)


# Inicia o game
run_game()
