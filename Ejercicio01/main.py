from perro import Perro


def menu(perro, act):
    selec = -1
    while selec < 0 or selec > 6:
        print(
            "> Elija una accion\n"
            ">> 1) Tomar Agua\n"
            ">> 2) Ver horas de agua\n"
            ">> 3) Revisar esta paseando\n"
            ">> 4) Pasear\n"
            ">> 5) Parar de Pasear\n"
            ">> 6) cambiar de perro\n"
            ">> 0) Salir"
            )
        
        try:
            selec = int(input())
            print("\n")
            if selec < 0 or selec > 6:
                print("Valor invalido")
        except:
            print("Valor invalido")
    
    match selec:
        case 1:
            hora = int(input("Ingrese hace cuanto en el perro tomo agua: "))
            perro.set_hora_toma_agua(hora)
        case 2:
            perro.get_hora_toma_agua()
        case 3:
            perro.get_pasear()
        case 4:
            perro.pasear()
        case 5:
            perro.para()
        case 6:
            pass
        case 0:
            act = False
    
    return act


def main():
    accion = True
    print("> Inserte el nombre de sus 2 perrros")
    perro_1 = Perro()
    perro_2 = Perro()
    
    """
    perro_1.set_nombre("Cristian")
    perro_2.set_nombre("Juan")
    """
    
    while not perro_1.get_nombre():
        perro_1.set_nombre(input("Perro 1: "))
    while not perro_2.get_nombre():
        perro_2.set_nombre(input("Perro 2: "))
    
    print(">", perro_2.get_nombre())
    print(">", perro_1.get_nombre())
    
    while accion:
        selec = -1
        
        while selec < 0 or selec > 2:
            print(
                "\n> Elija su perro"
                "\n>> 1)", perro_1.get_nombre(), 
                "\n>> 2)", perro_2.get_nombre(), 
                "\n>> 0) Salir"
                )
            
            try:
                selec = int(input())
                print("\n")
                if selec < 0 or selec > 2:
                    print("Valor invalido")
            except:
                print("Valor invalido")
        
        match selec:
            case 0:
                accion = False
            case 1:
                accion = menu(perro_1, accion)
            case 2:
                accion = menu(perro_2, accion)


if __name__ == "__main__":
    main()