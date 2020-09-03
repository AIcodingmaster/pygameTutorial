import pygame #파이 게임 모듈 임포트

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
COOL_DOWN=100
score=0
lost_rock=0
pygame.key.set_repeat(1)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 
VELOCITY=10
MISSILE_VELOCITY=15
GAME_OVER=False
LAST=0
NOW=0
#변수

pygame.mixer.init()
pygame.mixer.music.load('asset/shoot_rock/music.mid')
pygame.mixer.music.play(-1)
game_over_sound=pygame.mixer.Sound('asset/shoot_rock/game_over.wav')
large_font = pygame.font.SysFont('malgungothic', 72)#font객체 생성
small_font = pygame.font.SysFont('malgungothic', 36)
background_image = pygame.image.load('asset/shoot_rock/background.png')
fighter_image=pygame.image.load('asset/shoot_rock/fighter.png')
fighter=fighter_image.get_rect(centerx=SCREEN_WIDTH//2,bottom=SCREEN_HEIGHT)
rock_image = pygame.image.load('asset/shoot_rock/rock.png')
rocks=[]
missile_image = pygame.image.load('asset/shoot_rock/missile.png')
missiles = []
explosion_image=pygame.image.load('asset/shoot_rock/explosion.png')
notC=True
import random
for i in range(3):
    rock=rock_image.get_rect(top=-10,left=random.randint(0,SCREEN_WIDTH-rock_image.get_width()))
    dy=random.randint(3,9)
    rocks.append((rock,dy))

while True: #게임 루프
    screen.blit(background_image, (0, 0))
    score_image=small_font.render("점수:{}".format(score),True,(255,255,0))
    screen.blit(score_image,(0,0))
    if notC:
        screen.blit(fighter_image,fighter)
    for rock,_ in rocks:
        screen.blit(rock_image,rock)
    for missile in missiles:
        screen.blit(missile_image,missile)

    for missile in missiles:
        if missile.bottom==0:
            missiles.remove(missile)
        missile.top-=MISSILE_VELOCITY
    for rock,dy in rocks:
        if rock.top==SCREEN_HEIGHT:
            rocks.remove((rock,dy))
            rock=rock_image.get_rect(left=random.randint(0,SCREEN_WIDTH-rock.width),top=-100)
            dy=random.randint(3,9)
            rocks.append((rock,dy))
        rock.bottom+=dy

    for rock,dy in rocks:
        if rock.colliderect(fighter):
            screen.blit(explosion_image,explosion_image.get_rect(centerx=fighter.centerx,centery=fighter.centery))
            rocks.remove((rock,dy))
            notC=False
            GAME_OVER=True
    if GAME_OVER:
        game_over_image=large_font.render("게임 오버",True,(255,255,0))
        game_over_sound.play()
        screen.blit(game_over_image,game_over_image.get_rect(centerx=SCREEN_WIDTH//2,centery=SCREEN_HEIGHT//2))
        

    #변수 업데이트
    for missile in missiles:
        for rock,dy in rocks:
            if missile.colliderect(rock):
                score+=5
                screen.blit(explosion_image,explosion_image.get_rect(centerx=rock.centerx,centery=rock.bottom))
                rocks.remove((rock,dy))
                missiles.remove(missile)
                rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
                rocks.append((rock,dy))

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    pressed=pygame.key.get_pressed()#동시 키를 위해서
    if pressed[pygame.K_LEFT]:
        fighter.centerx-=VELOCITY
    elif pressed[pygame.K_RIGHT]:
        fighter.centerx+=VELOCITY
    elif pressed[pygame.K_UP]:
        fighter.centery-=VELOCITY
    elif pressed[pygame.K_DOWN]:
        fighter.centery+=VELOCITY
    if pressed[pygame.K_SPACE]:
        missile=missile_image.get_rect(bottom=fighter.top,centerx=fighter.centerx)
        NOW=pygame.time.get_ticks()
        print(NOW,LAST)
        if NOW-LAST>=COOL_DOWN:
            missiles.append(missile)
            LAST=pygame.time.get_ticks()
    if fighter.left<0:
        fighter.left=0
    elif fighter.right>SCREEN_WIDTH:
        fighter.right=SCREEN_WIDTH
    elif fighter.bottom>SCREEN_HEIGHT:
        fighter.bottom=SCREEN_HEIGHT;
    elif fighter.top<0:
        fighter.top=0

    #화면 그리기

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 
