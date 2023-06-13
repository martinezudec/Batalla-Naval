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

#función de validación
def read_validate(m,M,txt):
    val=int(input(txt))
    while val<m or val>M:
        print(f'Error, el valor debe estar entre {m} y {M}')
        val=int(input(txt))
    return val

# Inicializar Variables
sea=[[]]
sea_size=read_validate(10,26,'tamaño del tabelero= ')
ships_num=sea_size
game_over=False
sunk_ships=0
ship_pos=[[]]
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ship_placement_validation(start_row,end_row,start_col,end_col):
    #verificará si es segura la colocación de un barco en esa posición
    #devolverá True o False

    global sea
    global ship_pos
    # verificar si las casillas son validas
    all_valid=True
    for i in range(start_row,end_row):
        for a in range(start_col,end_col):
            if sea[i][a]!="^":
                all_valid=False
                break
    #si son validas permite crear un barco
    if all_valid:
        ship_pos.append([start_row,end_row,start_col,end_col])
        for i in range(start_row,end_row):
            for a in range(start_col,end_col):
                sea[i][a]="O"
    return all_valid

def place_ship_in_sea(row,col,direction,lenght):
    #dependiendo de la dirección llamará a ship_placement_validation antes de colocar un barco
    global sea_size

    start_row,end_row,start_col,end_col=row,row+1,col,col+1
    if direction=="left":
        if col-lenght<0:
            return False
        start_col=col-lenght+1

    elif direction=="right":
        if col+lenght>=sea_size:
            return False
        end_col=col+lenght
    elif direction=="up":
        if row-lenght<0:
            return False
        start_row=row-lenght+1
    elif direction=="down":
        if row+lenght>=sea_size:
            return False
        end_row=row+lenght

    return ship_placement_validation(start_row,end_row,start_col,end_col)

def create_sea():
    #creará un mar del tamaño especificado y colocará barcos en diferentes direcciones.

    global sea
    global sea_size
    global ships_num
    global ship_pos

    random.seed(time.time())
    rows,cols=(sea_size,sea_size)
    #creación del mar
    sea=[]
    for i in range(rows):
        row=[]
        for a in range(cols):
            row.append("^")
        sea.append(row)

    ships_num_placed=0

    ship_pos=[]
    
    while ships_num_placed !=ships_num:
        random_row=random.randint(0,rows-1)
        random_col=random.randint(0,cols-1)
        direction=random.choice(["left","right","up","down"])
        ship_size=3
        if place_ship_in_sea(random_row,random_col,direction,ship_size):
            ships_num_placed+=1

def print_sea():
    #desplegará el océano
    global sea
    global alphabet
    
    debug_mode=True #modo de pruebas para testear el juego, cuando está apagado no se ven los barcos enemigos

    alphabet=alphabet[0:len(sea)+1] #ajustando el largo del abecedario a el largo del tablero
    
    for row in range(len(sea)):
        print(alphabet[row],end=")")
        for col in range(len(sea[row])):
            if sea[row][col]=="O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print ("^", end=" ")
            print("")

def bullet_coord_validation():
    #valida las coordenadas en la que se quiere lanzar el disparo
    global sea
    global alphabet

    valid_shot=False
    row=-1
    col=-1
    while valid_shot is False:
        placement=input("Ingrese una fila y una columna para disparar de la manera 'A1': ")
        placement= placement.upper()
        if len(placement)<=0 or len(placement)>2:
            print("Error, ingrese coordenadas de la manera 'A1' ")
            continue
        row=placement[0]
        col=placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error, ingrese coordenadas de la manera 'A1' ")
            continue
        row=alphabet.find(row)
        if not (-1<row<sea_size):
            print("Error, ingrese coordenadas de la manera 'A1' ")
            continue
        col=int(col)
        if not (-1<col<sea_size):
            print("Error, ingrese coordenadas de la manera 'A1' ")
            continue
        if sea[row][col]=="/" or sea[row][col]=="X":
            print("Ya disparaste en esta zona, escoge otras coordenadas")
            continue
        if sea[row][col]=="^" or sea[row][col]=="O":
            valid_shot=True

    return row,col

def check_sunk_ship(row,col):
    #si todas las partes del barco recibieron disparos, el barco está hundido
    #devuelve True o Flase
    global ship_pos
    global sea

    for position in ship_pos:
        start_row=position[0]
        end_row=position[1]
        start_col=position[2]
        end_col=position[3]
        if start_row<=row<=end_row and start_col<=col<=end_col:
            #chequea si está hundido completamente
            for i in range(start_row,end_row):
                for a in range(start_col,end_col):
                    if sea[r][c]!="X":
                        return False
    return True

def shoots():
    #actualiza el mar dependiendo de donde se ha disparado
    global sea
    global sunk_ships
    
    row,col=bullet_coord_validation()
    print("")
    print("----------------------------")
    
    if sea[row][col]=="^":
        print("Disparo al agua!")
        sea[row][col]="/"
    elif sea[row][col]

def game_over_check():
    #si todos los barcos han sido hundidos el juego se acaba
    global sunk_ships
    global ships_num
    global game_over


def main():
    #inicia el loop del juego 
    global game_over

    pass

if __name__ == '__main__':
    '''solo se pedirá cuando el programa corra a través de terminal o IDE'''

    main()