print('Saludos desde un archivo Python')
# 1. TAREA: imprimir "Hola mundo"
print( 'Hola mundo')
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print('Hola ', name)	# con una coma
print( 'Hola ' + name)	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
name = 42
print( 'Hola ', str(name))	# con una coma
#print( 'Hola ' + name)	# con un + - !Este debería darnos un error! // Solucionado con str()
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print(f'Me encanta comer {fave_food1} y {fave_food2}') # con .format()
print('Me encanta comer {} y {}' .format(fave_food1, fave_food2) ) # con una cadena f

