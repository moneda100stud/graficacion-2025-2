import pygame
pygame.init()

# --- Configuración ---
ANCHO, ALTO = 640, 480
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación Direccional - Sprite Sheet")

# --- Cargar Sprite Sheet ---
sprite_sheet = pygame.image.load("personaje_direcciones.png").convert_alpha()
# --- Cargar y escalar el fondo ---
fondo = pygame.image.load("fondo-juego.png").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# --- Dimensiones de los fotogramas (¡CORRECCIÓN CLAVE!) ---
# Ahora cada sprite mide 64x64 en la hoja
FRAME_ANCHO = 220
FRAME_ALTO = 298
FILAS = 4     # Una fila por dirección
COLUMNAS = 4   # Cuatro fotogramas por fila

sprite_sheet.set_colorkey((255, 255, 255))  # Color de transparencia (Blanco)

# --- Tamaño del personaje en pantalla (Se ajusta al mismo tamaño, 64x64) ---
# Si quisieras el doble de tamaño (128x128), cambiarías estos valores.
JUGADOR_ANCHO = 64
JUGADOR_ALTO = 64

# --- Función para extraer los cuadros de una fila ---
def obtener_frames(fila):
    frames = []
    for i in range(COLUMNAS):
        # Utiliza las dimensiones CORRECTAS (64x64) para el recorte
        rect = pygame.Rect(i * FRAME_ANCHO, fila * FRAME_ALTO, FRAME_ANCHO, FRAME_ALTO)
        frame = sprite_sheet.subsurface(rect).copy().convert_alpha()
        
        # Escalamos el frame al tamaño deseado para el jugador (64x64)
        frame_escalado = pygame.transform.scale(frame, (JUGADOR_ANCHO, JUGADOR_ALTO))
        frames.append(frame_escalado)
    return frames

# --- Diccionario con las animaciones de cada dirección (Mapeo corregido) ---
# Asumiendo el orden estándar: Fila 0=Abajo, Fila 1=Izquierda, Fila 2=Derecha, Fila 3=Arriba
animaciones = {
    "abajo": obtener_frames(0),
    "izquierda": obtener_frames(2),
    "derecha": obtener_frames(1),
    "arriba": obtener_frames(3)
}

# --- Animación de "quieto" (idle) ---
# Usaremos el primer y tercer cuadro de la animación "abajo" para un efecto de respiración.
animacion_quieto = [animaciones["abajo"][0], animaciones["abajo"][2]]
tiempo_animacion_quieto = 400 # Hacemos que la animación de quieto sea más lenta

# --- Variables de juego ---
x, y = ANCHO // 2, ALTO // 2
velocidad = 3
direccion = "abajo"
frame_index = 0
ultimo_tiempo = pygame.time.get_ticks()
tiempo_animacion = 150  # milisegundos entre cuadros
reloj = pygame.time.Clock()
estaba_moviendose = False # Nueva variable para detectar cambio de estado

# --- Bucle principal ---
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # --- Movimiento y dirección ---
    teclas = pygame.key.get_pressed()
    moviendo = False

    if teclas[pygame.K_UP]:
        y -= velocidad
        direccion = "arriba"
        moviendo = True
    elif teclas[pygame.K_DOWN]:
        y += velocidad
        direccion = "abajo"
        moviendo = True
    elif teclas[pygame.K_LEFT]:
        x -= velocidad
        direccion = "izquierda"
        moviendo = True
    elif teclas[pygame.K_RIGHT]:
        x += velocidad
        direccion = "derecha"
        moviendo = True

    # --- Límites de la pantalla ---
    # El personaje se dibuja desde su centro, así que usamos la mitad de su tamaño para los bordes.
    mitad_ancho = JUGADOR_ANCHO // 2
    mitad_alto = JUGADOR_ALTO // 2
    if x < mitad_ancho:
        x = mitad_ancho
    if x > ANCHO - mitad_ancho:
        x = ANCHO - mitad_ancho
    if y < mitad_alto:
        y = mitad_alto
    if y > ALTO - mitad_alto:
        y = ALTO - mitad_alto

    # --- Reiniciar índice si el estado de movimiento cambia ---
    if moviendo != estaba_moviendose:
        frame_index = 0
    estaba_moviendose = moviendo

    # --- Actualizar animación ---
    ahora = pygame.time.get_ticks()
    if moviendo:
        # Animación de caminar
        # Asegurarse de que el índice no se salga de rango para la animación actual
        if ahora - ultimo_tiempo > tiempo_animacion:
            frame_index = (frame_index + 1) % len(animaciones[direccion])
            ultimo_tiempo = ahora
    else:
        # Animación de quieto (idle)
        if ahora - ultimo_tiempo > tiempo_animacion_quieto:
            frame_index = (frame_index + 1) % len(animacion_quieto)
            ultimo_tiempo = ahora

    # --- Dibujar ---
    VENTANA.blit(fondo, (0, 0)) # Dibuja la imagen de fondo
    # Centrar el sprite en las coordenadas (x, y)
    frame_actual = animacion_quieto[frame_index] if not moviendo else animaciones[direccion][frame_index]
    VENTANA.blit(frame_actual, (x - JUGADOR_ANCHO // 2, y - JUGADOR_ALTO // 2)) 
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()