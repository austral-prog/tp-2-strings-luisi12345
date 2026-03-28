def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""
    lol = "Python"
    strip = (nombre.strip())
    left = (nombre.lstrip())
    right = (nombre.rstrip())
    print(f"Strip: {strip}")
    print(f"Lstrip: {left}")
    print(f"Rstrip: {right}")
    print(f"Upper: {frase.upper()}")
    print(f"Lower: {frase.lower()}")
    print(f"Title: {frase.title()}")
    print(f"Find: {frase.find("gran")}")
    print(f"Replace: {frase.replace("programacion","desarrollo")}")
    print(f"Count: {frase.count("a")}")
    print(f"Contiene Python: {"Python" in frase}")
    print(f"Contiene Java: {"Java" in frase}")
    print(f"Slice: {frase[0:6]}")
    print(f"Paso: {frase[0:6:2]}")
    print(f"Reverso: {lol [::-1]}")
    print(f"Formato: {nombre.strip()} sabe {lol}")
    print("""Linea 1
Linea 2
Linea 3""")




string_methods()
