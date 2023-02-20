import pygame
import sys
import time
pygame.init()
pygame.font.init()
window_width = 800
window_height = 600
window_size = (window_width, window_height)

screen = pygame.display.set_mode(window_size)

rect_width=10
rect_length=50

rect_x=10
rect_y=275

rect_size_loc=(rect_x,rect_y,rect_width,rect_length)

rect2_x=780
rect2_y=275

rect2_color=(255,0,0)

rect2_size_loc=(rect2_x,rect2_y,rect_width,rect_length)

ball_width=10
ball_length=10

ball_x=400
ball_y=300

ball_color=(0,0,255)

ball_size_loc=(ball_x,ball_y,ball_width,ball_length)



velocity1=0
velocity2=0
ball_velocity_x=1
ball_velocity_y=0

rect_color=(255,0,0)
pygame.draw.rect(screen,rect2_color,rect2_size_loc)
pygame.draw.rect(screen,rect_color,rect_size_loc)
pygame.draw.rect(screen,ball_color,ball_size_loc)
clock = pygame.time.Clock()

score1=0
score2=0

font= pygame.font.SysFont('Arial',36)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                velocity1=-5
            if event.key==pygame.K_DOWN:
                velocity1=5
            if event.key==pygame.K_w:
                velocity2 =-5
            if event.key==pygame.K_s:
                velocity2=5
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                velocity1=0
            if event.key == pygame.K_w or event.key==pygame.K_s:
                velocity2=0

    rect_y += velocity1
    rect2_y +=velocity2
    ball_x +=ball_velocity_x
    ball_y +=ball_velocity_y
    if ball_x<0:
        score2 +=1
        ball_x=400
        ball_y=300
        ball_velocity_x=-1
        ball_velocity_y=0
        time.sleep(0.15)
    if ball_x>window_width-ball_width:
        score1 +=1
        ball_x=400
        ball_y=300
        ball_velocity_x=1
        ball_velocity_y=0
        time.sleep(0.15)
    if (ball_x+ball_width>=rect_x and rect_x+rect_width>ball_x and ball_y+ball_length>rect_y and rect_y+rect_length>ball_y) or (ball_x+ball_width>=rect2_x and rect2_x+rect_width>ball_x+ball_width and ball_y+ball_length>rect2_y and rect2_y+rect_length>ball_y):
        ball_velocity_x = ball_velocity_x*-1.15
        if(ball_x+ball_width>=rect_x and rect_x+rect_width>ball_x and ball_y+ball_length>rect_y and rect_y+rect_length>ball_y) and (velocity1 !=0):
            ball_velocity_y=velocity1*0.5
        elif(ball_x+ball_width>=rect2_x and rect2_x+rect_width>ball_x+ball_width and ball_y+ball_length>rect2_y and rect2_y+rect_length>ball_y) and(velocity2 !=0):
            ball_velocity_y=velocity2*0.5
    if ball_y < 0:
        ball_velocity_y *=-1
    elif ball_y > window_height - ball_length:
        ball_velocity_y *=-1
    if rect_y < 0:
        rect_y = 0
    elif rect_y > window_height - rect_length:
        rect_y = window_height - rect_length


    if rect2_y < 0:
        rect2_y = 0
    elif rect2_y > window_height - rect_length:
        rect2_y = window_height - rect_length
    text=font.render(f"LeftPlayer {score1}:{score2} RightPlayer",True,(0,255,0))
    if score1 == 10:
        screen.fill((0, 0, 0))
        screen.blit(text,(250,270))
        winner_text = font.render("Left player wins! Press 'r' to restart", True, (0, 255, 0))
        screen.blit(winner_text, (200, 250))
        pygame.display.update()
        time.sleep(1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    score1 = 0
                    score2 = 0
                    ball_x = 400
                    ball_y = 300
                    ball_velocity_x = 1
                    ball_velocity_y = 0
                    rect_y = 275
                    rect2_y = 275
                    pygame.time.wait(500)
                    break
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            break
    elif score2 == 10:
        screen.fill((0, 0, 0))
        screen.blit(text,(250,270))
        winner_text = font.render("Right player wins! Press 'r' to restart", True, (0, 255, 0))
        screen.blit(winner_text, (200, 250))
        pygame.display.update()
        time.sleep(1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    score1 = 0
                    score2 = 0
                    ball_x = 400
                    ball_y = 300
                    ball_velocity_x = 1
                    ball_velocity_y = 0
                    rect_y = 275
                    rect2_y = 275
                    pygame.time.wait(500)
                    break
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            break
    rect_size_loc = (rect_x, rect_y, rect_width, rect_length)
    rect2_size_loc=(rect2_x,rect2_y,rect_width,rect_length)
    ball_size_loc=(ball_x,ball_y,ball_width,ball_length)
    screen.fill((0, 0, 0))
    text.set_alpha(300)
    screen.blit(text,(250,270))
    pygame.draw.rect(screen,ball_color,ball_size_loc)
    pygame.draw.rect(screen,rect_color,rect_size_loc)
    pygame.draw.rect(screen,rect_color,rect2_size_loc)
    pygame.display.update()
    clock.tick(60)