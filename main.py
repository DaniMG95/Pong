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

jugador=pygame.Rect(10,10,10,140)
ia=pygame.Rect(screen_width-20,10,10,140)

separador=[]

for i in range(32):
    cuadrado=pygame.Rect(screen_width//2,i*30,5,10)
    separador.append(cuadrado)

cuadrado=pygame.Rect(screen_width-20,10,10,140)


score_jugador=0
score_ia=0
bola=pygame.Rect(50,10,50,50)

speed=0

speed_bola_x=3
speed_bola_y=3

accion="STAND"

def draw_puntuacion(jugador,ia):
    global screen
    fuente=pygame.font.Font(None,120)
    texto_jugador=fuente.render(str(jugador),0,(255,255,255))
    texto_ia=fuente.render(str(ia),0,(255,255,255))
    screen.blit(texto_jugador,((screen_width//2)-120,40))
    screen.blit(texto_ia,((screen_width//2)+60,40))

def IA():
    ia.top=bola.top-50

def mover_rectangulo():
    global speed
    global accion
    if(accion=="UP" and jugador.top>10):
        jugador.top-=3
    elif(accion=="DOWN" and jugador.bottom+10< screen_height):
        jugador.top+=3
    else:
        jugador.top=jugador.top

def controller(event,pygame):
    global speed
    global accion
    # Controla el cambio de  las direcciones
    # Orientaciones
    # Horizontal    -> Movimientos [UP - DOWN]
    # Incremento del movimiento
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            accion="UP"
        elif event.key == pygame.K_DOWN:
            accion="DOWN"
        else:
            accion="STAND"
    else:
        accion="STAND"

def start_bola():
    global speed_bola_x,speed_bola_y
    global score_jugador
    global score_ia
    if(bola.right>screen_width):
        score_jugador+=1
        bola.top=screen_height//2
        bola.left=screen_width//2
        speed_bola_x=3*random.choice((1,-1))
        speed_bola_y=3*random.choice((1,-1))
    elif(bola.left<0):
        score_ia+=1
        bola.top=screen_height//2
        bola.left=screen_width//2
        speed_bola_x=3*random.choice((1,-1))
        speed_bola_y=3*random.choice((1,-1))



def mover_bola():
    global speed_bola_x,speed_bola_y
    if(bola.top+50>screen_height or bola.top<0):
        speed_bola_x=-speed_bola_x

    if bola.left<20 and jugador.top<bola.top<jugador.top+140:
        speed_bola_y=-speed_bola_y
    if bola.right>screen_width-20 and ia.top<bola.top<ia.top+140:
        speed_bola_y=-speed_bola_y

    start_bola()

    bola.top +=speed_bola_x
    bola.left +=speed_bola_y

while True:
    screen.fill(light_gray)

    for event in pygame.event.get():
        controller(event,pygame)
    mover_bola()
    mover_rectangulo()
    IA()
    pygame.draw.rect(screen,white_color,jugador)
    pygame.draw.ellipse(screen,white_color,bola)
    pygame.draw.rect(screen,white_color,ia)
    for i in range(32):
        pygame.draw.rect(screen,white_color,separador[i])
    draw_puntuacion(score_jugador,score_ia)
    pygame.display.flip()
    clock.tick(60)