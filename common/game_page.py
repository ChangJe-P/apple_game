import os
import pygame
import time
import random
from common.color import WHITE, BLACK, RED, GREEN, BLUE
from common.set_page import SCREEN_WIDTH, SCREEN_HEIGHT, screen
from common.data_set import apple_group, create_apples, dragging, start, end 

flag = 1
score = 0


pygame.font.init()
font = pygame.font.Font(None, 50)

def game_page(events, game_time):
    global dragging, start, end 
    global flag, score

    # 게임시작시 배경화면은 초록색으로 설정
    screen.fill(GREEN)
    
    # ★ 딱 한 번만 호출
    if flag == 1:
        create_apples()  
        flag = 0
        
    # ★ 사과는 apple_group에서 그리기만 함 (새로 생성 X)
    # game_page.py 수정
    for apple in apple_group:
        apple.draw_text(screen, font)  # draw → draw_text 로 변경

    # 이벤트 처리
    for event in events:
        #if event.type == pygame.QUIT:
        #    pygame.quit()
        #    return

        if event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
            start = event.pos
            end = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            end = event.pos

            # ★ 드래그 종료 시 판정
            drag_rect = pygame.Rect(
                min(start[0], end[0]),
                min(start[1], end[1]),
                abs(end[0] - start[0]),
                abs(end[1] - start[1])
            )

            selected = [a for a in apple_group if drag_rect.colliderect(a.rect)]
            total = sum(a.number for a in selected)

            if total == 10:
                score += len(selected)
                for apple in selected:
                    apple_group.remove(apple)  # ★ 합이 10이면 삭제

            # 드래그 초기화
            start = (0, 0)
            end = (0, 0)

        elif event.type == pygame.MOUSEMOTION and dragging:
            end = event.pos

    # 드래그 사각형 (방향 무관)
    if dragging:
        x = min(start[0], end[0])
        y = min(start[1], end[1])
        w = abs(end[0] - start[0])
        h = abs(end[1] - start[1])
        pygame.draw.rect(screen, RED, (x, y, w, h), 2)

        # ★ 드래그 중 선택된 사과 하이라이트
        drag_rect = pygame.Rect(x, y, w, h)
        for apple in apple_group:
            apple.selected = drag_rect.colliderect(apple.rect)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 제한시간 표시
    time_text = font.render(f"Time: {game_time:.1f}", True, WHITE)
    screen.blit(time_text, (10, 60))  # 글로 표기
    # 막대바로 남은 시간 표기 (위치는 사과 박스 위에 표시, 사이즈는 사과 박스 크기와 동일)
    # 제한시간은 150초(2분30초)
    finish = 150
    time_bar_width = (finish - game_time) / finish * 850
    pygame.draw.rect(screen, RED, (215, 90, time_bar_width, 20))
    

    pygame.display.update()
            
