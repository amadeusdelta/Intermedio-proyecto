import random
import functions
from pynput import keyboard

#Variable global que almacena la tecla presionada
tecla_presionada = None

#función que se llama una vez la tecla fue presionada
def on_press(key):
    global tecla_presionada
    tecla_presionada == None
    direccionales = [keyboard.Key.left, keyboard.Key.right, keyboard.Key.up, keyboard.Key.down]
    if tecla in direccionales:
        # obtiene la tecla presionada
        dirección = str(key).split('.')[-1]  
        tecla = f'{dirección}'
        # detiene el listener una vez que se presiono una vez una tecla
        return False  

score = 0
max_value = 0
tablero = [[0]*4] + [[0]*4] + [[0]*4] + [[0]*4]


print("\n\t---Bienvenido al juego 2048---\n")
op = int(input("1 - Iniciar\n2 - Como se juega? \n3 - Salir\nIngrese la opcion que desea...\t"))
if op == 2:
    print("\nUsa las WASD para mover las fichas. Cuando hay dos fichas juntas con el mismo número, se convierte en una.\n")

nombre = input("Ingresa tu nombre...\t")


# Agregar dos números iniciales aleatorios
contador = 0
while contador < 2:
    fila = random.randint(0, 3)
    columna = random.randint(0, 3)
    if tablero[fila][columna] == 0:
        tablero[fila][columna] = random.choice([2,4])
        contador += 1

testing.print_tablero(tablero)


while True:
        # Set up the listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()            

    if tablero != testing.mover_tablero(tecla_presionada,tablero)[0]:
        tablero,score,max_value= testing.mover_tablero(tecla_presionada,tablero,score,max_value)
        testing.print_tablero(tablero)
        print(score)
        if max_value<128:
            valores_random = [2,4]
        elif max_value<512:
            valores_random = [4,8]
        elif max_value<1024:
            valores_random = [8,16]
        else:
            valores_random = [16,32]

        if max_value == 4096:
            print("Ganaste! ")
            break
        
        #Determina si se puede continuar o no el juego
        if testing.continuar(tablero):
            while True:
                #Escoge una posición aleatoria en la que agregar un nuevo número
                fila = random.randint(0, 3)
                columna = random.randint(0, 3)
                if tablero[fila][columna] == 0:
                    tablero[fila][columna] = random.choice(valores_random)
                    break
        else:
            print("Perdiste! :(")
    else:
        print("No paso nada")
        continue    
