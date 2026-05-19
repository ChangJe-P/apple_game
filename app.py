import pygame
import random
import time
import os

from common.data_set import create_apples
from common.game_page import get_game_page
from common.start_page import start_page
from common.color import WHITE, BLACK, RED, GREEN, BLUE
from common.set_page import SCREEN_WIDTH, SCREEN_HEIGHT, screen, start_button

# 초기화
pygame.init()

# 화면 설정
pygame.display.set_caption("사과 게임")

# 게임 루프
running = True
game_state = "start"

# 게임 시간 설정
game_time = 0 # 현재 게임 시간 
start_time = 0 # 게임 시작 시간 
end_time = 0 # 게임 종료 시간 
finish = 120 # 2분 종료 시간

# 최종 점수 (return 값으로 받음)
score = 0

# 게임 시작 시 사과 생성 플래그 
flag = 1

while running:
    events = pygame.event.get()     # 
    for event in events: # 이벤트 처리
        if event.type == pygame.QUIT: # x 버튼을 누르면 게임 종료
            running = False # running을 False로 변경하여 게임 종료
    
    # 화면 채우기
    # game_stae = "game" 이면 게임 바탕 화면 띄우기 
    # 게임 화면과 게임 바탕화면 구분 
    if game_state == "start": 
        start_page(score)
    
    # 게임 시작 버튼 클릭시 game_state를 game으로 변경 
    if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 클릭 이벤트가 발생하면 
        if start_button.collidepoint(event.pos):    # 마우스 클릭이 버튼 안에 있으면 
            game_state = "game" # 게임 화면으로 전환 
            start_time = time.perf_counter() 

    # game_state == "game" 이면 게임 화면 띄우기
    if game_state == "game":
        if finish <= game_time:  # 게임 시작 후 game_time이 finish과 같아지면 종료 
            game_state = "start" # -> 현재 게임이 종료 되어야됨. 
            flag = 1     # 게임 시작 시 사과 생성하기 위한 플래그 
            # 게임 시간 초기화 # 
            start_time = 0
            end_time = 0
            game_time = 0
            
        else:
            end_time = time.perf_counter()
            game_time = end_time - start_time  
            score = get_game_page(events, game_time, flag, finish)   # event 처리 중복을 제거하기 위해 game_page()에서 처리하도록 전달
            flag = 0
    
    # 화면 업데이트
    # pygame.display.flip() # 화면 업데이트

# 게임 종료
pygame.quit() 