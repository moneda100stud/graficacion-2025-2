import pygame
import random

pygame.init()

# --- Constantes ---
ANCHO_PANTALLA, ALTO_PANTALLA = 600, 400
ANCHO_JUGADOR, ALTO_JUGADOR = 40, 40
ANCHO_ENEMIGO, ALTO_ENEMIGO = 40, 40

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Práctica 4 - Colisiones")

jugador = pygame.Rect(50, 300, ANCHO_JUGADOR, ALTO_JUGADOR)
balas = []
enemigos = [pygame.Rect(500, 300, ANCHO_ENEMIGO, ALTO_ENEMIGO)]
clock = pygame.time.Clock()
running = True

# --- Variables del juego ---
puntuacion = 0
fuente = pygame.font.Font(None, 36)  # Fuente para el texto del puntaje

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(jugador.x + 40, jugador.y + 15, 10, 5))

    for b in balas:
        b.x += 10
    balas = [b for b in balas if b.x < ANCHO_PANTALLA]

    # Detección de colisiones
    for b in balas[:]:
        for e in enemigos[:]:
            if b.colliderect(e):
                balas.remove(b)
                enemigos.remove(e)
                puntuacion += 1  # Incrementar el puntaje
                # Crear un nuevo enemigo en una posición aleatoria
                # Se genera en la mitad derecha para no aparecer sobre el jugador
                mitad_pantalla = ANCHO_PANTALLA / 2
                nuevo_x = random.randint(int(mitad_pantalla), ANCHO_PANTALLA - ANCHO_ENEMIGO)
                nuevo_y = 300  # Posición Y fija para que aparezca en la misma línea
                enemigos.append(pygame.Rect(nuevo_x, nuevo_y, ANCHO_ENEMIGO, ALTO_ENEMIGO))
                break  # La bala ya colisionó, no necesita seguir buscando

    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, (0, 255, 0), jugador)
    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b)
    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e)

    # Mostrar el puntaje en la pantalla
    texto_puntaje = fuente.render(f"Puntaje: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto_puntaje, (10, 10))

    pygame.display.update()

pygame.quit()
