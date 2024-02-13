def cuadrilateros():
    print("**TIPOS DE CUADRILATEROS**")
    print("Ingrese las medidas de los lados del cuadrilatero: ")
    lados = []
    for i in range(4):
        lado = int(input(f"Lado {i+1}: "))
        lados.append(lado)

    lados_unicos = len(set(lados))
    if lados_unicos == 1:
        print("Es un cuadrado")
    elif lados_unicos == 2:
        print("Es un rectangulo")
    else:
        print("Es otro tipo de cuadrilatero")

cuadrilateros()
