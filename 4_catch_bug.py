import pygame #파이 게임 모듈 임포트
import random
import math
import time
pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 
score=0
remain_time=10
current_time=int(time.time())
game_over=False
#변수

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
small_font=pygame.font.SysFont("malgungothic",36)
bug_image = pygame.image.load('asset/catch_bug/bug.png')
bugs = []
for i in range(3):
    degree=random.randint(0,360)
    bug = bug_image.get_rect(left=random.randint(0,SCREEN_WIDTH), top=random.randint(0,SCREEN_HEIGHT))
    bugs.append((bug,degree))

while True: #게임 루프
    future_time=int(time.time())
    if remain_time<=0:
        game_over=True
    else:
        remain_time=10+current_time-future_time
    screen.fill(BLACK) #단색으로 채워 화면 지우기
    for bug,degree in bugs:
        if not bug.colliderect(screen.get_rect()):
            bugs.remove((bug,degree))
            bug = bug_image.get_rect(left=random.randint(0, SCREEN_WIDTH) - bug_image.get_width(), top=random.randint(0, SCREEN_HEIGHT) - bug_image.get_height())
            bugs.append((bug,random.randint(0,360)))
    #변수 업데이트

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type==pygame.MOUSEBUTTONDOWN:
        print(event.pos[0],event.pos[1])
        for bug,degree in bugs:
            if bug.collidepoint(event.pos):
                bugs.remove((bug,degree))
                bug=bug_image.get_rect(left=random.randint(0, SCREEN_WIDTH) - bug_image.get_width(), top=random.randint(0, SCREEN_HEIGHT) - bug_image.get_height())
                bugs.append((bug,random.randint(0,360)))
                score+=1
    for bug,degree in bugs:
        radian=math.pi*degree/180
        if not game_over:
            bug.left+=5*math.cos(radian)
            bug.top-=5*math.sin(radian)
    #화면 그리기
    score_image=small_font.render('점수 {}'.format(score),True,YELLOW)
    time_image=small_font.render('남은시간 {}'.format(remain_time),True,YELLOW)
    screen.blit(score_image,score_image.get_rect(left=10,top=10))
    screen.blit(time_image,score_image.get_rect(left=SCREEN_WIDTH-time_image.get_width(),top=10))
    for bug,degree in bugs:
        screen.blit(pygame.transform.rotate(bug_image, degree), bug)

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 