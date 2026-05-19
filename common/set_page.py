import pygame

# 화면 설정
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

###############
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 시작 버튼
start_button = pygame.Rect(540, 350, 200, 50)  # (x, y, width, height) 게임 시작 버튼 생성 


# 바탕화면 이미지#############
tree_image = pygame.image.load("image/apple_tree2.jpg") # 사과 이미지 로드
tree_image = pygame.transform.scale(tree_image, (SCREEN_WIDTH, SCREEN_HEIGHT)) # 사과 이미지 크기 조정