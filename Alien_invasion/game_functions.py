import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''键盘按下'''
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    '''如果没有达到限制，就发射一颗子弹'''
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    '''键盘松开'''
    if event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_a:
        ship.moving_left = False

def check_events(ai_settings,screen,stats,play_button,ship,bullets):
    '''响应按键和鼠标事件'''

    # 终止程序
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 控制飞船移动
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y)

def check_play_button(stats,play_button,mouse_x,mouse_y):
    '''在玩家单击PLAY时开始新游戏'''
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.game_active = True

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    '''更新子弹的位置，删除消失的子弹'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)


def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    '''响应子弹和外星人碰撞'''
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        # 删除现有子弹并创建一群新的外星人
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)

def update_screen(ai_settings,screen,stats,ship,alien,bullets,
                  play_button):
    '''更新屏幕上的图像'''

    # 如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()

    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.draw(screen)

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def get_number_aliens_x(ai_settings,alien_width):
    '''计算没一行能够容纳多少个外星人'''
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可以容纳多少行外星人'''
    available_space_y = (ai_settings.screen_height - 
                         (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个外星人并将其放在当前行'''
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)
        
def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人群'''
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,
                                  ship.rect.height,alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,
                         alien_number,row_number)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘时及时采取响应的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将外星人下移，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left > 0:
        # 将ships_lest减1
        stats.ships_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放在屏幕底部中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''检查是否有外星人到达了屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞一样处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    '''更新外星人群中所有外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
        print("Ship hit!!")
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

