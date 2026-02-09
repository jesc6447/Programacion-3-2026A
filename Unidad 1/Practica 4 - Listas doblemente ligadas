#Juan Emmanuel Sanchez Castañon
#Listas doblemnte ligadas

class Contacto:
    def __init__(self, nombre, telefono,curp):
        self.nombre = nombre
        self.telefono = telefono
        self.curp = curp
        self.siguiente = None
        self.anterior = None

class nodo:
    def __init__(self, contacto):
        self.contacto = contacto
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_contacto_al_inicio(self, contacto):
        nuevo_nodo = nodo(contacto)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def agregar_contacto_al_final(self, contacto):
        nuevo_nodo = nodo(contacto)
        if self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
    

    def eliminar_contacto(self, curp):
        actual = self.cabeza
        while actual is not None:
            if actual.contacto.curp == curp:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def mostrar_contactos(self):
        contactos = []
        actual = self.cabeza
        while actual is not None:
            contactos.append(actual.contacto)
            actual = actual.siguiente
        return contactos
    
    def buscar_contacto(self, curp):
        actual = self.cabeza
        while actual is not None:
            if actual.contacto.curp == curp:
                return actual.contacto
            actual = actual.siguiente
        return None
    
def main():
        lista = ListaDoble()
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
                    print(" Opcion 1 seleccionada. Insertar al inicio ". center(60, "="))
                    nombre = input("Ingrese el nombre del contacto: ")
                    telefono = input("Ingrese el teléfono del contacto: ")
                    curp = input("Ingrese la CURP del contacto: ")
                    contacto = Contacto(nombre, telefono, curp)
                    lista.agregar_contacto_al_inicio(contacto)
                    print("Contacto agregado al inicio.")

                case "2":
                    print(" Opcion 2 seleccionada. Insertar al final ". center(60, "="))                    
                    nombre = input("Ingrese el nombre del contacto: ")
                    telefono = input("Ingrese el teléfono del contacto: ")
                    curp = input("Ingrese la CURP del contacto: ")
                    contacto = Contacto(nombre, telefono, curp)
                    lista.agregar_contacto_al_final(contacto)
                    print("Contacto agregado al final.")
                
                case "3":
                    print(" Opcion 3 seleccionada. Mostrar Agenda ". center(60, "="))
                    print("\n")
                    contactos = lista.mostrar_contactos()
                    if contactos:
                        print("Contactos en la lista:")
                        for contacto in contactos:
                            print("=".center(60, "-"))
                            print("\n")
                            print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, CURP: {contacto.curp}")
                            print("\n")
                            print("=".center(60, "-"))
                    else:
                        print("La lista está vacía.")
                    
                case "4":
                    print(" Opcion 4 seleccionada. Buscar contacto ". center(60, "="))
                    print("\n")
                    buscar = input("Deseas buscar al inicio de la agenda? (s/n): ")
                    if buscar.lower() == "s":
                        curp = input("Ingrese la CURP del contacto a buscar: ")
                        actual = lista.cabeza
                        encontrado = False
                        while actual is not None:
                            if actual.contacto.curp == curp:
                                print(f"Contacto encontrado: Nombre: {actual.contacto.nombre}, Teléfono: {actual.contacto.telefono}, CURP: {actual.contacto.curp}")
                                encontrado = True
                                break
                            actual = actual.siguiente
                        if not encontrado:
                            print("Contacto no encontrado.")
                    else:
                        curp = input("Ingrese la CURP del contacto a buscar: ")
                        actual = lista.cola
                        encontrado = False
                        while actual is not None:
                            if actual.contacto.curp == curp:
                                print(f"Contacto encontrado: Nombre: {actual.contacto.nombre}, Teléfono: {actual.contacto.telefono}, CURP: {actual.contacto.curp}")
                                encontrado = True
                                break
                            actual = actual.anterior
                        if not encontrado:
                            print("Contacto no encontrado.")

                case "5":
                    print("\n")
                    print(" Opcion 5 seleccionada. Eliminar contacto ". center(60, "="))
                    print("\n")
                    curp = input("Ingrese la CURP del contacto a eliminar: ")
                    buscar_contacto = lista.buscar_contacto(curp) 
                    if buscar_contacto:
                        print("\n")
                        print("Contacto encontrado:".center(60, "-"))
                        print(f"Contacto encontrado: Nombre: {buscar_contacto.nombre}, Teléfono: {buscar_contacto.telefono}, CURP: {buscar_contacto.curp}")
                        confirmar = input("¿Deseas eliminar este contacto? (s/n): ")
                        if confirmar.lower() == "s":
                            if lista.eliminar_contacto(curp):
                                print("Contacto eliminado.")
                            else:
                                print("Error al eliminar el contacto.")                        
                        else:
                            print("Operación cancelada. No se eliminará ningún contacto.")


                    """print("\n")
                    confirmar = input("¿Deseas eliminar al inicio de la agenda? (s/n): ")
                    if confirmar.lower() == "s":
                        if lista.eliminar_contacto(curp):
                            print("Contacto eliminado.")
                        else:
                            print("Contacto no encontrado.")
                    else:
                       print("Operación cancelada. No se eliminará ningún contacto.")"""



                case "6":
                    print("\n")
                    print(" Opcion 6 seleccionada. Salir ". center(60, "="))
                    print("\n")
                    print(" Opcion 6 seleccionada. Salir ". center(60, "="))
                    print("Saliendo del programa.")
                    break

                case _:
                    print("\n")
                    print(" Opción no válida ". center(60, "="))
                    print("\n")
                    print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()