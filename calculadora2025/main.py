#funciones sueltas
from funciones_calculadora import resta

#la clase
from clase_calculadora import calculadora

def menu():
    mi_calculadora = calculadora()
    opcion = 0
    while True:
        print("""
                    Dime, ¿Que operacion quieres realizar?
                    1) Suma
                    2) Resta
                    3) Multiplicacion
                    4) Division
                    5) Salir                   
                """)
        opcion = 0
        opcion_cadena = input("Elige una opción: ")
        if (opcion_cadena.isdigit() == True):
            opcion = int(opcion_cadena)
            if opcion == 1:
               print(mi_calculadora.suma(3,4))
            elif opcion == 2:
               print(resta(4,3))
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                break
        else:
            print("Opción incorrecta")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()
