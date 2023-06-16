#Queremos quedarnos con los nombres que tengan menos de 6 caracteres
#Lo primero sera abrir el fichero

fp = open("nombres.txt","r")
nombres_apellidos = fp.readlines()
fp.close()#cierro el fichero
#imprimo por pantalla
# print(nombres_apellidos)#imprimo para ver que todos los nombres tienen un salto de linea que hay que 
# #eliminar los saltos de linea
#haremos un bucle for
#creamos una lista 
fp = open('salidas.txt', 'w')
nombres, apellidos = [], []



for elemento in nombres_apellidos:
    aux = elemento.split("\n")[0]
    aux2 = aux.split(" ")
    
    if len(aux2[0]) < 6:
        fp.write(aux2[0] + " " + aux2[1] + "\n")
        

fp.close()
    


    





