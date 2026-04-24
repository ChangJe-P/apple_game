import pygame
import random
import time
from common.color import WHITE, BLACK, RED, GREEN, BLUE
from common.set_page import SCREEN_WIDTH, SCREEN_HEIGHT, screen
from common.data_set import apple_image, apple_number

# 게임 화면
def game_page():
    # 바탕 화면에서 게임 화면으로 전환
    screen.fill(GREEN) # 화면을 흰색으로 채우기
    # 게임 화면에 사과 가로 (17) * 세로(10) 개 띄우고 화면 중앙에 위치하기
    # 사과 이미지 위에 1 ~ 9 까지 랜덤 숫자 표시, 숫자는 게임 진행 내 1회만 설정 (처음 숫자가 정해진 후 변경 x)
    for i in range(17):
        for j in range(10):
            screen.blit(apple_image, (i * 50 + 220, j * 50 + 90)) # (x, y) 사과 이미지 표시
            font = pygame.font.Font(None, 50) # 폰트 설정
            text = font.render(str(apple_number[i][j]), True, WHITE) # 텍스트 생성
            text_rect = text.get_rect(center=(i * 50 + 245, j * 50 + 115)) # 텍스트 위치 설정
            screen.blit(text, text_rect) # 텍스트 표시

