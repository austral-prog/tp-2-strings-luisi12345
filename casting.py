def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    Precio=int(input("Precio:"))
    Descuento=float(input("Descuento:"))
    Cantidad=int(input("Cantidad:"))


    Preciocondescuento = Precio - Descuento

    print(f"Precio: {Precio}")

    print(f"Descuento: {Descuento}")
    print(f"Precio con descuento: {Preciocondescuento}")
    print(f"Total: {Preciocondescuento * Cantidad}")

casting()

