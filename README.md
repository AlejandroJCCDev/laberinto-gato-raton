# Laberinto del Gato y el Ratón

Simulador inteligente de persecución usando el algoritmo Minimax en Python puro.

---

## ¿Qué es este proyecto?

Un juego donde el ratón y el gato se enfrentan en un tablero bidimensional. El objetivo del ratón es escapar, mientras que el gato intenta atraparlo. Ambos evolucionan: primero se mueven de forma simple, luego aplican estrategias inteligentes con el algoritmo Minimax.

---

## Estructura del proyecto

- **`minimax_lab.py`**: Código principal del juego.
- **`README.md`**: Explicación del reto, proceso, aprendizajes y cómo ejecutar el juego.

---

## Proceso y funcionamiento

- El tablero es una matriz bidimensional (lista de listas).
- El ratón comienza moviéndose aleatoriamente en el primer turno, luego evoluciona a usar Minimax para buscar rutas de escape.
- El gato también evoluciona: primero usa movimiento simple, luego usa Minimax para predecir y acorralar al ratón.
- El juego termina si el gato atrapa al ratón o si el ratón escapa tras X turnos.

---

## "Aha Moments" y aprendizajes

Durante el desarrollo aprendí y enfrenté varios retos interesantes:

- **Minimax & Evaluaciones**: El mayor reto fue lograr que el gato realmente persiguiera al ratón. Al principio, la función de evaluación hacía que el gato se alejara, pero ajustando la lógica (minimizar distancia), logré que lo persiguiera correctamente.
- **Control de profundidad y eficiencia**: Aprendí la importancia de limitar la profundidad del algoritmo para evitar bucles infinitos y mantener el juego fluido.
- **Variación de comportamiento**: Implementé que el ratón haga su primer movimiento aleatorio y luego evolucione a Minimax, cumpliendo con el reto de simular una "mente brillante".
- **Balance de dificultad**: Ajustar la dificultad y la eficiencia del juego fue clave para que ambos jugadores (gato y ratón) tengan oportunidad de ganar.
- **Interfaz y jugabilidad**: Mejoré la lógica para que el usuario pueda elegir qué personaje controlar y la visualización del tablero para mayor claridad.
- **Iteración y testing**: Realicé pruebas con diferentes tamaños de tablero y situaciones, lo que ayudó a pulir la lógica y entender mejor el algoritmo Minimax.

---

## Problemas enfrentados y cómo los resolví

- **Minimax demasiado lento/ineficiente**: Reduje la profundidad y optimicé los movimientos válidos.
- **Condiciones de parada poco claras**: Definí claramente los casos de fin del juego para evitar bucles.
- **Errores en la visualización**: Ajusté varias veces cómo se imprime el tablero para que sea entendible y útil.

---

## Cómo ejecutar el juego

1. **Instala Python 3** si aún no lo tienes.
2. Descarga los archivos del proyecto.
3. Ejecuta el juego en consola con:

   ```bash
   python minimax_lab.py
   ```

---

## Bonus opcionales

Si tienes tiempo o quieres experimentar, puedes agregar:
- Obstáculos en el tablero.
- Objetivo “queso” para el ratón.
- Visualización mejorada del tablero en consola.
- Elegir quién quieres ser (gato o ratón).

---

## Reflexión final

Este proyecto me ayudó a entender en profundidad el algoritmo Minimax y cómo aplicar estrategias de decisión en juegos. Aprendí no solo a programar la lógica, sino también a pensar en eficiencia, jugabilidad y cómo explicar el código para otros ademas de seguir practicando este tipos de proyectos.

¡Diviértete y aprende estrategia con Python!
