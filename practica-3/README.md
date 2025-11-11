# Práctica 3: Disparos en Múltiples Direcciones (finalizado)
)

## Descripción

El objetivo de esta práctica fue implementar una mecánica de disparo. El jugador puede disparar proyectiles (balas) en cuatro direcciones (arriba, abajo, izquierda y derecha) usando las flechas del teclado y la barra espaciadora. También se añadió un efecto de sonido para cada disparo.

## Cambios Realizados

1.  **Estructura de las Balas**: Se reestructuró la forma en que se almacenan las balas. En lugar de una simple lista de rectángulos, se usa una lista de tuplas. Cada tupla contiene el `pygame.Rect` de la bala y sus velocidades en los ejes `x` e `y`: `(rect, dx, dy)`.
2.  **Lógica de Disparo**: Al presionar la barra espaciadora, el juego detecta qué tecla de flecha está presionada. Basado en eso, determina la dirección `(dx, dy)` de la nueva bala. Luego, crea la tupla de la bala y la añade a la lista.
3.  **Movimiento y Eliminación de Balas**: En cada fotograma, el juego itera sobre la lista de balas, actualizando la posición de cada rectángulo según su `dx` y `dy` almacenados. También se implementó una lógica para eliminar las balas de la lista una vez que salen de la pantalla, optimizando el rendimiento.
4.  **Sonido**: Se utilizó el módulo `pygame.mixer` para cargar un archivo de sonido al inicio del programa. El sonido se reproduce una sola vez cada vez que se crea una nueva bala.

## Inconvenientes y Soluciones

*   **Inconveniente 1**: El principal problema fue un `AttributeError: 'list' object has no attribute 'y'`. Esto ocurría porque el código intentaba modificar la coordenada `y` de la lista de balas (`balas.y -= 10`), en lugar de la de una bala individual.

*   **Solución 1**: Se cambió la estructura de datos. Al hacer que cada bala sea una tupla que contiene su propio rectángulo y su dirección de movimiento, pudimos separar la lógica. El bucle principal ahora puede iterar sobre cada bala, acceder a su rectángulo individual y moverlo en la dirección que le corresponde, solucionando el error y permitiendo que múltiples balas se muevan independientemente.

*   **Inconveniente 2**: El sonido del disparo se reproducía continuamente en un bucle, causando un ruido constante en lugar de un efecto de sonido por disparo.

*   **Solución 2**: Se movió la llamada `sonido_disparo.play()` al bloque de evento `KEYDOWN` donde se crea la bala. De esta manera, el sonido se activa una sola vez por cada pulsación de la tecla de disparo, sincronizándose perfectamente con la acción.