#Ana Sofía Espinoza Durán

#El programa muestra operaciones con x, que es 22, las muestra en numero decimal y en numero binario.

x = 22

print ("x       =       {: >6b}". format ( x ) )                      #x=22 en binario 
print ("x & 4 	= {: >3d} = {: >6b}". format ( x & 4 , x & 4) )       #AND entre x y 4
print ("x | 1 	= {: >3d} = {: >6b}". format ( x | 1 , x | 1) )       #OR entre x y 1
print ("x ^ 4 	= {: >3d} = {: >6b}". format ( x ^ 4 , x ^ 4) )       #XOR entre 4 y x
print ("~x      = {: >3d} = {: >6b}". format (~ x , ~ x ) )           #NOT de x
print ("x << 1 	= {: >3d} = {: >6b}". format ( x << 1 , x << 1) )     #Desplazamiento hacia la izquierda 
print ("x >> 2 	= {: >3d} = {: >6b}". format ( x >> 2 , x >> 2) )     #Desplazamiento hacia la derecha