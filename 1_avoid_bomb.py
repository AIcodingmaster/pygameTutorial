import pygame

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
bombs=[]
score = 0
game_over = False

large_font = pygame.font.SysFont('malgungothic', 72)#font객체 생성
small_font = pygame.font.SysFont('malgungothic', 36)
bomb_image = pygame.image.load('asset/avoid_bomb/bomb.png')
import random
for i in range(2):
    bomb=bomb_image.get_rect(left=random.randint(0,600-bomb_image.get_width()),top=-100)
    dy = random.randint(3, 9)
    bombs.append((bomb,dy))

pygame.mixer.init()
pygame.mixer.music.load('asset/avoid_bomb/music.mid') #배경 음악
pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번
game_over_sound = pygame.mixer.Sound('asset/avoid_bomb/game_over.wav')    

pygame.key.set_repeat(1,1)#(지연시간, 간격) ms 단위
girl_image = pygame.image.load('asset/avoid_bomb/girl.png')
girl=girl_image.get_rect(centerx=300,bottom=800)#크기 좌표를 담고 있는 객체 리턴됨
'''
img.get_width()
left
centerx
right
top
centery
bottom
center #(centerx, centery)
bomb.width
height
'''
while True:
    screen.fill((0, 0, 0))
    for bomb,dy in bombs:
        bomb.bottom+=dy
        if not game_over:
            if bomb.top>800:
                bombs.remove((bomb,dy))
                bomb = bomb_image.get_rect(left=random.randint(0, 600 - bomb.width), top=-100)
                dy=random.randint(3,9)
                bombs.append((bomb,dy))
                score+=1
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:#key가 눌렸을때
        if event.key == pygame.K_LEFT:
            girl.left-=5
        elif event.key == pygame.K_RIGHT:
            girl.left+=5
    if girl.left<0:
        girl.left=0
    elif girl.right>600:
        girl.right=600
    for bomb,_ in bombs:
        if bomb.colliderect(girl):#충돌
            game_over=True
            pygame.mixer.music.stop()#배경음악 중지
            game_over_sound.play()
    #drawing
    screen.blit(girl_image,girl)#blit는 이미지를 목적지 비트맵에 복사하는 것을 의미
    score_image = small_font.render('점수 {}'.format(score), True, (255 ,255, 0))#render(텍스트, 안티엘리어싱, 색깔튜플)
    
    screen.blit(score_image, (10, 10))
    if game_over:
        game_over_image=large_font.render('게임 종료',True,(255,0,0))
        screen.blit(game_over_image, game_over_image.get_rect(centerx=300, centery=400))   
    for bomb,_ in bombs:
        screen.blit(bomb_image,bomb)
    pygame.display.update()
    clock.tick(30) #초당 프레임수

pygame.quit() 