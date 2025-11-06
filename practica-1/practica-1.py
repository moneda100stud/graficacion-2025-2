import pygame

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 1 - Movimiento básico")

x, y = 300, 200
vel = 5
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= vel
    if teclas[pygame.K_RIGHT]:
        x += vel
    if teclas[pygame.K_UP]:
        y -= vel
    if teclas[pygame.K_DOWN]:
        y += vel
    # Aumentar la velocidad al mantener presionada la tecla Shift y disminuirla al soltarla     
    if shift := teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]: 
        vel = 50 
    else:
        vel = 5

    #  mantener el cuadrado dentro de la ventana 
    ancho_rect, alto_rect = 40, 40
    if x < 0:
        x = 0
    if x > 600 - ancho_rect:
        x = 600 - ancho_rect
    if y < 0:
        y = 0
    if y > 400 - alto_rect:
        y = 400 - alto_rect

    pantalla.fill((30, 30, 30))
    # cambio de color del rectángulo a verde  cambiando los valores RGB despues de la seccion pantalla,((30, 30, 30)) 
    pygame.draw.rect(pantalla, (0, 250, 0), (x, y, 40, 40))

    pygame.display.update()

pygame.quit()