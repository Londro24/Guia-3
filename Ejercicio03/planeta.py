class Planeta():
    def __init__(self):
        self.__nombre = None
        self.__identifcador = int
        self.__masa = None
        self.__densidad = None
        self.__diametro = None
        self.__distancia = None
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("El tipo de dato no es aceptable")
            self.__nombre = None
    
    def get_nombre(self):
        return self.__nombre
    
    def set_identifcador(self, identifcador):
        if isinstance(identifcador, int):
            self.__identifcador = identifcador
        else:
            print("El tipo de dato no es aceptable")
            self.__identifcador = 0
    
    def get_identifcador(self):
        return self.__identifcador
    
    def set_masa(self, masa):
        if isinstance(masa, str):
            self.__masa = masa
        else:
            print("El tipo de dato no es aceptable")
            self.__masa = None
    
    def get_masa(self):
        return self.__masa
        
    def set_densidad(self, densidad):
        if isinstance(densidad, str):
            self.__densidad = densidad
        else:
            print("El tipo de dato no es aceptable")
            self.__densidad = None
    
    def get_densidad(self):
        return self.__densidad
    
    def set_diametro(self, diamtro):
        if isinstance(diamtro, str):
            self.__diametro = diamtro
        else:
            print("El tipo de dato no es aceptable")
            self.__diametro = None
    
    def get_diametro(self):
        return self.__diametro
    
    def set_distancia(self, distancia):
        if isinstance(distancia, str):
            self.__distancia = distancia
        else:
            print("El tipo de dato no es aceptable")
            self.__distancia = None
    
    def get_distancia(self):
        return self.__distancia
    
    def mostrar_datos(self):
        print(f"Planeta: {self.get_nombre()}")
        print(f"Identificador: {self.get_identifcador()}")
        print(f"Masa: {self.get_masa()} Kg")
        print(f"Densidad: {self.get_densidad()} g/cm**3")
        print(f"Diametro: {self.get_diametro()} Km")
        print(f"Distancia: {self.get_distancia()} Km del sol")
