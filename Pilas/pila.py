class Pila:
    def __init__(self):
        self.lista = [] #creamos la lista

    def esta_vacia(self):
        return self.lista == [] #verificamos si la lista esta vacia

    def agregar(self, elemento):
        self.lista.append(elemento) #agregamos el elemento

    def eliminar(self):
        return self.lista.pop() #eliminamos el ultimo elemento 

    def imprimir(self):
        return self.lista #imprimimos la lista
    
    def tamaño(self):
        return len(self.lista) #devolvemos el tamaño de la lista

p = Pila()#creamos la instancia y mandamos a llamar al constructor 
print("Estado de la pila: ")
print(p.esta_vacia())
elemento = int(input("Ingrese un elemento de tipo entero: "))
p.agregar(elemento)
elemento = float(input("Ingrese un elemento de tipo decimal: "))
p.agregar(elemento)
elemento = input("Ingrese un elemento de tipo cadena: ")
p.agregar(elemento)
print("Estado de la pila: ")
print(p.esta_vacia())
print("Lista de elementos:")
print(p.imprimir())
print("Tamaño de la pila: ")
print(p.tamaño())
print("Eliminar elemento")
print(p.eliminar())
print("Estado de la pila: ")
print(p.esta_vacia())
print("Lista de elementos: ")
print(p.imprimir())