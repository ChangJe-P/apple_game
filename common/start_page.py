import pygame
import random
import time
from common.color import WHITE, BLACK, RED, GREEN, BLUE
from common.set_page import SCREEN_WIDTH, SCREEN_HEIGHT, screen, start_button
from common.data_set import apple_tree_image

# 배경 화면
def start_page():
    screen.fill(WHITE) # 화면을 흰색으로 채우기
    # 흰색 바탕에 사과 5개 띄우기
    screen.blit(apple_tree_image, (0, 0)) # 사과 이미지 표시
    # 게임 시작 버튼 누르면 게임 화면으로 이동
    pygame.draw.rect(screen, RED, start_button) # 게임 시작 버튼 그리기 
    # 게임 시작 버튼에 텍스트 표시
    font = pygame.font.Font(None, 50) # 폰트 설정
    text = font.render("START", True, WHITE) # 텍스트 생성
    text_rect = text.get_rect(center=start_button.center) # 텍스트 위치 설정
    screen.blit(text, text_rect) # 텍스트 표시
    