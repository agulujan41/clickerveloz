import pygame
import time 
from random import randint
pygame.init()

#creamos ventana
color_fondo = (200,255,255)
ventana = pygame.display.set_mode((500,500))
ventana.fill(color_fondo)
pygame.display.set_caption("Clicker Veloz")
clock = pygame.time.Clock()


#rectangulo

class Rectangulo():
    def __init__(self,x,y,ancho,alto,colorRectangulo):
        self.rect = pygame.Rect(x,y,ancho,alto)
        self.colorDeRelleno = colorRectangulo
    def cambiarColor(self,nuevoColor):
        self.colorDeRelleno = nuevoColor
    def rellenar(self):
        pygame.draw.rect(ventana, self.colorDeRelleno,self.rect)
    def bordear(self,colorBorde,anchoDelBorde):
        pygame.draw.rect(ventana,colorBorde,self.rect,anchoDelBorde)
    def estaClickeando(self,x,y):
        return self.rect.collidepoint(x,y)

class Etiqueta(Rectangulo):
    def cambiar_texto(self,texto,tamanioFuente,colorTexto):
        self.image = pygame.font.SysFont('verdana', tamanioFuente).render(texto, True, colorTexto)

    def dibujar(self,cambiarx,cambiary):
        self.rellenar()
        ventana.blit(self.image, (self.rect.x +cambiarx, self.rect.y + cambiary))        

AMARILLO = (255,255,0)
AZUL_OSCURO = (0,0,100)
AZUL = (80,80,255)
NEGRO = (0,0,0)
VERDE = (0,255,0)
ROJO = (255,0,0)
etiquetas = []

numero_tarjetas = 4

x = 70
contador_tiempo = Etiqueta(10,10,50,50,color_fondo)
contador_tiempo.cambiar_texto("Tiempo:",20,NEGRO)
cronometro = Etiqueta(100,10,50,50,color_fondo)
cronometro.cambiar_texto("0",20,NEGRO)

contador_puntaje = Etiqueta(450,10,50,50,color_fondo)
contador_puntaje.cambiar_texto("Contar:",20,NEGRO)
puntaje_etiqueta = Etiqueta(450,10,50,50,color_fondo)
puntaje_etiqueta.cambiar_texto("0",20,NEGRO)

tiempo_inicio = time.time()
tiempo_actual = time.time()


for i in range (numero_tarjetas):
    nueva_etiqueta = Etiqueta(x,170,70,100,AMARILLO)
    nueva_etiqueta.bordear(AZUL,13)
    nueva_etiqueta.cambiar_texto("CLIC",20,NEGRO)
    etiquetas.append(nueva_etiqueta)
    x= x+100


esperar = 0 
puntos = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            x,y = event.pos
            for i in range(0,numero_tarjetas):
                if etiquetas[i].estaClickeando(x,y):
                    if (i+1) == click:
                        etiquetas[i].cambiarColor(VERDE)
                        puntos= puntos +1
                        puntaje_etiqueta.cambiar_texto(str(puntos),20,NEGRO)
                    else:
                        etiquetas[i].cambiarColor(ROJO)
                        puntos = puntos -1 
                        puntaje_etiqueta.cambiar_texto(str(puntos),20,NEGRO)

                    etiquetas[i].rellenar()
            
    if esperar == 0:
        esperar = 20
        click = randint(1,numero_tarjetas)
        for i in range(numero_tarjetas):
            etiquetas[i].cambiarColor(AMARILLO)
            if (i+1) == click:
                etiquetas[i].dibujar(10,35)
            else:
                 etiquetas[i].rellenar()
    else:
        esperar = esperar - 1

    contador_tiempo.dibujar(0,0)
    cronometro.dibujar(0,0)
    contador_puntaje.dibujar(-80,0)
    puntaje_etiqueta.dibujar(10,0)

    nuevo_tiempo = time.time()
    if nuevo_tiempo -tiempo_inicio >=11:
        pantallaTimeOver = Etiqueta(0,0,500,500,ROJO)
        pantallaTimeOver.cambiar_texto("¡¡¡Tiempo terminado!!!",40,NEGRO)
        pantallaTimeOver.dibujar(20,180)

        
    if int(nuevo_tiempo)-int(tiempo_actual) == 1:
        cronometro.cambiar_texto(str(int(nuevo_tiempo-tiempo_inicio)),20,NEGRO)
        tiempo_actual = nuevo_tiempo

    if puntos >= 5 :
        pantallaGanaste = Etiqueta(0,0,500,500,VERDE)
        pantallaGanaste.cambiar_texto("¡¡¡Ganaste!!!",40,NEGRO)
        pantallaGanaste.dibujar(80,180)

        

    if puntos <= -5:
        pantallaPerdiste = Etiqueta(0,0,500,500,ROJO)
        pantallaPerdiste.cambiar_texto("¡¡¡Perdiste!!!",40,NEGRO)
        pantallaPerdiste.dibujar(80,180)
        etiquetaVolverJugar = Etiqueta(180,450,2GI00,100,AMARILLO)
        etiquetaVolverJugar.cambiar_texto("Volver a Jugar",20,NEGRO)
        etiquetaVolverJugar.dibujar(10,10)
    pygame.display.update()
    clock.tick(40)