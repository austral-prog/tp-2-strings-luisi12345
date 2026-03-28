def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    Base= int(input("Base:"))
    Altura = int(input("Altura:"))

    area= Base * Altura
    perimetro = 2* (Base + Altura)

    print(f"Base: {Base}")
    print(f"Altura: {Altura}")
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")

rectangle()