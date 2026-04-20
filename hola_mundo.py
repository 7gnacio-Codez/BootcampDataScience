# 1. Imprime "Hola, mundo"
print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Luis Ignacio"
print( "Hola,", nombre ) # con una coma
print("Hola, "+nombre ) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 717
print("Hola",numero) # con una coma
print("Hola " + str(numero) ) # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "pasta"
comida2 = "asados"
print("Me encanta comer {} y {}".format(comida1,comida2)) # con .format()
print(f"Me encanta comer {comida1} y {comida2}" ) # con una cadena f

##Bonus Ninja

print(
    f"Hola, mi nombre es {nombre.upper()} y tiene {len(nombre)} letras.\n"
    f"Si mi nombre estuviera en una lista: {nombre.split(' ')}.\n"
    f"Mi primer nombre es {nombre.split(' ')[0]} y mi apellido es {nombre.split(' ')[1]}.\n"
    f"También me gusta comer {comida1} y {comida2}.\n"
    f"Mi número favorito es {numero}."
)