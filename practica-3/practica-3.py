import pygame
pygame.init()

# Inicializar el mezclador de audio y cargar el sonido
pygame.mixer.init()
sonido_disparo = pygame.mixer.Sound('laser-312360.mp3')

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 3 - Disparos")

x, y = 50, 300
vel_jugador = 10
vel_bala = 28
balas = []
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Reproducir sonido de disparo
            sonido_disparo.play()

            # Determinar la dirección de la bala según las flechas presionadas
            teclas = pygame.key.get_pressed()
            dx, dy = 0, 0
            if teclas[pygame.K_UP]:
                dy = -vel_bala
            elif teclas[pygame.K_DOWN]:
                dy = vel_bala
            elif teclas[pygame.K_LEFT]:
                dx = -vel_bala
            elif teclas[pygame.K_RIGHT]:
                dx = vel_bala
            else: # Dirección por defecto si no se presiona ninguna flecha
                dx = vel_bala

            # Crear la bala con su rectángulo y su dirección
            bala_rect = pygame.Rect(x + 15, y + 15, 10, 10) # Centrar la bala
            balas.append((bala_rect, dx, dy))

   

    # Mover y eliminar las balas que salen de la pantalla
    for i in range(len(balas) - 1, -1, -1):
        bala_rect, dx, dy = balas[i]
        bala_rect.x += dx
        bala_rect.y += dy
        if not pantalla.get_rect().colliderect(bala_rect):
            balas.pop(i)

    # --- Dibujo ---
    pantalla.fill((30, 30, 30))
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, 40, 40))
    for bala_rect, _, _ in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), bala_rect)
    pygame.display.update()

pygame.quit()
