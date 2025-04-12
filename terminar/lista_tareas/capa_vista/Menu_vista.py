#pip install termcolor
#https://pypi.org/project/termcolor/
import sys
import os
from platform import system

from termcolor import colored, cprint
class menu_vista:

    def __init__(self):
        # self.__tarea_v = t_v()
        pass

    def lista_items_menu(self):
        os.system('cls')
        text = colored("Dime, ¿Qué opción eliges?", "white","on_light_blue", attrs=["bold", "dark"])
        print(text)
        text = colored("1) Insertar una nueva Tarea", "blue", attrs=["bold","strike"])
        print(text)
        text = colored("2) Modificar una nueva Tarea", "blue", attrs=["bold", "strike"])
        print(text)
        text = colored("3) Eliminar una nueva Tarea", "blue", attrs=["bold", "strike"])
        print(text)
        text = colored("4) Buscar una Tarea", "blue", attrs=["bold", "strike"])
        print(text)
        text = colored("5) Listar tareas", "blue", attrs=["bold", "strike"])
        print(text)
        text = colored("6) Crear la base de datos", "blue", attrs=["bold", "strike"])
        print(text)
        text = colored("7) Crear un archivo txt con la lista de tareas", "blue", attrs=["bold", "strike"])
        print(text)
        text = colored("8) Salir de la aplicación", "red", attrs=["bold", "strike"])
        print(text)
        text = colored("0) Ayuda", "yellow", attrs=["bold", "strike"])
        print(text)
        cprint("Atención! con la elección", "red", attrs=["bold"], file=sys.stderr)

    def mostrar_menu(self):
        opcion = 0
        while True:
            self.lista_items_menu()
            opcion = 0
            opcion_cadena = input("Elige una opción: ")
            if (opcion_cadena.isdigit() == True):
                opcion = int(opcion_cadena)
                if opcion == 1:
                    # self.__tarea_v.insertar_nueva_tarea()
                    pass
                elif opcion == 2:
                    # self.__tarea_v.modificar_una_tarea()
                    pass
                elif opcion == 3:
                    # self.__tarea_v.eliminar_una_tarea()
                    pass
                elif opcion == 4:
                    # self.__tarea_v.buscar_una_tarea()
                    pass
                elif opcion == 5:
                    # self.__tarea_v.ver_tareas()
                    pass
                elif opcion == 6:
                    # self.__tarea_v.crear_base_de_datos_por_defecto()
                    pass
                elif opcion == 7:
                    # self.__tarea_v.crear_archivo()
                    pass
                elif opcion == 8:
                    break
                elif opcion >= 9:
                    print("Opción incorrecta")
                elif opcion == 0:
                    pass
                    # help(self.__tarea_v)
                    # help(t)
            else:
                print("Opción incorrecta")