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

    ->Cada una de estas entradas deben ser validadas o en el caso de la informaci ́on de las naves y coordenadas de
    los disparos se deben ajustar al tamaño del tablero. En el caso que los valores no est ́en dentro de los rangos
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
