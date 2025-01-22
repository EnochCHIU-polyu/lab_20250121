# filepath: /workspaces/lab_20250121/v.py

import pygame
import random
import math

# 初始化 pygame
pygame.init()

# 設置畫布大小和標題
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Interactive Digital Art")

# 定義顏色列表
colors = [(255, 0, 0), (255, 255, 0), (0, 0, 255), (0, 255, 0), (128, 0, 128), (255, 165, 0), (255, 255, 255)]

# 運行標誌
running = True

# 主循環
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 獲取鼠標位置
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 清除屏幕
    screen.fill((0, 0, 0))

    # 繪製數位藝術
    for i in range(360):
        angle = math.radians(i * 59)
        x = mouse_x + i * math.cos(angle)
        y = mouse_y + i * math.sin(angle)
        color = random.choice(colors)
        pygame.draw.circle(screen, color, (int(x), int(y)), 5)

    # 更新屏幕
    pygame.display.flip()

# 退出 pygame
pygame.quit()