


def filtro(filtrar):

    nombres = ["maria", "rambo", "yulimey", "santiago", "rafmary"]
    nombres_filtrados = []
    for nombre in nombres:
        
        if nombre != filtrar:
            nombres_filtrados.append(nombre)
    return nombres_filtrados


filter = filtro("yulimey")


print(filter)


        