from sistema_planetario import Sistema
from planeta import Planeta


def main():
    sistema_solar = Sistema()
    sistema_solar.set_nombre("Sistema Solar")
    mercurio = Planeta()
    venus = Planeta()
    tierra = Planeta()
    marte = Planeta()
    
    mercurio.set_nombre("Mercurio")
    venus.set_nombre("Venus")
    tierra.set_nombre("Tierra")
    marte.set_nombre("Marte")
    
    sistema_solar.set_planetas(mercurio)
    sistema_solar.set_planetas(venus)
    sistema_solar.set_planetas(tierra)
    sistema_solar.set_planetas(marte)
    
    sistema_solar.get_planetas()
    
    mercurio.set_identifcador(1)
    mercurio.set_masa("3,302 * (10**23)")
    mercurio.set_densidad("5,43")
    mercurio.set_diametro("4879.4")
    mercurio.set_distancia("5.791 * (10**7)")

    mercurio.mostrar_datos()

if __name__ == "__main__":
    main()
