def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    Nombre = input("Ingrese el nombre:")
    Email = input("ingrese el email:")
    Texto1 = input("ingrese el texto:")
    Texto2 = input("ingrese el texto:")
    Texto3 = input("ingrese el texto:")
    nombrebien = Nombre.strip().title()
    print('''========================
    FICHA DEL ALUMNO
========================''')
    print(f"Nombre: {nombrebien}")
    print(f"Email: {Email.lower()}")
    print(f"Caracteres en nombre: {len(nombrebien)}")
    esp = nombrebien.find(" ")
    print(f"Iniciales: {nombrebien[0] + nombrebien[esp+1]}")
    partes = nombrebien.split(" ")
    print(f"Usuario: {partes[1].lower() +"."+partes[0].lower()}")
    print(f"Email valido: {"@" in Email}")
    pos = Email.find("@")
    dominio = Email[pos+1:]
    print(f"Dominio: {dominio.lower()}")
    print(f"Nombre para archivo: {nombrebien.replace(" ", "_")}")
    print(f"Cantidad de a: {nombrebien.lower().count("a")}")
    print(f"Codigo secreto: {nombrebien[::-1].upper()}")
    print(f"Nota 1: {Texto1}")
    print(f"Nota 2: {Texto2}")
    print(f"Nota 3: {Texto3}")
    n1= int(Texto1)
    n2= int(Texto2)
    n3= int(Texto3)
    suma = n1+n2+n3
    promedio = suma/3
    promediobien= suma//3
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promediobien}")
    print("="*24)


ficha()
