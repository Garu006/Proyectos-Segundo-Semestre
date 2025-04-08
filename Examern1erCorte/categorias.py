def add_categoria(categorias):
    categoria = input("Agregue una nueva categoría: ")
    if categoria not in categorias:
        categorias.append(categoria)
        print(f"La categoría {categoria} ha sido registrada.")
    else:
        print(f"La categoría ya existe.")