# -*- coding: utf-8 -*-

import pygame
import random

display_w = 800
display_h = 600


pygame.init()
game_display = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption('Bibiki')
clock = pygame.time.Clock()

background = pygame.image.load('img/streat.png')

hp_icon = pygame.image.load('img/hp_icon.png')

fuel_icon = pygame.image.load('img/fuel_icon.png')

car = pygame.image.load('img/car.png')

car1 = pygame.image.load('img/car1.png')

car2 = pygame.image.load('img/car2.png')

my_font = pygame.font.Font("Pixel.ttf", 18)

my_font1 = pygame.font.Font("Pixel.ttf", 60)

my_font2 = pygame.font.Font("Pixel.ttf", 30)

my_font3 = pygame.font.Font("Pixel.ttf", 40)

start_ecran = pygame.image.load('img/title.png')

bullet_sprite = pygame.image.load('img/bullet.png')

back_black = pygame.image.load('img/back_ground.png')

bum = pygame.image.load('img/bum.png')

cub = pygame.image.load('img/cub.png')

write_start = pygame.image.load('img/start.png')

hard_sprite = pygame.image.load('img/hard.png')

medium_sprite = pygame.image.load('img/medium.png')

easy_sprite = pygame.image.load('img/easy.png')

small_sprite = pygame.image.load('img/smal.png')

large_sprite = pygame.image.load('img/large.png')

class OtherCar1:
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red2.png')
        self.x = 0
        self.y = -100
        self.speed = 4
        self.alive = True

class OtherCar2:
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red1.png')
        self.x = 1
        self.y = -100
        self.speed = -4    
        self.alive = True  

class OtherCar3:
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red4.png')
        self.x = 0
        self.y = -100
        self.speed = 5
        self.alive = True
        
class OtherCar4:
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red3.png')
        self.x = 1
        self.y = -100
        self.speed = -5
        self.alive = True
        
class bullet:
    def __init__(self):
        self.sprite = pygame.image.load('img/bullet.png')
        self.x = 0
        self.y = 350
        self.speed = 7
        self.alive = False
        
other_cars = [OtherCar1(), OtherCar2(), OtherCar1(), OtherCar3(), OtherCar4(), OtherCar3()]
bullets = [bullet()]

game_exit = False
background_h = 2356
bullet_counter = 10
background_y = display_h - background_h
other_car_max_y = 800
bullet_max_y = 0
chose_car = False
world_speed = 7
accelerate = 0
chosed_car = 0
car_y = (display_h * 0.6)
hp = 10
score = 0
small = False
medium1 = True
large = False
distance = 0
rand_max_red = 200
rand_max_blue = 300
hard = False
medium = True 
easy = False
car_x = 0
i = 0
distance_max = 50000 
fuel = 100
menu_win = False
menu_lose = False
menu_cheat = False
a = 0
cub_x = 370
cub_y = 420
start = False
cheat = 0
cheat1 = 0
cheat2 = 0
end_win = False
end_lose = False
end_cheat = False

   
def fuel1():
    global fuel, a
    if fuel <= 0 :
        fuel = 0    
    a += 1
    if a == 20:
        if accelerate <= 5:
            a = 0
            fuel -= 1
        if accelerate >= 5:
            a = 0
            fuel -= 2 
def draw_progress(x, y, width, value, max_value):
    pygame.draw.rect(game_display, (255, 255, 255), (x, y, width, 15))
    pygame.draw.rect(game_display, (150, 150, 200), (x, y, width * value / max_value, 15))  

def draw_ui():
    global fuel
    text_image = my_font.render(str(score), True, (255, 255, 255))
    game_display.blit(text_image, (720, 20))
    text_image = my_font.render(str(distance), True, (255, 255, 255))
    game_display.blit(text_image, (720, 40))    

    draw_progress(60, 32, 220, hp , 10 )
    draw_progress(60, 90, 220, fuel , 100 )
    draw_progress(10, 550, 750, distance , distance_max )
def lose():
    global hp,game_exit, start,fuel,world_speed ,accelerate ,distance ,score,hp,car_x, car_y, i,a , other_car,menu_lose,end_lose
    if hp == 0:
        fuel = 100
        world_speed = 7
        accelerate = 0
        car_x = 0
        i = 0
        a = 0
        car_y = (display_h * 0.6)        
        hp = 10
        score = 0
        distance = 0 
        other_cars[1].y = -100
        other_cars[2].y = -100
        other_cars[1].x = 0
        menu_lose = True
        end_lose = True
        other_cars[2].x = 1        
        start = False
        print('game over')

def path_length():
    difficult_level = my_font2.render('path length', True, (255, 255, 255))  
    game_display.blit(difficult_level,(30,50))   
    if large == False:
        game_display.blit(large_sprite,(30,100))
    if medium1 == False:
        game_display.blit(medium_sprite,(30,150))
    if small == False:
        game_display.blit(small_sprite,(30,200))    
    
def menu_win_or_lose():
    global menu_win, menu_lose
    if menu_win == True:
        win_write = my_font1.render('win', True, (255, 80, 0))
        game_display.blit(win_write, (200, 100))  
    if menu_lose == True:
        win_write = my_font1.render('game over', True, (255, 80, 0))
        game_display.blit(win_write, (200, 100))  
    if menu_cheat == True:
        win_write = my_font1.render('chiter', True, (255, 80, 0))
        game_display.blit(win_write, (200, 100)) 
        
def chosing_car():
    game_display.blit(background,(0,0))
    game_display.blit(write_start,(350,500))
    game_display.blit(car,(220,300))
    game_display.blit(car1,(370,300))
    game_display.blit(car2,(520,300))
    chose_one_car = my_font1.render('chose one car', True, (255, 255, 255))
    game_display.blit(chose_one_car, (170, 100))
    game_display.blit(cub, (cub_x, cub_y))
        
                
                    
def proces_menu_key(event):
    global start, game_exit,menu_win,menu_lose, menu_cheat, chose_car,cub_x
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            chose_car = True
            start = True
            menu_win = False
            menu_lose = False
            menu_cheat = False
        if event.key == pygame.K_2:
            game_exit = True  

def difficult():
    difficult_level = my_font2.render('difficult', True, (255, 255, 255))  
    game_display.blit(difficult_level,(600,50))
    if hard == False:
        game_display.blit(hard_sprite,(620,100))
    if medium == False:
        game_display.blit(medium_sprite,(620,150))
    if easy == False:
        game_display.blit(easy_sprite,(620,200))
        
def process_mouse(event):
    global chosed_car, chose_car, hard, medium, easy
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if hard_sprite.get_rect().move(620, 100).collidepoint(pos):
            hard = True
            medium = False
            easy = False
            print ('hard')
        if medium_sprite.get_rect().move(620, 160).collidepoint(pos):
            hard = False
            medium = True
            easy = False     
        if easy_sprite.get_rect().move(620, 220).collidepoint(pos):
            hard = False
            medium = False
            easy = True         
        if write_start.get_rect().move(350, 500).collidepoint(pos):
            if cub_x == 220:
                chosed_car = 0
                chose_car = False
            if cub_x == 370:
                chosed_car = 1 
                chose_car = False
            if cub_x == 520:
                chosed_car = 2  
                chose_car = False       
def menu_process_mouse(event):
    global hard, medium, easy,rand_max_red,rand_max_blue,distance_max, large, small, medium1
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if hard_sprite.get_rect().move(620, 100).collidepoint(pos):
            hard = True
            medium = False
            easy = False
            rand_max_red = 100
            rand_max_blue = 200            
        if medium_sprite.get_rect().move(620, 150).collidepoint(pos):
            hard = False
            medium = True
            easy = False   
            rand_max_red = 200
            rand_max_blue = 300             
        if easy_sprite.get_rect().move(620, 200).collidepoint(pos):
            hard = False
            medium = False
            easy = True  
            rand_max_red = 300
            rand_max_blue = 400 
        if large_sprite.get_rect().move(30, 100).collidepoint(pos):
            large = True
            medium1 = False
            small = False
            distance_max = 100000  
        if medium_sprite.get_rect().move(30, 150).collidepoint(pos):
            large = False
            medium1 = True
            small = False
            distance_max = 50000  
        if small_sprite.get_rect().move(30, 200).collidepoint(pos):
            large = False
            medium1 = False
            small = True
            distance_max = 25000          
    
def draw_other_cars():
    global other_cars, score
    for idx in range(len(other_cars)):
        game_display.blit(other_cars[idx].sprite, (335 + other_cars[idx].x * 75, other_cars[idx].y))
        other_cars[idx].y += world_speed + accelerate + other_cars[idx].speed
        
        if other_cars[idx].y > other_car_max_y:

            other_cars[idx].y = other_car_max_y + 1

            if(other_cars[idx].alive):
                score += 100
                other_cars[idx].alive = False
            if random.randint(0,rand_max_red) == 0:
                if random.randint(0,1) == 0:
                    other_cars[idx] = OtherCar2()
                if random.randint(0,1) == 1:  
                    other_cars[idx] = OtherCar1()
            if random.randint(0,rand_max_blue) == 0:
                if random.randint(0,1) == 0:  
                    other_cars[idx] = OtherCar4() 
                if random.randint(0,1) == 1:  
                    other_cars[idx] = OtherCar3()                 
   
def regen():
    global hp,i
    i += 1
    if hp< 10:
        if hp > 5:
            if i > 430:
                i = 0
            if i >= 400:
                hp += 1
                i = 0
    if hp< 10:
            if hp < 4:
                if i >= 200:
                    hp += 1
                    i = 0

def draw_background():
    global background_y

    game_display.blit(background, (0, background_y))
    game_display.blit(background, (0, background_y - background_h))
    background_y += world_speed + accelerate

    if background_y >= display_h:
        background_y = display_h - background_h 

def draw_car():
    global distance,game_exit, start,fuel,world_speed ,accelerate ,distance ,score,hp,car_x, car_y, i,a , other_car,menu_win,end_win
    if chosed_car == 0:
        game_display.blit(car, (335 + car_x * 75, car_y))
    if chosed_car == 1:
        game_display.blit(car1, (335 + car_x * 75, car_y))
    if chosed_car == 2:
        game_display.blit(car2, (335 + car_x * 75, car_y))    
    distance += world_speed + accelerate
    if distance >= distance_max :
        start = False
        fuel = 100
        world_speed = 7
        accelerate = 0
        car_x = 0
        i = 0
        a = 0
        car_y = (display_h * 0.6)        
        hp = 10
        score = 0
        distance = 0 
        end_win = True
        menu_win = True
        other_cars[1].y = -100
        other_cars[2].y = -100
        other_cars[1].x = 0
        other_cars[2].x = 1            
        print('win')

def draw_bullet():
    global bullets
    bullets[0].x = car_x
    bullet_count = my_font2.render(str(bullet_counter), True, (255, 255, 255))
    if bullet_counter < 0:
        bullet_counter == 0
    game_display.blit(bullet_count, (50, 140))    
    game_display.blit(bullet_sprite, (3, 100))
    if bullets[0].alive:
        for idx in range(len(bullets)):
            game_display.blit(bullets[idx].sprite, (335 + bullets[idx].x * 75, bullets[idx].y))
            bullets[idx].y -= world_speed + bullets[idx].speed

            if bullets[idx].y < bullet_max_y:
                if bullets[idx].alive:
                    bullets[idx].alive = False
                    
def collision():
    global score, hp, bullets,bullet_max_y
    car_rect = car.get_rect()
    car_rect = car_rect.move((335 + car_x * 75, car_y))
    bullet_rect = bullets[0].sprite.get_rect()
    bullet_rect = bullet_rect.move((335 + bullets[0].x * 75, bullets[0].y))
    show_picture = False 
    for idx in range(len(other_cars)):
        other_rect = other_cars[idx].sprite.get_rect()
        other_rect = other_rect.move((335 + other_cars[idx].x * 75, other_cars[idx].y))
        if other_cars[idx].y <= other_car_max_y:
            if car_rect.colliderect(other_rect):
                other_cars[idx].y = other_car_max_y + 1
                hp -= 1
                score -= 200
                if score < 0:
                    score = 0
                other_cars[idx].alive = False
                show_picture = True
                if show_picture == True:
                    game_display.blit(bum,(335 + other_cars[idx].x * 75 - 20,car_y - 100))
                    i = 0
                    i += 1
                    if i ==30:
                        show_picture = False
                        i = 0

    for idx in range(len(other_cars)):
        if bullets[0].alive == True:
            other_rect = other_cars[idx].sprite.get_rect()
            other_rect = other_rect.move((335 + other_cars[idx].x * 75, other_cars[idx].y))
            if other_cars[idx].y <= other_car_max_y:
                if bullet_rect.colliderect(other_rect):
                    other_cars[idx].y = other_car_max_y + 1
                    other_cars[idx].alive = False
                    show_picture = True
                    if show_picture == True:
                        game_display.blit(bum,(335 + other_cars[idx].x * 75 - 20,bullets[0].y - 100))
                        ir = 0
                        ir += 1
                        if ir ==30:
                            show_picture = False   
                            ir = 0                    
                    bullets[0].y = bullet_max_y - 1
                    bullets[0].alive = False 
                
def endings():
    win_write = my_font3.render('endings', True, (0, 0, 255))
    game_display.blit(win_write, (570, 350))
    if end_win :
        win_write = my_font2.render('winer', True, (0, 255, 0))
        game_display.blit(win_write, (600, 400))      
    if end_lose :
        win_write = my_font2.render('game over', True, (255, 45, 0))
        game_display.blit(win_write, (600, 450))  
    if end_cheat :
        win_write = my_font2.render('chiter', True, (255, 0, 0))
        game_display.blit(win_write, (600, 500))     
def process_keyboard(event):
    global car_x, accelerate,start,fuel,world_speed ,accelerate ,distance ,score,hp,car_x, car_y, i,a , other_cars,menu_cheat,cheat,cheat1,cheat2,end_cheat,bullets,bullet_counter,cub_x
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            car_x = 0
        if event.key == pygame.K_d:
            car_x = 1
        if event.key == pygame.K_RIGHT:
            if cub_x == 370:
                cub_x = 520
            if cub_x == 220:
                cub_x = 370 
    
        if event.key == pygame.K_LEFT:
            if cub_x == 370:
                cub_x = 220
            if cub_x == 520:
                cub_x = 370            
        if event.key == pygame.K_w:
            accelerate += 2
            if accelerate > 10:
                accelerate = 10
        if event.key == pygame.K_ESCAPE:
            start = False
        if event.key == pygame.K_s:
            accelerate -= 2
            if accelerate < -6:
                accelerate = -6
        if event.key == pygame.K_SPACE:
            accelerate = -6 
        if event.key == pygame.K_e:
            if bullet_counter > 0:
                if bullets[0].alive == False:
                    bullets[0].alive = True
                    bullets[0].y = 350
                    bullet_counter -= 1
        if event.key == pygame.K_w:
            cheat = 1
        if event.key == pygame.K_i:
            if cheat == 1:
                cheat1 = 1
        if event.key == pygame.K_n:
            if cheat1 == 1:
                cheat2 = 1
                start = False
                fuel = 100
                world_speed = 7
                accelerate = 0
                car_x = 0
                i = 0
                a = 0
                end_cheat = True
                menu_cheat = True
                car_y = (display_h * 0.6)        
                hp = 10
                other_cars[1].y = -100
                other_cars[2].y = -100
                other_cars[1].x = 0
                other_cars[2].x = 1          
                score = 0
                distance = 0    
                cheat = 0
                cheat1 = 0
                cheat2 = 0

def game_loop(update_time):
    global game_exit,hp_icon
    while not game_exit:
        for event in pygame.event.get():
            if start == True:
                process_keyboard(event)
                process_mouse(event)
            if start == False:
                menu_process_mouse(event)
                proces_menu_key(event)
                
            if event.type == pygame.QUIT:
                game_exit = True
        if start == True: 
            if chose_car :
                chosing_car()            
            if chose_car == False:             
                regen()
                lose()
                draw_background()
                draw_car()
                draw_other_cars()
                collision()
                draw_ui()
                fuel1()
                draw_bullet()
                game_display.blit(hp_icon,(10,20))
                game_display.blit(fuel_icon,(10,80))              
        if start == False:
            game_display.blit(start_ecran,(0,0))
            menu_win_or_lose()
            endings()
            difficult()
            path_length()

        pygame.display.update()
        clock.tick(update_time)

game_loop(30)
pygame.quit()