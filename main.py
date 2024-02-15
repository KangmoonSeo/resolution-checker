import sys
import pygame


BACKGROUND_COLOR = (255, 255, 255)  # 흰 배경
BLACK = (0, 0, 0)  # 검정색


def main():
    """
    십자모양 말을 이용한 HiDPI Checker
    """
    # 말의 초기 위치와 크기
    piece_x = 100
    piece_y = 100
    piece_size = 50

    # Pygame 초기화
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    # 이동 속도
    move_speed = 1

    # 폰트 설정
    font_large = pygame.font.Font(None, 36)
    font_small = pygame.font.Font(None, 24)

    # 게임 루프
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # 방향키 입력에 따라 말을 이동시킴
                if event.key == pygame.K_LEFT:
                    piece_x -= move_speed
                elif event.key == pygame.K_RIGHT:
                    piece_x += move_speed
                elif event.key == pygame.K_UP:
                    piece_y -= move_speed
                elif event.key == pygame.K_DOWN:
                    piece_y += move_speed
                elif event.key == pygame.K_q:  # q를 누르면 종료
                    running = False

        # 말 그리기 (십자모양)
        # 수직선
        pygame.draw.line(
            screen,
            BLACK,
            (piece_x, piece_y - piece_size),
            (piece_x, piece_y + piece_size),
            1,
        )
        # 수평선
        pygame.draw.line(
            screen,
            BLACK,
            (piece_x - piece_size, piece_y),
            (piece_x + piece_size, piece_y),
            1,
        )

        # Press Q to exit 문구 출력
        press_to_exit_text = "Press Q to exit"
        press_to_exit_surface = font_large.render(press_to_exit_text, True, BLACK)
        press_to_exit_rect = press_to_exit_surface.get_rect(
            center=(screen.get_width() // 2, 30)
        )
        screen.blit(press_to_exit_surface, press_to_exit_rect)

        # 현재 해상도 출력
        resolution_text = f"Resolution: {screen.get_width()}x{screen.get_height()}"
        resolution_surface = font_small.render(resolution_text, True, BLACK)
        screen.blit(
            resolution_surface,
            (screen.get_width() - resolution_surface.get_width() - 10, 10),
        )

        # 현재 말의 위치 출력
        position_text = f"Piece Position: ({piece_x}, {piece_y})"
        position_surface = font_small.render(position_text, True, BLACK)
        screen.blit(
            position_surface,
            (screen.get_width() - position_surface.get_width() - 10, 40),
        )

        # 화면 업데이트
        pygame.display.flip()
        clock.tick(60)

    # Pygame 종료
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
