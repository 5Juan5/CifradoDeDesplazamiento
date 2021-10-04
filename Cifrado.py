from Datos import *
class Cifrado(Datos):
    d1 = Datos.abc
    def __init__(self, palabra, clave):
        self.palabra = palabra
        self.clave = clave
        super().__init__(clave, palabra)

    def cifrar(self):
        resultado = ''
        for i in self.palabra:
            for j in self.abc:
                if i in j:
                    resultado += self.abc[(self.abc.index(j)+self.clave)% len(self.abc)]
        return resultado





