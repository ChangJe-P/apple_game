# 게임 데이터 파일
import os
import pygame
import random
from common.color import WHITE, BLACK, RED, GREEN, BLUE, YELLOW

pygame.font.init()
font = pygame.font.Font(None, 50) # 폰트 설정

# data_set.py 기준으로 상위 폴더(apple_game/)를 BASE_DIR로 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 사과 데이터 클래스로 만들기
class Apple(pygame.sprite.Sprite):
    image = None 
    def __init__(self, x, y, number):
        super().__init__()
        if Apple.image is None:
            # 사과 이미지
            Apple.image = pygame.image.load(os.path.join(BASE_DIR, "image", "apple.jpg")) # 사과 이미지 로드 
            Apple.image = pygame.transform.scale(Apple.image, (50, 50)) # 사과 이미지 크기 조정 
        self.number = number # 사과 숫자
        self.rect = self.image.get_rect(topleft=(x, y)) # x,y 위치에 이미지 생성
        self.selected = False # 드래그 선택 여부
    
    # 숫자 표시 메서드
    def draw_text(self, screen, font):
        screen.blit(Apple.image, self.rect)
        color = YELLOW if self.selected else WHITE
        text = font.render(str(self.number), True, color)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
        # 사과 이미지에 지정할 숫자 리스트 단, 숫자의 합이 10을 만들 수 있도록 비율에 맞게 설정
        # 1의 개수보다 9의 개수가 적어야함.
        # 5의 개수는 10을 만들 수 있는 조합이 많으므로 적절히 섞어야함.
        #self.apple_numbers = [[random.randint(1, 9) for _ in range(10)] for _ in range(17)]

# ★ 사과 그룹 - 게임 시작 시 딱 한 번만 생성
apple_group = pygame.sprite.Group()

def create_apples():
    for i in range(17):
        for j in range(10):
            number = random.randint(1, 9)
            x = i * 50 + 215
            y = j * 50 + 110
            apple = Apple(x, y, number)
            apple_group.add(apple)
            
        #print(i)
    #print("끝")

# 드래그 상태
dragging = False
start = (0, 0)
end = (0, 0)
#score = 0 