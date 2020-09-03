import pygame #파이 게임 모듈 임포트
import time
pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
game_over=False
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 
score = 0
start_time = int(time.time())
remain_second = 10
small_font = pygame.font.SysFont('malgungothic', 36)
#변수
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
import random
mole_image = pygame.image.load('asset/whack_mole/mole.png')
moles = []
for i in range(2):
    mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
    after_second = random.randint(0, 3)
    during_second = random.randint(1, 3)
    appear_time = int(time.time()) + after_second
    disappear_time = int(time.time()) + after_second + during_second
    moles.append((mole, appear_time, disappear_time))
while True: #게임 루프
    screen.fill(BLACK) #단색으로 채워 화면 지우기
    #변수 업데이트
    current_time=int(time.time())
    if not game_over:
        remain_second=10-(current_time-start_time)
    event = pygame.event.poll() #이벤트 처리
    if remain_second<=0:
        game_over=True
    if event.type == pygame.QUIT:
        break
    elif event.type==pygame.MOUSEBUTTONDOWN and not game_over:
        print(event.pos[0],event.pos[1])
        for mole, appear_time, disappear_time in moles:
            if mole.collidepoint(event.pos):
                print(mole)
                moles.remove((mole, appear_time, disappear_time))
                mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
                after_second = random.randint(0, 2)
                during_second = random.randint(1,2)
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                moles.append((mole, appear_time, disappear_time))
                score += 1
    #화면 그리기
    score_image = small_font.render('점수 {}'.format(score), True, YELLOW)
    screen.blit(score_image, (10, 10))
    if not game_over:
        for mole, appear_time, disappear_time in moles:
            if disappear_time<current_time:
                print(mole)
                moles.remove((mole, appear_time, disappear_time))
                mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
                after_second = random.randint(0, 2)
                during_second = random.randint(1,2)
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                moles.append((mole, appear_time, disappear_time))

    for mole, appear_time, disappear_time in moles:
        current_time = int(time.time())
        if  current_time >= appear_time and disappear_time>=current_time and not game_over:
            screen.blit(mole_image, mole)

    remain_second_image = small_font.render('남은 시간 {}'.format(remain_second), True, YELLOW)
    screen.blit(remain_second_image, remain_second_image.get_rect(right=SCREEN_WIDTH - 10, top=10))
    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 