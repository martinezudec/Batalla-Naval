import os
try:
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
        while True:  
            val=input(txt)
            if not val.isnumeric():
                print("Error, el valor debe ser un número entero.")
                continue
            val = int(val)

            if val<m or val>M:
                print(f'Error, el valor debe estar entre {m} y {M}')
                continue

            break

        return val

    # Inicializar Variables
    sea=[[]]
    sea_size=read_validate(10,26,'tamaño del tablero: ')
    ships_num = read_validate(3, sea_size, "ingrese número de barcos: ")

    print("sea_size: " + str(sea_size))
    print("sea_size: " + str(ships_num))

    game_over=False
    sunk_ships=0
    ship_pos=[[]]
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def ship_placement_validation(start_row, start_column):
        #verificará si es seguro poner un barco en esa posición
        #devolverá True o False
        global sea
        global ship_pos
        # verificar si las casillas son validas
        

    def place_ship_in_sea(row, column, direction):
        #dependiendo de la dirección llamará a ship_placement_validation antes de colocar un barco
        global sea_size
        global ship_pos

        start_row = row
        end_row = row
        start_column = column
        end_column = column
        
        if direction == "horizontal":
            if column - 2 < 0:
                return False
            start_column = column - 2
            end_column = column

        elif direction == "vertical":
            if row - 2 < 0:
                return False
            start_row = row - 2
            end_row = row

        all_valid=True
        # ver que el index en sea exista
        for i in range(start_row, end_row + 1):
            for a in range(start_column, end_column + 1):
                if i >= len(sea) or a >= len(sea[i]):
                    all_valid = False
                    break
                if sea[i][a] != "^":
                    all_valid = False
                    break
            

        # crear barco si las coordenadas son validas
        if all_valid:
            
            for i in range(start_row, end_row + 1):
                for a in range(start_column, end_column + 1):
                    sea[i][a]="O"
                    
        return all_valid

        # return ship_placement_validation(start_row, start_column)

    def create_sea():
        #creará un mar del tamaño especificado y columnocará barcos en diferentes direcciones.
        global sea
        global sea_size
        global ships_num
        

        random.seed(time.time())
        
        rows = sea_size
        columns = sea_size

        #creación del mar
        sea=[]

        for i in range(rows):
            row=[]
            for a in range(columns):
                row.append("^")
            sea.append(row)

        # crear barcos
        ships_num_placed = 0

        while ships_num_placed != ships_num:

            random_row = random.randint(0, rows -1 )
            random_column = random.randint(0, columns - 1)
            direction = random.choice(["horizontal", "vertical"])
            
            if place_ship_in_sea(random_row, random_column, direction):
                ships_num_placed += 1

    def print_sea():
        #desplegará el océano
        global sea
        global alphabet
        
        debug_mode = True #modo de pruebas para testear el juego, cuando está apagado no se ven los barcos enemigos

        alphabet = alphabet[0:len(sea) + 1] #ajustando el largo del abecedario a el largo del tablero
        
        def incrementar_letra(letra):
            return chr(ord(letra)+1) 

        space = "   "
        for row in range(len(sea)):
            print(alphabet[row], end=")")
            for column in range(len(sea[row])):
                if sea[row][column]=="O":
                    if debug_mode:
                        print(space + "O", end="")
                    else:
                        print (space + "^", end="")
                else:
                    print(space + sea[row][column], end="")
            print("\n  " + "----"*len(sea[row]))  
    
        string = "  "
        for i in range(len(sea[0])):
            if i < 10:
                string = string + space + str(i + 1) 
            else:
                string = string + "  " + str(i + 1)
        print(string)
            
    def bullet_coord_validation():
        #valida las coordenadas en la que se quiere lanzar el disparo
        global sea
        global alphabet

        valid_shot=False
        row =- 1
        column =- 1

        while valid_shot is False:
            placement=input("Ingrese una fila y una columnumna para disparar de la manera 'A1': ")
            placement= placement.upper()
            if len(placement)<=0 or len(placement)>2:
                print("Error, ingrese coordenadas de la manera 'A1' ")
                continue
            row=placement[0]
            column=placement[1]
            if not row.isalpha() or not column.isnumeric():
                print("Error, ingrese coordenadas de la manera 'A1' ")
                continue
            row=alphabet.find(row)
            if not (-1<row<sea_size):
                print("Error, ingrese coordenadas de la manera 'A1' ")
                continue
            column=int(column) - 1
            if not (-1<column<sea_size):
                print("Error, ingrese coordenadas de la manera 'A1' ")
                continue
            if sea[row][column]=="/" or sea[row][column]=="X":
                print("Ya disparaste en esta zona, escoge otras coordenadas")
                continue
            if sea[row][column]=="^" or sea[row][column]=="O":
                valid_shot=True

        return row,column

    def check_sunk_ship(row,column):
        #si todas las partes del barco recibieron disparos, el barco está hundido
        #devuelve True o Flase
        global ship_pos
        global sea

        for position in ship_pos:
            start_row=position[0]
            end_row=position[1]
            start_column=position[2]
            end_column=position[3]
            if start_row<=row<=end_row and start_column<=column<=end_column:
                #chequea si está hundido completamente
                for i in range(start_row,end_row):
                    for a in range(start_column,end_column):
                        if sea[i][a]!="X":
                            return False
        return True

    def shoots():
        #actualiza el mar dependiendo de donde se ha disparado
        global sea
        global sunk_ships
        
        row,column=bullet_coord_validation()
        print("")
        print("----------------------------")
        
        if sea[row][column]=="^":
            print("Disparo al agua!")
            sea[row][column]="/"
        elif sea[row][column]=="O":
            print("Le has dado!", end=" ")
            sea[row][column]="X"
            if check_sunk_ship(row,column):
                print("Has hundido un barco!")
                sunk_ships+=1
            else:
                print("Le has dado a un barco!")

    def game_over_check():
        #si todos los barcos han sido hundidos el juego se acaba
        global sunk_ships
        global ships_num
        global game_over

        if ships_num==sunk_ships:
            print("Felicidades, has ganado!")
            game_over=True

    def main():
        #inicia el loop del juego 
        global game_over

        print("-----Batalla Naval-----")
        print("Profe porfa denos un 7.0")
        
        create_sea()
        
        while game_over is False:
            print_sea()
            print("Barcos restantes: "+str(ships_num-sunk_ships))
            shoots()
            print("----------------------------")
            print("")
            game_over_check()
            
    if __name__ == '__main__':
        '''solo se pedirá cuando el programa corra a través de terminal o IDE'''

        main()

except Exception as e:
    raise(e)
    os.system("pause")