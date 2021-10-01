from Datos import *
class Cifrado(Datos):
    d1 = Datos.abc
    def __init__(self, palabra, clave):
        self.palabra = palabra
        self.clave = clave
        super().__init__(clave, palabra)

    def cifrar(self):
        for i in range(len(self.palabra)):
            for j in range (len(self.abc)):
                if self.palabra[i] in self.abc[j] :
                    resultado = self.abc[(self.palabra[i]+self.abc[j]) %len(self.abc)]
        return resultado





