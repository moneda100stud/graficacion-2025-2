import pygame
import random

pygame.init()

# --- Constantes y configuración inicial ---
ANCHO_PANTALLA, ALTO_PANTALLA = 600, 400
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Mini Juego Final")

# --- Carga de recursos (imágenes y fuente) ---
fondo = pygame.image.load("fondo.png").convert()
fondo = pygame.transform.scale(fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))

sprite_jugador = pygame.image.load("personaje.png").convert_alpha() # Usar convert_alpha para transparencias
sprite_jugador = pygame.transform.scale(sprite_jugador, (80, 80))

fuente = pygame.font.Font(None, 36)

# --- Variables del fondo ---
fondo_ancho = fondo.get_width()
fondo_x = 0
velocidad_scroll = 1

# --- Variables del jugador ---
jugador_rect = sprite_jugador.get_rect(midbottom=(100, 360)) #posición inicial del jugador
velocidad_y_jugador = 0
gravedad = 1
fuerza_salto = -20
en_el_suelo = True

# --- Variables de balas y enemigos ---
balas = []
enemigos = []
TIEMPO_SPAWN_ENEMIGO = pygame.USEREVENT + 1
pygame.time.set_timer(TIEMPO_SPAWN_ENEMIGO, 2000) # Un enemigo nuevo cada 2 segundos

# --- Variables del juego ---
puntuacion = 0
game_over = False
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60) # Aumentamos los FPS para un movimiento más suave

    # --- Manejo de eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Evento para disparar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and en_el_suelo:
                # Disparar solo si está en el suelo para simplificar
                balas.append(pygame.Rect(jugador_rect.right, jugador_rect.centery - 5, 10, 5))
            if event.key == pygame.K_UP and en_el_suelo:
                # Saltar
                velocidad_y_jugador = fuerza_salto
                en_el_suelo = False
        
        # Evento para crear enemigos
        if event.type == TIEMPO_SPAWN_ENEMIGO:
            nuevo_enemigo_rect = pygame.Rect(ANCHO_PANTALLA, 313, 40, 40)
            enemigos.append(nuevo_enemigo_rect)

    if not game_over:
        # --- Lógica del juego ---

        # Mover fondo
        fondo_x -= velocidad_scroll # El fondo se mueve constantemente
        if fondo_x <= -fondo_ancho:
            fondo_x = 0

        # Lógica de salto del jugador
        if not en_el_suelo:
            velocidad_y_jugador += gravedad
            jugador_rect.y += velocidad_y_jugador
            if jugador_rect.bottom >= 355:
                jugador_rect.bottom = 355
                en_el_suelo = True
                velocidad_y_jugador = 0

        # Mover balas y eliminar las que salen de pantalla
        for bala in balas:
            bala.x += 8
        balas = [bala for bala in balas if bala.x < ANCHO_PANTALLA]

        # Mover enemigos y eliminar los que salen de pantalla
        for enemigo in enemigos:
            enemigo.x -= 3
        enemigos = [enemigo for enemigo in enemigos if enemigo.right > 0]

        # Detección de colisiones (bala-enemigo)
        for bala in balas[:]:
            for enemigo in enemigos[:]:
                if bala.colliderect(enemigo):
                    balas.remove(bala)
                    enemigos.remove(enemigo)
                    puntuacion += 1
                    break
        
        # Detección de colisiones (jugador-enemigo)
        for enemigo in enemigos:
            if jugador_rect.colliderect(enemigo):
                game_over = True

    # --- Dibujado en pantalla ---
    pantalla.blit(fondo, (fondo_x, 0))
    pantalla.blit(fondo, (fondo_x + fondo_ancho, 0))

    if game_over:
        # Mostrar pantalla de Game Over
        texto_game_over = fuente.render("GAME OVER", True, (200, 0, 0))
        texto_rect = texto_game_over.get_rect(center=(ANCHO_PANTALLA/2, ALTO_PANTALLA/2))
        pantalla.blit(texto_game_over, texto_rect)
    else:
        # Dibujar elementos del juego
        pantalla.blit(sprite_jugador, jugador_rect)
        for bala in balas:
            pygame.draw.rect(pantalla, (255, 255, 0), bala) # Balas amarillas
        for enemigo in enemigos:
            pygame.draw.rect(pantalla, (255, 0, 0), enemigo) # Enemigos rojos

    # Dibujar puntuación
    texto_puntaje = fuente.render(f"Puntaje: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto_puntaje, (10, 10))

    pygame.display.update()

pygame.quit()
