class Pila:
    def __init__(self):
        self.lista = []

    def esta_vacia(self):
        return self.lista == []
    
    def agregar(self, pagina):
        self.lista.append(pagina)

    def eliminar(self):
        if not self.esta_vacia():
            return self.lista.pop()
        else:
            print("No ha visitado ninguna página")

    def imprimir(self):
        if not self.esta_vacia():
            return self.lista[-1]
        else:
            print("No ha entrado a ninguna página")


def main():
    p = Pila()
    while True:
        print("-----Navegación de páginas de OperaGX-----")
        print("1. Entrar a una página")
        print("2. Retroceder una página")
        print("3. Mostrar página actual")
        print("4. Salir del navegador")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            pagina = input("Ingrese una página que desea entrar: ")
            p.agregar(pagina)
            print("Página agregada")
        elif opcion == 2:
            print(f"Retrocediendo a página anterior")
            p.eliminar()
        elif opcion == 3:
            print(f"Pagina actual: {p.imprimir()}")
        elif opcion == 4:
            print("Saliendo del navegador")
            break
        else:
            print("Ingrese una opcion valida")
            return

    
if __name__ == "__main__":
    main()


    

    