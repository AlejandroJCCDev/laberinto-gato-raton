"""
Lab: Laberinto del Gato y el Ratón
Simulador de persecución usando Minimax en Python
"""

import random

# Parámetros principales
ANCHO = 8
ALTO = 8
MAX_TURNOS = 20

POS_INICIAL_RATON = (ALTO - 1, ANCHO - 1)
POS_INICIAL_GATO = (0, 0)

# --- Tablero y visualización ---
def crear_tablero(ancho, alto):
    return [['.' for _ in range(ancho)] for _ in range(alto)]

def mostrar_tablero(tablero, pos_raton, pos_gato):
    for fila in range(ALTO):
        linea = ""
        for columna in range(ANCHO):
            if (fila, columna) == pos_raton and (fila, columna) == pos_gato:
                linea += "💥 "
            elif (fila, columna) == pos_raton:
                linea += "🐭 "
            elif (fila, columna) == pos_gato:
                linea += "🐱 "
            else:
                linea += ". "
        print(linea)
    print()


def movimientos_validos(posicion):
    fila, col = posicion
    opciones = []
    for df, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nf, nc = fila + df, col + dc
        if 0 <= nf < ALTO and 0 <= nc < ANCHO:
            opciones.append((nf, nc))
    return opciones

def mover_raton_aleatorio(pos_raton):
    opciones = movimientos_validos(pos_raton)
    return random.choice(opciones)

def mover_manual(posicion, personaje):
    teclas = {'w': (-1,0), 's': (1,0), 'a': (0,-1), 'd': (0,1)}
    while True:
        mensaje = f"Movimiento del {personaje} (w/a/s/d): "
        tecla = input(mensaje).lower()
        if tecla in teclas:
            df, dc = teclas[tecla]
            nf, nc = posicion[0] + df, posicion[1] + dc
            if 0 <= nf < ALTO and 0 <= nc < ANCHO:
                return (nf, nc)
        print("Movimiento inválido. Usa solo w/a/s/d y no salgas del tablero.")

def juego_terminado(pos_raton, pos_gato, turno):
    if pos_raton == pos_gato:
        print("💀 ¡El gato atrapó al ratón! Fin del juego.")
        return True
    if turno >= MAX_TURNOS:
        print("🎉 ¡El ratón escapó durante 20 turnos!")
        return True
    return False

# --- Algoritmo principal de juego ---
def jugar():
    tablero = crear_tablero(ANCHO, ALTO)
    pos_raton = POS_INICIAL_RATON
    pos_gato = POS_INICIAL_GATO

  
    while True:
        eleccion = input("¿Quieres controlar al gato o al ratón? (gato/raton): ").strip().lower()
        if eleccion in ["gato", "raton"]:
            break
        print("Por favor, escribe 'gato' o 'raton'.")

    for turno in range(1, MAX_TURNOS + 1):
        print(f"\nTurno {turno}")
        mostrar_tablero(tablero, pos_raton, pos_gato)

        # Movimiento del gato
        if eleccion == "gato":
            pos_gato = mover_manual(pos_gato, "gato")
        else:
            _, pos_gato = minimax_gato(pos_gato, pos_raton, 2)
        if juego_terminado(pos_raton, pos_gato, turno):
            break

        
        if turno == 1:
            pos_raton = mover_raton_aleatorio(pos_raton)
        else:
            if eleccion == "raton":
                pos_raton = mover_manual(pos_raton, "ratón")
            else:
                _, pos_raton = minimax_raton(pos_raton, pos_gato, 2)
        if juego_terminado(pos_raton, pos_gato, turno):
            break

# --- Algoritmo Minimax 
def minimax_raton(pos_raton, pos_gato, profundidad):
    if pos_raton == pos_gato:
        return -1000, pos_raton
    if profundidad == 0:
        distancia = abs(pos_raton[0] - pos_gato[0]) + abs(pos_raton[1] - pos_gato[1])
        return distancia, pos_raton
    mejor_valor = float('-inf')
    mejor_movimiento = pos_raton
    for nueva_pos in movimientos_validos(pos_raton):
        posibles_gato = movimientos_validos(pos_gato)
        if posibles_gato:
            nueva_pos_gato = random.choice(posibles_gato)
        else:
            nueva_pos_gato = pos_gato
        valor, _ = minimax_raton(nueva_pos, nueva_pos_gato, profundidad - 1)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = nueva_pos
    return mejor_valor, mejor_movimiento


def minimax_gato(pos_gato, pos_raton, profundidad):
    if pos_gato == pos_raton:
        return 1000, pos_gato
    if profundidad == 0:
        distancia = abs(pos_gato[0] - pos_raton[0]) + abs(pos_gato[1] - pos_raton[1])
        return -distancia, pos_gato
    mejor_valor = float('-inf')
    mejor_movimiento = pos_gato
    for nueva_pos in movimientos_validos(pos_gato):
        if nueva_pos == pos_raton:
            return 1000, nueva_pos
        posibles_raton = movimientos_validos(pos_raton)
        if posibles_raton:
            _, nueva_pos_raton = minimax_raton(pos_raton, nueva_pos, profundidad - 1)
        else:
            nueva_pos_raton = pos_raton
        valor, _ = minimax_gato(nueva_pos, nueva_pos_raton, profundidad - 1)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = nueva_pos
    return mejor_valor, mejor_movimiento

if __name__ == "__main__":

    jugar()
