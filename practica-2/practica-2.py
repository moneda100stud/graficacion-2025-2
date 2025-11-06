from matplotlib import lines
import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 2 - Saltos")

# Definición del suelo
suelo_rect = pygame.Rect(0, 340, 600, 20)
color_suelo = (100, 50, 0)


x, y = 300, 300
vel_y = 0
gravedad = 1
# Variables para controlar los saltos dobles 
en_suelo = True
saltos_hechos = 0
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # bloque  de saltos dobles agregando los eventos de teclado      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and saltos_hechos < 2:
                # Salto modifcado para mas fuerza de empuje para el salto vel_y = -30
                vel_y = -20
                # bloque para contar los saltos 
                saltos_hechos += 1
                en_suelo = False

    y += vel_y
    vel_y += gravedad

    if y >= 300:
        y = 300
        vel_y = 0
        saltos_hechos = 0
        en_suelo = True

    pantalla.fill((50, 50, 100))
    # Dibujar el suelo
    pygame.draw.rect(pantalla, color_suelo, suelo_rect)
    pygame.draw.rect(pantalla, (255, 255, 0), (x, y, 40, 40))
    pygame.display.update()

pygame.quit()