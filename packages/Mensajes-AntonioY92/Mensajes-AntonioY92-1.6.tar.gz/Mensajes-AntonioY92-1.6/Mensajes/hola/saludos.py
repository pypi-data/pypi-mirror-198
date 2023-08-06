import numpy as np

def saludar():
    print("Hola, te saludo desde saludos.saludar()")

def prueba():
    print("Esto es una prueba de la nueva version 1.6")

def generar_array(numeros):
    return np.arange(numeros)
    #Se utiliza un modulo externo y se tiene que indicar en el setup(distribuible) que se instale como una dependencia

class Saludo:
    def __init__(self):
        print("Hola, te saludo desde saludo.__init__")

if __name__ == '__main__':
    print(generar_array(5))
#La variable __name__ almacena durante la ejecucion de un programa el nombre del scrip.

#Con esta comprobación se evita que al importar un modulo se ejecute el codigo que tenemos por ejemplo de pruebas en la parte inferior