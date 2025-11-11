# Práctica 1: Movimiento Básico y Límites de Pantalla (finalizado)

## Descripción

El objetivo de esta práctica era crear una ventana con Pygame y permitir que un cuadrado (el jugador) se moviera por la pantalla utilizando las flechas del teclado. Además, se implementó una mecánica para aumentar la velocidad y se aseguró que el jugador no pudiera salirse de los límites de la ventana.

## Cambios Realizados

1.  **Movimiento del Jugador**: Se utilizó `pygame.key.get_pressed()` dentro del bucle principal para detectar qué teclas de flecha están siendo presionadas en cada fotograma y actualizar las coordenadas `x` e `y` del jugador.
2.  **Aumento de Velocidad**: Se añadió una condición que verifica si la tecla `Shift` (izquierda o derecha) está presionada. Si es así, la variable `vel` aumenta, haciendo que el personaje se mueva más rápido. Cuando se suelta, la velocidad vuelve a su valor normal.
3.  **Límites de la Ventana**: Se implementaron condicionales `if` para comprobar la posición del jugador. Si el cuadrado intenta moverse más allá de los bordes (izquierdo, derecho, superior o inferior), su posición se ajusta para mantenerlo exactamente en el borde, impidiendo que se salga.

## Inconvenientes y Soluciones

*   **Inconveniente**: El principal desafío fue evitar que el cuadrado desapareciera de la pantalla al moverse hacia los bordes. El intento inicial de código para lograr esto no era funcional y tenía errores de sintaxis.

*   **Solución**: Se descartó el código inicial y se implementó una lógica de "colisión con los bordes" directamente en el bucle principal. Se crearon cuatro condiciones separadas, una para cada borde de la pantalla (0 en los ejes `x` e `y`, y el ancho/alto de la pantalla menos el tamaño del cuadrado). Esta solución es simple, eficiente y mantiene al jugador visible en todo momento.