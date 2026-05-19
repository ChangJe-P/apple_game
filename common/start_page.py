import pygame
import random
import time
from common.color import WHITE, BLACK, RED, GREEN, BLUE
from common.set_page import SCREEN_WIDTH, SCREEN_HEIGHT, screen, start_button, tree_image

# 이미지의 Rect 정보를 가져오면서 중앙(center) 좌표를 화면 중앙으로 설정
image_rect = tree_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# 배경 화면
def start_page():
    # 흰색 바탕에 사과 나무 띄우기
    screen.blit(tree_image, image_rect) # 사과 이미지 표시     ----> 여기서 부터 시작하자 클래스 활용
    # 게임 시작 버튼 누르면 게임 화면으로 이동
    pygame.draw.rect(screen, RED, start_button) # 게임 시작 버튼 그리기 
    # 게임 시작 버튼에 텍스트 표시
    font = pygame.font.Font(None, 50) # 폰트 설정
    text = font.render("START", True, WHITE) # 텍스트 생성
    text_rect = text.get_rect(center=start_button.center) # 텍스트 위치 설정
    screen.blit(text, text_rect) # 텍스트 표시
    
    pygame.display.update()