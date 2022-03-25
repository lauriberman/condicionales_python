# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

palabra_1 = str(input('Ingrese una palabra:\n'))
palabra_2 = str(input('Ingrese una segunda palabra:\n'))
palabra_3 = str(input('Ingrese una tercera palabra:\n'))

print('Cómo quiere ordenar las palabras ingresadas?\n')
print('1 - Ordenar por orden alfabético\n')
print('2 - Ordenar por cantidad de letras\n')
respuesta = str(input('Ingrese el número de la respuesta elegida:\n'))

if respuesta == '1':
    print('Orden alfabético:')
    if (palabra_1 > palabra_2) and (palabra_1 > palabra_3) and (palabra_2 > palabra_3):
        print(palabra_1, palabra_2, palabra_3)
    elif (palabra_1 > palabra_2) and (palabra_1 > palabra_3) and (palabra_3 > palabra_2):
        print(palabra_1, palabra_3, palabra_2)
    elif (palabra_2 > palabra_1) and (palabra_2 > palabra_3) and (palabra_1 > palabra_3):
        print(palabra_2, palabra_1, palabra_3)
    elif (palabra_2 > palabra_1) and (palabra_2 > palabra_3) and (palabra_3 > palabra_1):
        print(palabra_2, palabra_3, palabra_1)
    elif (palabra_3 > palabra_1) and (palabra_3 > palabra_2) and (palabra_1 > palabra_2):
        print(palabra_3, palabra_1, palabra_2)
    elif (palabra_3 > palabra_1) and (palabra_3 > palabra_2) and (palabra_2 > palabra_1):
        print(palabra_3, palabra_2, palabra_1)

if respuesta == '2':
    print('Orden por cantidad de letras:')
    if (len(palabra_1) > len(palabra_2)) and (len(palabra_1) > len(palabra_3)) and (len(palabra_2) > len(palabra_3)):
        print(palabra_1, palabra_2, palabra_3)
    elif (len(palabra_1) > len(palabra_2)) and (len(palabra_1) > len(palabra_3)) and (len(palabra_3) > len(palabra_2)):
        print(palabra_1, palabra_3, palabra_2)
    elif (len(palabra_2) > len(palabra_1)) and (len(palabra_2) > len(palabra_3)) and (len(palabra_1) > len(palabra_3)):
        print(palabra_2, palabra_1, palabra_3)
    elif (len(palabra_2) > len(palabra_1)) and (len(palabra_2) > len(palabra_3)) and (len(palabra_3) > len(palabra_1)):
        print(palabra_2, palabra_3, palabra_1)
    elif (len(palabra_3) > len(palabra_1)) and (len(palabra_3) > len(palabra_2)) and (len(palabra_1) > len(palabra_2)):
        print(palabra_3, palabra_1, palabra_2)
    elif (len(palabra_3) > len(palabra_1)) and (len(palabra_3) > len(palabra_2)) and (len(palabra_2) > len(palabra_1)):
        print(palabra_3, palabra_2, palabra_1)

        



   



