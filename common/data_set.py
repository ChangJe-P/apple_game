# 게임 데이터 파일
import pygame
import random

# 사과 이미지
apple_image = pygame.image.load("image/apple.jpg") # 사과 이미지 로드
apple_image = pygame.transform.scale(apple_image, (50, 50)) # 사과 이미지 크기 조정
# 바탕화면 사진 이미지
apple_tree_image = pygame.image.load("image/apple_tree2.jpg") # 사과 이미지 로드
apple_tree_image = pygame.transform.scale(apple_tree_image, (1280, 720)) # 사과 이미지 크기 조정

# 사과 이미지에 지정할 숫자 리스트 단, 숫자의 합이 10을 만들 수 있도록 비율에 맞게 설정
# 1의 개수보다 9의 개수가 적어야함.
# 5의 개수는 10을 만들 수 있는 조합이 많으므로 적절히 섞어야함.
apple_number = [[random.randint(1, 9) for _ in range(10)] for _ in range(17)]