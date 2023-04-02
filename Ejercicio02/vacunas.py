class Vacuna():
    def __init__(self):
        self.__nombre = None
        self.__laboratorio = None
        self.__efectos = []
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("El tipo de dato no es aceptable")
            self.__nombre = None
    
    def get_nombre(self):
        return self.__nombre
    
    def set_laboratorio(self, nombre):
        if isinstance(nombre, str):
            self.__laboratorio = nombre
        else:
            print("El tipo de dato no es aceptable")
            self.__laboratorio = None
    
    def get_laboratorio(self):
        return self.__laboratorio
    
    def set_efecto(self, efectos):
        if isinstance(efectos, str):
            self.__efectos.append(efectos)
        else:
            print("El tipo de dato no es aceptable")
    
    def get_efecto(self):
        if len(self.__efectos) == 0:
            print("No tiene efectos secundarios")
        else:
            print("Efectos: ")
            for i in range(0, len(self.__efectos)):
                print(f"{i + 1}) {self.__efectos[i]}")
