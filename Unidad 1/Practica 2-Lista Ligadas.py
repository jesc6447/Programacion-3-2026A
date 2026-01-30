# Juan Emmanuel Sanchez Castañon
# Implementación de una lista ligada en Python

class Contacto:
    def __init__(self, nombre, telefono,curp):
        self.nombre = nombre
        self.telefono = telefono
        self.curp = curp
        self.siguiente = None

class Nodo:
    def __init__(self,contacto):
        self.contacto = contacto
        self.siguiente = None

class ListaLigada:
    def __init__(self):
        self.cabeza = None

    def agregar_contacto_al_inicio(self, contacto):
        nuevo_nodo = Nodo(contacto)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def agregar_contacto_al_final(self, contacto):
        nuevo_nodo = Nodo(contacto)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo
    
    def mostrar_contactos(self):
        actual = self.cabeza
        while actual:
            print("="*60)
            print("\n")
            print(f"Nombre: {actual.contacto.nombre}, \nTeléfono: {actual.contacto.telefono}, \nCURP: {actual.contacto.curp}")
            print("\n")
            print("="*60)
            actual = actual.siguiente
    
    def buscar_contacto(self, curp):
        actual = self.cabeza
        while actual:
            if actual.contacto.curp == curp:
                return actual.contacto
            actual = actual.siguiente
        return None

    def eliminar_contacto(self, curp):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.contacto.curp == curp:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
        return False

def main():
        lista = ListaLigada()
        c1 = Contacto("Ana López", "3312345678", "LOPA900101HJCRNS09")
        lista.agregar_contacto_al_final(c1)
        c2 = Contacto("Luis Pérez", "3311122233", "PERL850505HJCRRS01")
        lista.agregar_contacto_al_final(c2)
        c3 = Contacto("María Gómez", "3319988776", "GOMM920202MJCRRS08")
        lista.agregar_contacto_al_final(c3)

        while True:
            print("\n")
            print(" Menú de Lista Ligada ".center(60, "*"))
            print("\n")
            print("1. Insertar al inicio")
            print("2. Insertar al final")
            print("3. Mostrar lista")
            print("4. Buscar elemento")
            print("5. Eliminar contacto")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    print("\n")
                    print(" Opcion 1 seleccionada. Insertar al inicio ". center(60, "="))
                    nombre = input("Ingrese el nombre del contacto: ")
                    telefono = input("Ingrese el teléfono del contacto: ")
                    curp = input("Ingrese la CURP del contacto: ")
                    nuevo_contacto = Contacto(nombre, telefono, curp)
                    lista.agregar_contacto_al_inicio(nuevo_contacto)
                    print("\n")
                    print("Contacto agregado al inicio de la agenda.".center(60, "="))

                case "2":
                    print("\n")
                    print(" Opcion 2 seleccionada. Insertar al final ". center(60, "="))
                    nombre = input("Ingrese el nombre del contacto: ")
                    telefono = input("Ingrese el teléfono del contacto: ")
                    curp = input("Ingrese la CURP del contacto: ")
                    nuevo_contacto = Contacto(nombre, telefono, curp)
                    lista.agregar_contacto_al_final(nuevo_contacto)
                    print("\n")
                    print("Contacto agregado al final de la agenda.".center(60, "="))

                case "3":
                    print("\n")
                    print(" Opcion 3 seleccionada. Mostrar Agenda ". center(60, "="))
                    print("\n")
                    lista.mostrar_contactos()

                case "4":
                    print("\n")
                    print(" Opcion 4 seleccionada. Buscar elemento ". center(60, "="))
                    print("\n")
                    curp = input("Ingrese la CURP del contacto a buscar: ")
                    contacto_encontrado = lista.buscar_contacto(curp)
                    if contacto_encontrado:
                        print("\n")
                        print(f"Contacto encontrado: Nombre: {contacto_encontrado.nombre}, Teléfono: {contacto_encontrado.telefono}, CURP: {contacto_encontrado.curp}")
                    else:
                        print("\n")
                        print("Contacto no encontrado.".center(60, "="))
                    
                case "5":
                    print("\n")
                    print(" Opcion 5 seleccionada. Eliminar contacto ". center(60, "="))
                    print("\n")
                    curp = input("Ingrese la CURP del contacto a eliminar: ")
                    contacto_encontrado = lista.buscar_contacto(curp)
                    if contacto_encontrado:
                        print("\n")
                        print(f"Contacto encontrado: Nombre: {contacto_encontrado.nombre}, Teléfono: {contacto_encontrado.telefono}, CURP: {contacto_encontrado.curp}")
                        confirmado = input("¿Está seguro que desea eliminar este contacto? (s/n): ")
                        if confirmado.lower() == 's':
                            eliminado = lista.eliminar_contacto(curp)
                            if eliminado:
                                print("\n")
                                print("Contacto eliminado exitosamente.".center(60, "="))
                            else:
                                print("\n")
                                print("Error al eliminar el contacto.".center(60, "="))
                        else:
                            print("\n")
                            print("Eliminación cancelada.".center(60, "="))

                    else:
                        print("\n")
                        print("Contacto no encontrado.".center(60, "="))
                
                case "6":
                    print("\n")
                    print(" Saliendo del programa... ".center(60, "="))
                    break

                case _:

                    print(" Opción no válida. Por favor, intente de nuevo. ". center(60, "="))

if __name__ == "__main__":
    main()

