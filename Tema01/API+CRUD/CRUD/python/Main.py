import Directores
import Supermercados

def menu():
    print("\n--- Menú ---")
    print("1. Directores")
    print("2. Supermercados")
    print("0. Salir de la aplicación")


def Main():
    menu()
    opc = input("Selecciona una opción: ")
    while opc!="0":
        match opc:
            case "1":
                Directores.printMenudirectores()
                opc = input("Selecciona una opción: ")
                Directores.menuDirectores(opc)
            case "2":
                Supermercados.printMenuSupermercados()
                opc = input("Selecciona una opción: ")
                Supermercados.menuSupermercados(opc)
            case _:
                print("Opcion invalida")
        menu()
        opc = input("Selecciona una opción: ")
    print("Saliendo...")

if __name__ == '__main__':
    Main()