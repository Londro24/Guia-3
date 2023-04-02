from planeta import Planeta


class Sistema():
    def __init__(self):
        self.__nombre = None
        self.__planetas = []
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("El tipo de dato no es aceptable")
            self.__nombre = None
    
    def get_nombre(self):
        return self.__nombre
    
    def set_planetas(self, planeta):
        if isinstance(planeta, Planeta):
            self.__planetas.append(planeta)
        else:
            print("El tipo de dato no es aceptable")
    
    def get_planetas(self):
        if len(self.__planetas) == 0:
            print("No tiene planetas el sistema")
        else:
            print("Planetas (Según entrada al programa): ")
            for i in range(0, len(self.__planetas)):
                print(f"{i + 1}) {self.__planetas[i].get_nombre()}")
