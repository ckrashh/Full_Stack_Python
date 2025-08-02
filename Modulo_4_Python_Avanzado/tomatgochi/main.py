from tomatgochi import Tomatgochi
from persona import Persona
from tipo_tomatgochi import TipoTomatgochi

if __name__ == "__main__":
    def lineas():
        print("-" * 50 + "\n")
    lineas()
    print("Primer Caso:")
    # Crear un objeto Tomatgochi
    tomatgochi = Tomatgochi(nombre="Tomate", color="Rojo", salud=80, felicidad=90, energia=100)
    # Mostrar los datos del Tomatgochi
    print(tomatgochi)
    # Crear una Persona con el Tomatgochi
    persona1 = Persona(nombre="Juan", apellido="Perez", tomatgochi=tomatgochi)
    # Mostrar los datos de la Persona
    print(persona1)
    # Interactuar con el Tomatgochi
    persona1.jugar_con_tomatgochi().darle_comida().curarlo()
    lineas()
    lineas()
    print("Segundo Caso:")
    # Crear los objetos TipoTomatgochi y Persona
    tamatchi = TipoTomatgochi(nombre="Shanks", color="Rojo", salud=85, felicidad=95, energia=110, tipo="Tamatchi", descripcion="Rebosante de energía y con un lado travieso, hace gala de incesante curiosidad y verborrea como si de un niño se tratase. Sin embargo, es precoz para su edad.")
    persona2 = Persona(nombre="Gerald", apellido="Carrillo", tomatgochi=tamatchi)
    # Mostrar los datos de la Persona con el Tipo de Tomatgochi
    print(persona2)
    tamatchi.mostrar_tipo()
    # Interactuar con el Tipo de Tomatgochi
    persona2.jugar_con_tomatgochi().darle_comida().curarlo()
    lineas()

    # crear persona sin Tomatgochi
    print("Tercer Caso:")
    persona3 = Persona(nombre="Andres", apellido="Sandoval", tomatgochi=None)
    print(persona3)
    # Intentar interactuar con un Tomatgochi que no existe
    persona3.jugar_con_tomatgochi().darle_comida().curarlo()
    lineas()

    # Tamatgochi sin entrenador
    print("Cuarto Caso:")
    tomatgochi2 = Tomatgochi(nombre="Pepe", color="naranjo", salud=80, felicidad=90, energia=100)
    print(tomatgochi2)
    # Interactuar con el Tomatgochi sin entrenador
    tomatgochi2.jugar().comer().curar()
    lineas()

    # TipoTomatgochi sin entrenador
    print("Quinto Caso:")  
    Mametchi = TipoTomatgochi(nombre="Mametchi", color="Amarillo", salud=90, felicidad=85, energia=95, tipo="Mametchi", descripcion="Un personaje Tamagotchi ambicioso que adora estudiar y hacer deporte.Disfruta inventando cosas, aunque no siempre le salen bien. Dibujar tampoco es lo suyo..")
    print(Mametchi)
    Mametchi.mostrar_tipo()
    # Interactuar con el Tipo de Tomatgochi sin entrenador
    Mametchi.jugar().comer().curar()
    lineas()

    print("Fin del Programa")