'''
1.引入pygame和sys
2.初始化init（）以及设置
3.获取事件并响应
4.刷新屏幕
'''
# 1.引入pygame和sys
import pygame
import sys

# 2.初始化init（）以及设置
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('pygame')

# 3.获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
# 4.刷新屏幕
    pygame.display.update()