import random
import time

"""
    Restricciones del juego:
    * Tablero de N x N (N >= 10).
    * Las filas y columnas del tablero se referenciarán usando números enteros mayores o iguales a 0.
    * El oponente será el computador, que generará su tablero y sus jugadas siguiendo las normas del juego y en
    forma aleatoria.
    * La cantidad de naves de cada jugador debe ser consultada al usuario del juego (debe ser 2 < x =< N).
    * Todas las naves serán buques de tamaño 3 casillas.

    Entradas:
    * Entero positivo N (10 =< N =< 1000) que indica tamaño del tablero y cantidad de barcos de cada jugador.
    * N pares de números y una letra (H o V) que especificará las coordenadas del punto central y la orientación
    (horizontal o vertical) de cada nave.
    * Especificar si parte jugando "Humano" o "Máquina".
    * A continuación, sucesivamente con el oponente (el computador) se deben ir ingresando (generando) pares de
    números que representan las coordenadas de los disparos. El programa debe indicar si se trata de un impacto o
    agua y debe generar los registros correspondientes.

    ->Cada una de estas entradas deben ser validadas o en el caso de la información de las naves y coordenadas de
    los disparos se deben ajustar al tamaño del tablero. En el caso que los valores no estén dentro de los rangos
    establecidos, se debe indicar el error y permitir un nuevo ingreso de datos.<-
    
    Salidas:
    Habrá sólo una salida del programa consistente en uno de los siguientes textos “Gana el humano” o “Gana la 
    máquina”.


    Simbología:
    "^" = agua
    "O" = barco
    "X" = impacto
    "/" = disparo fallido
""" 

# Inicializar Variables
sea=[[]]
sea_size=10
ships_num=3
game_over=False
sunk_ships=0
ship_pos=[[]]
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def read_validate(m,M,txt):
    val=int(input(txt))
    while val<m or val>M:
        print(f'Error, el valor debe estar entre {m} y {M}')
        val=int(input(txt))
    return val

def ship_placement_validation(start_row,end_row,start_col,end_col):
    #verificará si es segura la colocación de un barco en esa posición
    #devolverá True o False

    global sea
    global ship_pos

    pass

def place_ship_in_sea(row,col,direction,lenght):
    #dependiendo de la dirección llamará a ship_placement_validation antes de colocar un barco
    global sea_size

    pass

    return ship_placement_validation(0,0,0,0)

def create_sea():
    #creará un mar del tamaño especificado y colocará barcos en diferentes direcciones.

    global sea
    global sea_size
    global ships_num
    global ship_pos

    pass
    
    place_ship_in_sea(0,0,0,0)

def print_sea():
    #desplegará el océano
    global sea
    global alphabet
    
    pass

def bullet_coord_validation():
    #valida las coordenadas en la que se quiere lanzar el disparo
    global sea
    global alphabet

    pass

    return 0,0

def check_sunk_ship(row,col):
    #si todas las partes del barco recibieron disparos, el barco está hundido
    #devuelve True o Flase
    global ship_pos
    global sea

    pass

def shoots():
    #actualiza el mar dependiendo de donde se ha disparado
    global sea
    global sunk_ships
    
    row,col=bullet_coord_validation()

    pass

def game_over_check():
    #si todos los barcos han sido hundidos el juego se acaba
    global sunk_ships
    global ships_num
    global game_over

    pass

def main():
    #inicia el loop del juego 
    global game_over

    pass

if __name__ == '__main__':
    '''solo se pedirá cuando el programa corra a través de terminal o IDE'''

    main()