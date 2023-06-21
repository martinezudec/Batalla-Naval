import os, random, time, math
os.system("cls")
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

debug_mode=False

#función de validación
def read_validate(m,M,txt):
    while True:  
        val=input(txt)
        if not val.isnumeric():
            print("Error, el valor debe ser un número entero positivo.")
            continue
        val = int(val)

        if val<m or val>M:
            print(f'Error, el valor debe estar entre {m} y {M}')
            continue

        break

    return val

input("""
                -----BATALLA NAVAL-----
       _           _   _   _           _     _       
      | |         | | | | | |         | |   (_)      
      | |__   __ _| |_| |_| | ___  ___| |__  _ _ __  
      | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
      | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
      |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                            | |    
                                            |_| 

           ---PRESIONA ENTER PARA COMENZAR---
                                            """)

# Inicializar Variables
sea=[]
sea_size=read_validate(10, 1000, 'tamaño del tablero: ')
ships_num = read_validate(3, sea_size, "Ingrese número de barcos: ")
ship_position=[]
sunk_ships = 0
user_sea = []
user_ship_position = []
user_sunk_ships = 0



game_over=False



def place_ship_in_sea(row, column, direction, arr, ship_pos, User):
    #dependiendo de la dirección llamará a ship_placement_validation antes de colocar un barco
    global sea_size

    start_row = row
    end_row = row
    start_column = column
    end_column = column
    
    if direction == "horizontal":
        if column < 0 and column + 2 >= sea_size:
            return False
        start_column = column -1
        end_column = column + 1

    elif direction == "vertical":
        if row < 0 and row + 2 >= sea_size:
            return False
        start_row = row -1
        end_row = row + 1

    all_valid=True
    # ver que el index en sea exista
    for i in range(start_row, end_row + 1):
        for a in range(start_column, end_column + 1):
            if i >= len(arr) or a >= len(arr[i]) or a<0 or i<0:
                all_valid = False
                if User:
                    print("Barco fuera de rango")
                break
            if arr[i][a] != "^":
                all_valid = False
                if User:
                    print("No se puede colocar un barco aquí")
                break
        

    # crear barco si las coordenadas son validas
    if all_valid:
        ship_pos.append([start_row, end_row, start_column, end_column])
        
        for i in range(start_row, end_row + 1):
            for a in range(start_column, end_column + 1):
                arr[i][a]="O"
                
    return all_valid

    # return ship_placement_validation(start_row, start_column)


def create_sea(arr, ship_pos, randomize):
    #creará un mar del tamaño especificado y columnocará barcos en diferentes direcciones.
    global sea_size
    global ships_num
    random.seed(time.time())

    
    #creación del mar
    for i in range(sea_size):
        row=[]
        for j in range(sea_size):
            row.append("^")
        
        arr.append(row)

    # crear barcos
    ships_num_placed = 0

    while ships_num_placed != ships_num:
                
        if randomize:
            row = random.randint(0, sea_size - 1 )
            column = random.randint(0, sea_size - 1)
            direction = random.choice(["horizontal", "vertical"])

            if place_ship_in_sea(row, column, direction, arr,  ship_pos, False):
                ships_num_placed += 1
            

        else:
            direction = input("Direccion del barco, vertical o horizontal (V/H): ").lower()
            
            while direction != "v" and direction != "h":
                direction = input("Valor invalido. Ingresar vertical o horizontal de la forma V o H: ").lower()
            
            if direction == "v":
                direction = "vertical"
            elif direction == "h":
                direction = "horizontal"

        # falta verificar entrada /////////////////////////////////////////////////////////////////////////////////////////////////
            row = int(input("Ingrese fila del barco: ")) - 1
            column = int(input("Ingrese columna del barco: ")) - 1
            
            if place_ship_in_sea(row, column, direction, arr,  ship_pos, True):
                ships_num_placed += 1
                print_sea(arr)
                
def print_sea(arr):
    #desplegará el océano
    
    global debug_mode #modo de pruebas para testear el juego, cuando está apagado no se ven los barcos enemigos
       
    os.system("cls")
    for row in range(len(arr)): 
        space = 10**row  
        
        if row + 1 < 10:
            string_r = str(row + 1) + ") "
        else:
            string_r = str(row + 1) + ")"

        for column in range(len(arr[row])):
            if arr[row][column]=="O":
                if arr == user_sea:
                    string_r = string_r + "   " + "O"
                else:
                    if debug_mode and arr == sea:
                        string_r = string_r + "   " + "O"
                    else:
                        string_r = string_r + "   " + "^"
            else:
                string_r = string_r + "   " + arr[row][column]

        print(string_r)
        print("   " + "----"*len(arr[row]))  

    string_c = "   "
    for i in range(len(arr[0])):    

        if i < 10:
            string_c = string_c + "   " + str(i + 1) 
        else:
            string_c = string_c + "  " + str(i + 1)
            
    print(string_c)
        
def bullet_coord_validation():
    #valida las coordenadas en la que se quiere lanzar el disparo
    global sea
    global alphabet

    valid_shot=False    
    while valid_shot is False:

        while True:
            row = input("Ingrese una fila para disparar: ")

            if not row.isnumeric(): # revisar que sean letra y número
                print("Error, ingrese el número de fila a disparar")
                continue
            
            row = int(row) - 1
            if not (-1 < row < sea_size):
                print("Error, La fila no esta dentro del rango del tablero. ")
                continue
            
            break

        while True: 
            column = input("Ingrese una columna para disparar: ")

            if not column.isnumeric():
                print("Error, ingrese número de la columna a disparar")
                continue

            column = int(column) - 1
            if not (-1 < column < sea_size):
                print("Error, la columna no esta dentro del rango del tablero")
                continue
            
            break

        if sea[row][column] == "/" or sea[row][column] == "X":
            print("Ya disparaste en esta zona, escoge otras coordenadas")
            continue
        
        if sea[row][column] == "^" or sea[row][column] == "O":
            valid_shot=True

    return row, column

def check_sunk_ship(row, column, ship_pos, board):
    #si todas las partes del barco recibieron disparos, el barco está hundido
    #devuelve True o Flase
    

    for ship in ship_pos:

        start_row = ship[0]
        end_row = ship[1]
        start_column = ship[2]
        end_column = ship[3]

        if start_row <= row <= end_row and start_column <= column <= end_column:
            # ve si el barco ha recibido tres disparos
            for i in range(start_row, end_row + 1):
                for a in range(start_column, end_column + 1):
                    if board[i][a]!="X":
                        return False

    return True

def computer_shot():
    global user_ship_position
    global user_sea
    random.seed(time.time())

    
    while True:
        row = random.randint(0, sea_size - 1 )
        column = random.randint(0, sea_size - 1)
      
        if user_sea[row][column] == "/" or user_sea[row][column] == "X":
            continue
        
        if user_sea[row][column] == "^" or user_sea[row][column] == "O":
            break
    
   
    if user_sea[row][column] == "^":
        os.system("cls")
        print(f"\n\n\n Disparo al agua por parte de tu enemigo en ({row + 1}, {column + 1}), tus barcos estan a salvo.")
        user_sea[row][column]="/"
        time.sleep(2)

    elif user_sea[row][column] == "O":
        os.system("cls")

        if check_sunk_ship(row, column, user_ship_position, user_sea):
            print(f"¡¡¡¡Tu barco ha sido hundido!!!!")
            user_sunk_ships += 1

        else:
            print(f"\n\n\n Le han disparado a tu barco en ({row + 1}, {column + 1})!")

        user_sea[row][column]="X"
        time.sleep(2)

    
def shoots():
    #actualiza el mar dependiendo de donde se ha disparado
    global sea
    global sunk_ships
    global ship_position
    
    row, column = bullet_coord_validation()
    print("")
    print("----------------------------")
    
    if sea[row][column] == "^":
        os.system("cls")
        print("\n\n\nDISPARO AL AGUA!")
        sea[row][column]="/"
        time.sleep(2)

    elif sea[row][column] == "O":
        os.system("cls")
        print("\n\n\nLe has dado!")
        sea[row][column]="X"

        if check_sunk_ship(row,column, ship_position, sea):
            print("\n\n\nHas hundido un barco!")
            sunk_ships += 1

        else:
            print("\n\n\nLe has dado a un barco!")

        time.sleep(2)

def game_over_check():
    #si todos los barcos han sido hundidos el juego se acaba
    global sunk_ships
    global ships_num
    global user_sunk_ships
    global game_over

    if ships_num == sunk_ships:
        game_over=True
        win=True
    elif ships_num == user_sunk_ships:
        game_over=True
        win=False


def main():
    #inicia el loop del juego 
    global game_over
    
    create_sea(sea, ship_position, True)
    print_sea(sea)
    print("--------------------------------------------------------------------------------")
    create_sea(user_sea, user_ship_position, False)
    print_sea(user_sea)
    input("Presiona una Enter para continuar...")
    
    turn = 1
    while game_over is False:

        if turn % 2 != 0: # primero turno usuario
            os.system("cls")
            print("__________________________________\n         tablero enemigo\n__________________________________")
            print_sea(sea)
            print("Barcos restantes: " + str(ships_num - sunk_ships))
            shoots()

            print("__________________________________\n         tablero enemigo\n__________________________________")
            print_sea(sea)
            input("Presiona una Enter para continuar...")

        else: # turno computador        
            os.system("cls")
            print("__________________________________\n         turno del computador\n__________________________________")
            print(user_sea)
            print("Barcos restantes: " + str(ships_num - sunk_ships))
            computer_shot()
            print("__________________________________\n         tu tablero\n__________________________________")
            print_sea(user_sea)
            input("Presiona una Enter para continuar...")
            
        
        game_over_check()
        turn += 1   
            
main()
os.system("cls")
if win:
    print("""Felicidades, has ganado!
                   |    |    |                 
                  )_)  )_)  )_)              
                 )___))___))___)\            
                )____)____)_____)\\
              _____|____|____|____\\\__
     ---------\                   /---------
       ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
         ^^^^      ^^^^     ^^^    ^^
              ^^^^      ^^^
         """)
else:
    print("""Derrota. Han hundido todos tus barcos
                   |    |    |                 
                  )_)  )_)  )_)              
                 )___))___))___)\            
                )____)____)_____)\\
              _____|____|____|____\\\__
     ---------\                   /---------
       ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
         ^^^^      ^^^^     ^^^    ^^
              ^^^^      ^^^
         """)