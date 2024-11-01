import Directores
import Supermercados
from python.Acceso import login


def menu():
    print("\n--- Menú ---")
    print("1. Directores")
    print("2. Supermercados")
    print("0. Salir de la aplicación")


def Main():
    token = login()
    menu()
    opc = input("Selecciona una opción: ")
    while opc!="0":
        match opc:
            case "1":
                Directores.printMenudirectores()
                opc = input("Selecciona una opción: ")
                Directores.menuDirectores(opc, token)
            case "2":
                Supermercados.printMenusupermercados()
                opc = input("Selecciona una opción: ")
                Supermercados.menuSupermercados(opc, token)
            case _:
                print("Opcion invalida")
        menu()
        opc = input("Selecciona una opción: ")
    print("Saliendo...")



if __name__ == '__main__':
    Main()