class Perro():
    def __init__(self):
        self.__nombre = None
        self.__agua = 0
        self.__pasear = False
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("El tipo de dato no es aceptable")
            self.__nombre = None
    
    def get_nombre(self):
        return self.__nombre
    
    def set_hora_toma_agua(self, hora):
        if isinstance(hora, int):
            self.__agua = hora 
        else:
            print("El tipo de dato no es aceptable")
            self.__agua = 0
    
    def get_hora_toma_agua(self):
        print("El perro tomo agua hace", self.__agua, "horas")
        return self.__agua
    
    def tomar_agua(self):
        if not self.__pasear:
            self.__agua = 0
        else:
            print("No puede tomar agua")
    
    def pasear(self):
        if self.__agua < 4:
            self.__pasear = True
            print("El perro esta paseando")
        else:
            print(
                "Aun no puede pasear, revise la opcion 2\nRecuerde "
                "que el perro puede pasear solo si tomo hace 4 horas"
                )
    
    def para(self):
        self.__pasear = False
        print("El perro ya no esta paseando")
    
    def get_pasear(self):
        if self.__pasear:
            print("Esta paseando")
            return True
        else:
            print("No esta paseando")
            return False
