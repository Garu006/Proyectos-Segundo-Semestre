class Pila:
    def __init__(self):#Se crea un constructor que inicializa un atributo llamado "panes", que es una lista vacía
        self.panes = [] #Esta lista actuara como una pila

    def agregarPanes(self, pan): #Este metodo recibe un pan y lo añade al final de la lista con el metodo append
        self.panes.append(pan) #En la lista, el ultimo pan en entrar sera el ultimo en salir 
    
    def venderPan(self): #Se revisa si la pila no esta vacia
        if self.panes: #Si hay panes, se elimina el ultimo pan usando pop
            return self.panes.pop() #y se retorna ese valor
        else:
            return None #Si no hay panes, se retorna nulo
        
    def mostrarPanes(self): 
        if self.panes: #Si la lista tiene elementos, muestra todos los panes en la pila
            print("Panes en la pila:")
            print(self.panes)
        else: #Si la lista esta vacia, imprime un mensaje indicando error
            print("No hay panes en la pila.")