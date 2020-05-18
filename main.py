import pygame, random

#Variables
screen_width=1280
screen_height=960

#Colors
white_color=(200,200,200)
light_gray=pygame.Color('grey12')

pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode((screen_width,screen_height))

rectangulo=pygame.Rect(10,10,10,140)

bola=pygame.Rect(50,10,50,50)

speed=0

speed_bola_x=3
speed_bola_y=3

def mover_rectangulo():
    global speed
    if rectangulo.top +150 < screen_height:
        rectangulo.top+=speed



def start_bola():
    global speed_bola_x,speed_bola_y
    if(bola.left+50>screen_width or bola.left<0):
        bola.top=screen_height//2
        bola.left=screen_width//2
        speed_bola_x=3*random.choice((1,-1))
        speed_bola_y=3*random.choice((1,-1))

def mover_bola():
    global speed_bola_x,speed_bola_y
    if(bola.top+50>screen_height or bola.top<0):
        speed_bola_x=-speed_bola_x

    if bola.left<10 and rectangulo.top<bola.top<rectangulo.top+140:
        speed_bola_y=-speed_bola_y

    start_bola()

    bola.top +=speed_bola_x
    bola.left +=speed_bola_y

while True:
    screen.fill(light_gray)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed=-3
            elif event.key == pygame.K_DOWN:
                speed=3
        elif event.type == pygame.KEYUP:
            speed=0

    mover_bola()
    mover_rectangulo()
    pygame.draw.rect(screen,white_color,rectangulo)
    pygame.draw.ellipse(screen,white_color,bola)

    pygame.display.flip()
    clock.tick(60)