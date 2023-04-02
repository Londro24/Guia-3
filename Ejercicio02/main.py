from vacunas import Vacuna


def menu(vac, inter):
    selec = -1
    while selec < 0 or selec > 4:
        print(
            "\n> Elija una acción"
            "\n>> 1) Ver nombre de la vacuna"
            "\n>> 2) Ver laboratorio de la vacuna"
            "\n>> 3) Agregar efectos secundarios a la vacuna"
            "\n>> 4) Ver efectos secundarios de la vacuna"
            "\n>> 5) Cambiar a otra vacuna"
            "\n>> 0) Salir"
            )
        
        try:
            selec = int(input())
            print("\n")
            if selec < 0 or selec > 4:
                print("Valor invalido")
        except:
            print("Valor invalido")
    
    match selec:
        case 1:
            print(vac.get_nombre())
        case 2:
            print(vac.get_laboratorio())
        case 3:
            vac.set_efecto(input("> Señale el efecto secundario: "))
        case 4:
            vac.get_efecto()
        case 5:
            pass
        case 0:
            inter = False
    
    return inter


def main():
    interruptor = True
    vacuna1 = Vacuna()
    vacuna2 = Vacuna()
    vacuna3 = Vacuna()
    
    print("Ingrese el nombre de las 3 vacunas")
    while not vacuna1.get_nombre():
        vacuna1.set_nombre(input("Vacuna 1: "))
    while not vacuna2.get_nombre():
        vacuna2.set_nombre(input("Vacuna 2: "))
    while not vacuna3.get_nombre():
        vacuna3.set_nombre(input("Vacuna 3: "))
    
    print("Ingrese el laboratorio de las 3 vacunas")
    while not vacuna1.get_laboratorio():
        vacuna1.set_laboratorio(input(
            f"Laboratorio de la vacuna {vacuna1.get_nombre()}: "
            ))
    while not vacuna2.get_laboratorio():
        vacuna2.set_laboratorio(input(
            f"Laboratorio de la vacuna {vacuna2.get_nombre()}: "
            ))
    while not vacuna3.get_laboratorio():
        vacuna3.set_laboratorio(input(
            f"Laboratorio de la vacuna {vacuna3.get_nombre()}: "
            ))
    
    while interruptor:
        selec = -1
        while selec < 0 or selec > 3:
            print(
                "\n> Seleccione una vacuna"
                f"\n>> 1) {vacuna1.get_nombre()}" 
                f"\n>> 2) {vacuna2.get_nombre()}", 
                f"\n>> 3) {vacuna3.get_nombre()}"
                "\n>> 0) Salir"
                )
            
            try:
                selec = int(input())
                print("\n")
                if selec < 0 or selec > 3:
                    print("Valor invalido")
            except:
                print("Valor invalido")
        
        match selec:
            case 0:
                interruptor = False
            case 1:
                interruptor = menu(vacuna1, interruptor)
            case 2:
                interruptor = menu(vacuna2, interruptor)
            case 3:
                interruptor = menu(vacuna3, interruptor)


if __name__ == "__main__":
    main()
