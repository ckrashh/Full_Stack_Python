class rutInvalido(Exception):    
    pass
def val_rut(rut):    
    if len(rut) > 8:
        raise rutInvalido("rut invalido")
    return f"rut valido {rut}"
try:
    with open("rut.txt", "r") as archivo:
        contenido = archivo.read()
    val_rut(contenido.strip())
except FileNotFoundError:
    print("Archivo no encontrado.")
except rutInvalido as e:
    print(e)
