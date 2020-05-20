import pygame, random


#Variables
screen_width=1280
screen_height=960
velocidad=0
velocidad_incremento=0.5
stand_movie=3
numero_jugadas=10

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

speed_bola_x=3
speed_bola_y=3
rebote=1

accion="STAND"

def increment_speed():
    global speed_bola_y,speed_bola_x
    global rebote
    if(rebote%2==0):
        if(speed_bola_x<0):
            speed_bola_x=speed_bola_x-1
            speed_bola_y=speed_bola_y-1
        else:
            speed_bola_x+=1
            speed_bola_y+=1
        rebote=1


def draw_puntuacion(jugador,ia):
    global screen
    fuente=pygame.font.Font(None,120)
    texto_jugador=fuente.render(str(jugador),0,white_color)
    texto_ia=fuente.render(str(ia),0,white_color)
    screen.blit(texto_jugador,((screen_width//2)-120,40))
    screen.blit(texto_ia,((screen_width//2)+60,40))

def IA():
    ia.top=bola.top-50


def mover_rectangulo():
    global velocidad
    global accion
    if(accion=="UP" and jugador.top>10):
        jugador.top-=stand_movie+velocidad
        velocidad+=velocidad_incremento
    elif(accion=="DOWN" and jugador.bottom+10< screen_height):
        jugador.top+=stand_movie+velocidad
        velocidad+=velocidad_incremento
    else:
        jugador.top=jugador.top
        velocidad=0

def controller(event,pygame):
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

def reset_bola():
    global speed_bola_x,speed_bola_y
    global rebote
    rebote=1
    speed_bola_x=3
    speed_bola_y=3
    bola.top=screen_height//2
    bola.left=screen_width//2
    speed_bola_x=3*random.choice((1,-1))
    speed_bola_y=3*random.choice((1,-1))


def start_bola():
    global score_jugador
    global score_ia
    if(bola.right>screen_width):
        reset_bola()
        score_jugador+=1
    elif(bola.left<0):
        reset_bola()
        score_ia+=1


def fin_juego(jugador,ia):
    global speed_bola_y
    global speed_bola_x
    global stand_movie
    global velocidad_incremento
    if(jugador==numero_jugadas or ia==numero_jugadas):
        speed_bola_y=0
        speed_bola_x=0
        velocidad_incremento=0
        stand_movie=0
    if(jugador==numero_jugadas):
        fuente=pygame.font.Font(None,120)
        texto_jugador=fuente.render("!!!HAS GANADO¡¡¡",0,white_color)
        screen.blit(texto_jugador,((screen_width//2)-300,(screen_height//2)-100))
    elif(ia==numero_jugadas):
        fuente=pygame.font.Font(None,120)
        texto_jugador=fuente.render("!!!HAS PERDIDO¡¡¡",0,white_color)
        screen.blit(texto_jugador,((screen_width//2)-300,(screen_height//2)-100))




def mover_bola():
    global speed_bola_x,speed_bola_y
    global rebote
    if(bola.top+50>screen_height or bola.top<0):
        speed_bola_x=-speed_bola_x

    if bola.left<20 and jugador.top<bola.top<jugador.top+140:
        rebote+=1
        speed_bola_y=-speed_bola_y
    if bola.right>screen_width-20 and ia.top<bola.top<ia.top+140:
        rebote+=1
        speed_bola_y=-speed_bola_y

    start_bola()

    bola.top +=speed_bola_x
    bola.left +=speed_bola_y

while True:
    screen.fill(light_gray)
    fin_juego(score_jugador,score_ia)
    for event in pygame.event.get():
        controller(event,pygame)
    mover_bola()
    mover_rectangulo()
    increment_speed()
    IA()
    pygame.draw.rect(screen,white_color,jugador)
    pygame.draw.ellipse(screen,white_color,bola)
    pygame.draw.rect(screen,white_color,ia)
    for i in range(32):
        pygame.draw.rect(screen,white_color,separador[i])
    draw_puntuacion(score_jugador,score_ia)
    pygame.display.flip()
    clock.tick(60)