def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"

# La palabra.
# Su longitud.
# Su primera letra.
# Su última letra.
# La palabra repetida 3 veces.
# La palabra decorada con *** a cada lado.
# Salida esperada:
#
# Palabra: Programacion
# Longitud: 12
# Primera letra: P
# Ultima letra: n
# Repetida: ProgramacionProgramacionProgramacion
# Decorada: ***Programacion***

    print(f"Palabra: {palabra}")
    print (f"Longitud: {len(palabra)}")
    print(f"Primera letra: {palabra[0]}")
    print(f"Ultima letra: {palabra[11]}")
    print(f"Repetida: {palabra*3}")
    print(f"Decorada: ***{palabra}***")
string_info()