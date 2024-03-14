from copy import copy

def transponer_tablero(tablero):


    # Suponemos que el tablero es rectangular
    n = len(tablero[0])
    m = len(tablero)
    
    # Create a transposed matrix with distinct inner lists
    tablero_transpuesto = [[0] * m for _ in range(n)]
    # Recorre las filas
    for i in range(m):
        # Recorre las columnas
        for j in range(n):
            tablero_transpuesto[j][i] = tablero[i][j]
            print(tablero[i])
    return tablero_transpuesto

def print_tablero(tablero):
    print("\n")
    for fila in tablero:
        print("| ",end="\t")
        for elemento in fila:
            print(elemento, end="\t")
            
        print(" |")
    print("\n")
    

def mover_tablero(key, tablero,score=0,max_value=0):
    #Vamos a movernos hacia la izquierda
    match key:
        case "left":
            for k in range(len(tablero)):
                #This is the only case when two combinations may happen
                #When we have something like [a,a,b,b]
                if (len(set(tablero[k][0:2]))==1 and tablero[k][0] != 0) and (len(set(tablero[k][2:4]))==1  and tablero[k][2] != 0):
                    tablero[k] = [2*tablero[k][0],2*tablero[k][2],0,0]
                    continue
                #Intentaremos combinarlos primero, 
                #y luego rellenaremos los espacios vacíos
                #Comprueba si se ha producido una combinación
                flag = 0 
                for i in range(1,4):
                    if tablero[k][i] == 0:
                        continue
                    else:
                        for j in range(i):
                            if (tablero[k][i] == tablero[k][j]) and (flag == 0):
                                #Los elementos intermedios no pueden
                                #ser iguales, (a menos que sean cero) ya que
                                #caería en el otro caso.
                                if set(tablero[k][j+1:i]) in [{0},set()]:
                                    
                                    tablero[k][j] = copy(tablero[k][i]*2)
                                    tablero[k][i] = 0
                                    score += tablero[k][j]
                                    if max_value<tablero[k][j]:
                                        max_value = tablero[k][j]
                                    if tablero[k][j] in [512,1024,2048,4096]:
                                        print(f"Alcanzaste el {tablero[k][j]}")
                                    flag = 1
                                    break
                            else:
                                continue
                #Queremos rellenar los espacios vacíos
                for i in range(1,4):
                    #Obtiene el cero más cercano de nuestro elemento
                    try:
                        tablero[k][tablero[k][0:i].index(0)] = copy(tablero[k][i])
                        tablero[k][i] = 0
                    #Significa que no hay ningun espacio vacío al que recorrer
                    except:
                        continue
                        
        case "right":
            #Notemos que para este caso, fila por fila, moverse hacia la derecha es lo mismo que
            #Primero invertir la fila, hacer lo mismo que en el caso de movimiento a la izquierda
            #Y, finalmente invertir de vuelta
            for k in range(len(tablero)):
                fil_inv = copy(tablero[k][::-1])
                if (len(set(fil_inv[0:2]))==1 and fil_inv[0] != 0) and (len(set(fil_inv[2:4]))==1  and fil_inv[2] != 0):
                    fil_inv = [2*fil_inv[0],2*fil_inv[2],0,0]
                    tablero[k] = fil_inv[::-1]  
                    continue
                flag = 0 
                for i in range(1,4):
                    if fil_inv[i] == 0:
                        continue
                    else:
                        for j in range(i):
                            if (fil_inv[i] == fil_inv[j]) and (flag == 0):
                                if set(fil_inv[j+1:i]) in [{0},set()]:
                                    fil_inv[j] = copy(fil_inv[i]*2)
                                    fil_inv[i] = 0
                                    score += fil_inv[j]
                                    if max_value<fil_inv[j]:
                                        max_value = fil_inv[j]
                                    if fil_inv[j] in [512,1024,2048,4096]:
                                        print(f"Alcanzaste el {fil_inv[j]}")
                                    flag = 1
                                    break
                            else:
                                continue
                
                for i in range(1,4):

                    try:
                        fil_inv[fil_inv[0:i].index(0)] = copy(fil_inv[i])
                        fil_inv[i] = 0

                    except:
                        continue
                tablero[k] = fil_inv[::-1]    
        case "up":
            #Notemos que para este caso, fila por fila, moverse hacia arriba es lo mismo que
            #Primero transponer el tablero, y luego mover el tablero como en el caso hacia la
            #Izquierda y luego transponer de vuelta
            trans_tab = copy(transponer_tablero(tablero))
            for k in range(len(trans_tab)):
                if (len(set(trans_tab[k][0:2]))==1 and trans_tab[k][0] != 0) and (len(set(trans_tab[k][2:4]))==1  and trans_tab[k][2] != 0):
                    trans_tab[k] = [2*trans_tab[k][0],2*trans_tab[k][2],0,0]
                    continue
                flag = 0 
                for i in range(1,4):
                    if trans_tab[k][i] == 0:
                        continue
                    else:
                        for j in range(i):
                            if (trans_tab[k][i] == trans_tab[k][j]) and (flag == 0):
                                if set(trans_tab[k][j+1:i]) in [{0},set()]:
                                    
                                    trans_tab[k][j] = copy(trans_tab[k][i]*2)
                                    trans_tab[k][i] = 0
                                    score += trans_tab[k][j]
                                    if max_value<trans_tab[k][j]:
                                        max_value = trans_tab[k][j]
                                    if trans_tab[k][j] in [512,1024,2048,4096]:
                                        print(f"Alcanzaste el {trans_tab[k][j]}")
                                    flag = 1
                                    break
                            else:
                                continue

                for i in range(1,4):

                    try:
                        trans_tab[k][trans_tab[k][0:i].index(0)] = copy(trans_tab[k][i])
                        trans_tab[k][i] = 0

                    except:
                        continue
            tablero = transponer_tablero(trans_tab)
            
        #Notemos que para este caso, mover hacia arriba el tablero es lo mismo que
        #Primero transponer el tablero, y luego mover el tablero como en el caso hacia la
        #derecha y luego transponer de vuelta
        case "down":
            trans_tab = copy(transponer_tablero(tablero))
            for k in range(len(trans_tab)):
                fil_inv = copy(trans_tab[k][::-1])
                if (len(set(fil_inv[0:2]))==1 and fil_inv[0] != 0) and (len(set(fil_inv[2:4]))==1  and fil_inv[2] != 0):
                    fil_inv = [2*fil_inv[0],2*fil_inv[2],0,0]
                    trans_tab[k] = fil_inv[::-1]  
                    continue
                flag = 0 
                for i in range(1,4):
                    if fil_inv[i] == 0:
                        continue
                    else:
                        for j in range(i):
                            if (fil_inv[i] == fil_inv[j]) and (flag == 0):
                                if set(fil_inv[j+1:i]) in [{0},set()]:                                    
                                    fil_inv[j] = copy(fil_inv[i]*2)
                                    fil_inv[i] = 0
                                    score += fil_inv[j]
                                    if max_value<fil_inv[j]:
                                        max_value = fil_inv[j]
                                    if fil_inv[j] in [512,1024,2048,4096]:
                                        print(f"Alcanzaste el {fil_inv[j]}")
                                    flag = 1
                                    break
                            else:
                                continue
                for i in range(1,4):
                    try:
                        fil_inv[fil_inv[0:i].index(0)] = copy(fil_inv[i])
                        fil_inv[i] = 0
                    except:
                        continue
                trans_tab[k] = fil_inv[::-1]
            tablero = transponer_tablero(trans_tab)
        
                
    return (tablero,score,max_value)

#Determina si se perdio o no, y si se puede continuar jugando
def continuar(tablero):
    for mov in ["up","left","right","down"]:
        if mover_tablero(mov,tablero)[0] != tablero:
            return True
        
    




    

        
    
    
    

