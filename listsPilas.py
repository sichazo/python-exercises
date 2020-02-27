from collections import deque

stack = [3,4,5]
stack.append(6)
stack.append(7)
stack.append(8)
stack.pop()
stack.pop()
print(stack)

queue = deque(["Eric","Sergio","Michel"])
queue.append("Terry")
queue.append("Joel")
queue.popleft()
queue.popleft()
print(queue)

squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x : x**2, range(5)))
print(squares)

lista2 = [x**2 for x in range(5)]
print(lista2)

#Conjunto en python

basket = {'manzana','banana','manzana','banana','pera','naranja'}
print(basket)          # mostrar que se han eliminado los duplicados
v='naranja' in basket  # prueba rápida de membresía
print(v)
e = 'asdasdasd' in basket
print(e)

    # Demostrar operaciones de conjuntos en letras únicas de dos palabras.

a = set('abracadabra')
b = set('alacazam')
print(a)     # letras únicas en un
r = a - b    # letras en a pero no en b
print(r)
o = a | b  	# letters in a or b or both
print (o)
h =  a & b  # letras en a y b
print(h)

# Diccionario en Python

ej = {'Daniel':2323, 'Jose Alfredo':2525}
ej['Joel'] = 2626

ej['Jose Alfredo']
print(ej)

#Tecnica de bucle
knighthts = {'Numero':'Uno','Siguiente':'Dos'}
for k,V in knighthts.items():
    print(k,v)

#Funcion reversed cuando se imprime en forma reversa

for i in reversed(range(10)):
    print(i)

#Funcion sorted funcion donde devuelve una nueva lista ordenada

frutas =['Manzana','Naranja','Manzana','Naranja','Banana','Pera']
for f in sorted(set(frutas)):
    print(f)

cadena1, cadena2, cadena3 = '','Cadena','No Cadena'
non_null = cadena1 or cadena2 or cadena3
print(non_null)
