from Datos import *
class Cifrado(Datos):
    def __init__(self, palabra, clave, abc):
        self.palabra = palabra
        self.clave = clave
        self.abc = abc
        super().__init__(palabra, clave, abc)

    def cifrar(self):
        for i in range(len(self.palabra)):
            for j in range (len(self.abc)):
                if self.palabra[i] in self.abc[j] :
                    resultado = self.abc[(self.palabra[i]+self.abc[j]) %len(self.abc)]
        return resultado





