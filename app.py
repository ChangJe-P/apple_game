import pygame
import random
import time
import os
from common.data_set import create_apples
from common.game_page import game_page

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
finish = 150 # 2분 30초 종료 시간

# 점수 설정
#score = 0

while running:
    events = pygame.event.get()     # 
    for event in events: # 이벤트 처리
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
            start_time = time.perf_counter()

    # game_state == "game" 이면 게임 화면 띄우기
    if game_state == "game":
        if finish <= game_time:  # 게임 시작 후 현재 시간이 end_time과 같이지면 종료 
            game_state = "start" # -> 현재 게임이 종료 되어야됨.
        end_time = time.perf_counter()
        game_time = end_time - start_time  
        print(game_time)
        game_page(events, game_time)   # event 처리 중복을 제거하기 위해 game_page()에서 처리하도록 전달
        
    
    # 화면 업데이트
    #pygame.display.flip() # 화면 업데이트

# 게임 종료
pygame.quit() 