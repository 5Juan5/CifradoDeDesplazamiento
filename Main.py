from Cifrado import *

palabra = input("Agregar palabra a cifrar: ")
clave = int(input('Agrega la clave: '))
c1 = Cifrado(palabra, clave)
print(f'Tu palabra cifrada es: {c1.cifrar()}')