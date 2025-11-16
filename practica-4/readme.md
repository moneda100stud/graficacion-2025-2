# Práctica 4: Colisiones, Reaparición y Puntuación

## Descripción

El objetivo de esta práctica era construir un minijuego de disparos. Se partió de una base con un jugador estático que puede disparar balas. A lo largo del desarrollo, se añadieron mecánicas de colisión, la reaparición de enemigos en posiciones aleatorias y un sistema de puntuación para registrar el progreso del jugador.

## Proceso de Desarrollo

1.  **Mecánica de Disparo y Colisión**:
    *   Se implementó la capacidad del jugador para disparar balas (rectángulos) al presionar la barra espaciadora.
    *   Se utilizó un bucle anidado para comprobar la colisión entre cada bala y cada enemigo usando `colliderect()`.
    *   Al detectar una colisión, tanto la bala como el enemigo son eliminados de sus respectivas listas.

2.  **Reaparición de Enemigos**:
    *   Tras la destrucción de un enemigo, se genera uno nuevo para mantener el juego activo.
    *   Inicialmente, la reaparición era completamente aleatoria en la pantalla.
    *   Se refinó para que el enemigo reapareciera solo en una posición horizontal aleatoria, pero manteniendo una altura (`y`) fija, alineada con el jugador.

3.  **Sistema de Puntuación**:
    *   Se inicializó una variable `puntuacion` en `0`.
    *   Cada vez que un enemigo es destruido, la puntuación se incrementa en 1.
    *   Se utilizó `pygame.font` para renderizar el puntaje como texto y `pantalla.blit()` para mostrarlo en la esquina superior izquierda de la pantalla en cada fotograma.

## Inconvenientes y Soluciones

*   **Inconveniente 1: Error `ValueError` al reaparecer.**
    *   **Problema**: Al intentar generar una posición aleatoria, el programa fallaba con un `ValueError: empty range in randrange()`. Esto se debía a que el rango para `random.randint()` era inválido (ej. `randint(0, -100)`).
    *   **Solución**: Se corrigió la lógica para usar el ancho de la pantalla y el ancho del enemigo (`ANCHO_PANTALLA - ANCHO_ENEMIGO`), asegurando que el rango siempre fuera válido.

*   **Inconveniente 2: El enemigo "crecía" y aparecía en lugares incorrectos.**
    *   **Problema**: El nuevo enemigo se creaba con un tamaño diferente al original y podía aparecer en cualquier parte, incluso fuera de la línea de tiro.
    *   **Solución**: Se estandarizó el tamaño del enemigo usando constantes y se fijó la coordenada `y` de reaparición a la misma altura del jugador (`300`).

*   **Inconveniente 3: El enemigo reaparecía sobre el jugador.**
    *   **Problema**: El enemigo podía aparecer en una coordenada `x` que se superponía con la del jugador. Esto causaba que las balas se crearan "dentro" o "delante" del enemigo, haciendo imposible dispararle.
    *   **Solución**: Se limitó el área de reaparición a la mitad derecha de la pantalla. Esto garantiza que siempre haya una distancia inicial entre el jugador y el nuevo enemigo, solucionando el bug.