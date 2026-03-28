def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto = float(input("Ingresar gasto: "))

    dinero = int(input("Dinero recibido "))

    vuelto = dinero - gasto
    pesos = int(vuelto)
    centavos = vuelto - pesos
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero)
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print("Centavos:")
    print(int(round(centavos*100)))

change()


