# Práctica 2: Gravedad y Doble Salto (finalizado)


## Descripción

En esta práctica se introdujeron conceptos de física simple. El objetivo era hacer que un cuadrado fuera afectado por la gravedad, pudiera saltar para contrarrestarla y, finalmente, tuviera la habilidad de realizar un segundo salto en el aire (doble salto). También se añadió un suelo visible.

## Cambios Realizados

1.  **Gravedad**: Se creó una variable `gravedad` que se suma a la velocidad vertical (`vel_y`) en cada fotograma, simulando una aceleración constante hacia abajo.
2.  **Salto Simple**: La lógica del salto se movió al bucle de eventos (`pygame.KEYDOWN`). Al presionar la barra espaciadora, se le da a `vel_y` un valor negativo, impulsando al jugador hacia arriba.
3.  **Doble Salto**: Para permitir un segundo salto, se introdujo una variable `saltos_hechos`. Esta variable cuenta cuántas veces se ha saltado. Solo se permite un salto si `saltos_hechos` es menor que 2.
4.  **Suelo**: Se definió un `pygame.Rect` para representar el suelo y se dibujó en la pantalla. Cuando el jugador aterriza (su coordenada `y` alcanza la posición del suelo), su velocidad vertical se detiene y el contador `saltos_hechos` se reinicia a cero.

## Inconvenientes y Soluciones

*   **Inconveniente 1**: Inicialmente, el salto se registraba mientras la tecla espacio estuviera presionada, lo que podía causar un comportamiento no deseado. Además, solo se podía realizar un salto.

*   **Solución 1**: Se cambió la detección del salto de `pygame.key.get_pressed()` al bucle de eventos `if event.type == pygame.KEYDOWN`. Esto asegura que el salto se active solo una vez por cada pulsación. Para el doble salto, se implementó el contador `saltos_hechos`, que limita los saltos a dos antes de que sea necesario tocar el suelo de nuevo.

*   **Inconveniente 2**: El "suelo" era solo una coordenada invisible, lo que hacía difícil para el jugador saber dónde aterrizaría.

*   **Solución 2**: Se creó un objeto `pygame.Rect` para el suelo, con un color y posición definidos. Este rectángulo se dibuja en la pantalla en cada fotograma con `pygame.draw.rect()`, proporcionando una referencia visual clara.