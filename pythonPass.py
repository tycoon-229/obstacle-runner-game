import pygame
import random

# =========================
# KHỞI TẠO
# =========================
pygame.init()

# Màn hình
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Obstacle Runner")

# FPS
clock = pygame.time.Clock()

# =========================
# MÀU SẮC
# =========================
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

# =========================
# LOAD ẢNH
# =========================
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 600))

player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (70, 90))

obstacle_img = pygame.image.load("obstacle.png")
obstacle_img = pygame.transform.scale(obstacle_img, (70, 90))

# =========================
# FONT
# =========================
big_font = pygame.font.SysFont(None, 72)
medium_font = pygame.font.SysFont(None, 42)
small_font = pygame.font.SysFont(None, 32)

# =========================
# TỐC ĐỘ GAME
# =========================
obs_speed = 5

# =========================
# MENU CHÍNH
# =========================
def main_menu():

    menu = True

    while menu:

        screen.blit(background, (0, 0))

        title = big_font.render("OBSTACLE RUNNER", True, yellow)
        start_text = medium_font.render("Press SPACE to Start", True, white)
        quit_text = small_font.render("Press Q to Quit", True, white)

        screen.blit(title, (150, 180))
        screen.blit(start_text, (220, 300))
        screen.blit(quit_text, (300, 360))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    menu = False
                    difficulty_menu()

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# =========================
# MENU ĐỘ KHÓ
# =========================
def difficulty_menu():

    global obs_speed

    choosing = True

    while choosing:

        screen.blit(background, (0, 0))

        title = big_font.render("Choose Difficulty", True, yellow)

        easy = medium_font.render("1 - Easy", True, white)
        medium = medium_font.render("2 - Medium", True, white)
        hard = medium_font.render("3 - Hard", True, white)

        screen.blit(title, (170, 150))
        screen.blit(easy, (320, 260))
        screen.blit(medium, (290, 320))
        screen.blit(hard, (320, 380))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    obs_speed = 5
                    choosing = False
                    game_loop()

                elif event.key == pygame.K_2:
                    obs_speed = 8
                    choosing = False
                    game_loop()

                elif event.key == pygame.K_3:
                    obs_speed = 11
                    choosing = False
                    game_loop()

# =========================
# PAUSE GAME
# =========================
def pause_game():

    paused = True

    while paused:

        screen.blit(background, (0, 0))

        pause_text = big_font.render("PAUSED", True, red)
        continue_text = small_font.render("Press P to Continue", True, white)

        screen.blit(pause_text, (270, 220))
        screen.blit(continue_text, (260, 320))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    paused = False

        clock.tick(15)

# =========================
# GAME OVER
# =========================
def game_over(score):

    waiting = True

    while waiting:

        screen.blit(background, (0, 0))

        over_text = big_font.render("GAME OVER", True, red)
        score_text = medium_font.render(f"Score: {score}", True, white)

        restart_text = small_font.render(
            "Press R to Restart",
            True,
            white
        )

        menu_text = small_font.render(
            "Press M for Menu",
            True,
            white
        )

        quit_text = small_font.render(
            "Press Q to Quit",
            True,
            white
        )

        screen.blit(over_text, (220, 180))
        screen.blit(score_text, (320, 270))

        screen.blit(restart_text, (280, 340))
        screen.blit(menu_text, (285, 390))
        screen.blit(quit_text, (300, 440))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    game_loop()

                elif event.key == pygame.K_m:
                    main_menu()

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# =========================
# GAME LOOP
# =========================
def game_loop():

    player_x = 370
    player_y = 480

    player_speed = 0
    move_speed = 7

    player_width = 70
    player_height = 90

    obstacles = []

    score = 0

    # Tạo obstacle
    for i in range(5):

        obs_x = random.randint(0, screen_width - 70)
        obs_y = random.randint(-700, -100)

        obstacles.append([obs_x, obs_y])

    game_exit = False

    current_speed = obs_speed

    while not game_exit:

        # =========================
        # EVENT
        # =========================
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    player_speed = -move_speed

                elif event.key == pygame.K_RIGHT:
                    player_speed = move_speed

                elif event.key == pygame.K_p:
                    pause_game()

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_speed = 0

        # =========================
        # PLAYER SPEED
        # =========================
        player_x += player_speed

        if player_x < 0:
            player_x = 0

        if player_x > screen_width - player_width:
            player_x = screen_width - player_width

        # =========================
        # DRAW BACKGROUND
        # =========================
        screen.blit(background, (0, 0))

        # =========================
        # OBSTACLES
        # =========================
        for obs in obstacles:

            obs_x, obs_y = obs

            screen.blit(obstacle_img, (obs_x, obs_y))

            obs[1] += current_speed

            # Collision
            if (
                player_x < obs_x + 70
                and player_x + player_width > obs_x
                and player_y < obs_y + 90
                and player_y + player_height > obs_y
            ):

                game_exit = True

            # Reset obstacle
            if obs[1] > screen_height:

                obs[1] = random.randint(-500, -100)
                obs[0] = random.randint(0, screen_width - 70)

                score += 1

                # Tăng tốc độ
                if score % 5 == 0:
                    current_speed += 0.5

        # =========================
        # DRAW PLAYER
        # =========================
        screen.blit(player_img, (player_x, player_y))

        # =========================
        # HIỂN THỊ ĐIỂM
        # =========================
        score_text = medium_font.render(
            f"Score: {score}",
            True,
            white
        )

        speed_text = small_font.render(
            f"Speed: {round(current_speed, 1)}",
            True,
            white
        )

        screen.blit(score_text, (20, 20))
        screen.blit(speed_text, (20, 60))

        pygame.display.update()

        clock.tick(60)

    game_over(score)

# =========================
# START GAME
# =========================
main_menu()