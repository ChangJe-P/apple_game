import pygame
import random
import time

from common.start_page import start_page
from common.game_page import game_page
from common.color import WHITE, BLACK, RED, GREEN, BLUE
from common.set_page import SCREEN_WIDTH, SCREEN_HEIGHT, screen, start_button
from common.data_set import apple_image, apple_tree_image, apple_number

# 초기화
pygame.init()

# 화면 설정
pygame.display.set_caption("사과 게임")

# 게임 루프
running = True
game_state = "start"

# 게임 시간 설정
game_time = 150 # 2분 30초

# 점수 설정
score = 0


while running:
    for event in pygame.event.get(): # 이벤트 처리
        if event.type == pygame.QUIT: # x 버튼을 누르면 게임 종료
            running = False # running을 False로 변경하여 게임 종료
    
    # 화면 채우기
    # game_stae = "game" 이면 게임 바탕 화면 띄우기
    # 게임 화면과 게임 바탕화면 구분
    if game_state == "start":
        start_page()
    
    # 게임 시작 버튼 클릭시 game_state를 game으로 변경 
    if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 클릭 이벤트가 발생하면
        if start_button.collidepoint(event.pos):    # 마우스 클릭이 버튼 안에 있으면
            game_state = "game" # 게임 화면으로 전환

    # game_state == "game" 이면 게임 화면 띄우기
    if game_state == "game":
        game_page()

    # 드래그 이벤트: 사과 이미지를 드래그하면 사과가 선택되고, 선택된 사과의 합이 10이 되면 사과가 사라짐. (드래그한 사과 이미지 테두리 색깔 변경)
    # 드래그한 선택된 사과의 합이 10이 되지 않으면 사과가 사라지지 않음.   
    
    # 화면 업데이트
    pygame.display.flip() # 화면 업데이트

# 게임 종료
pygame.quit() 