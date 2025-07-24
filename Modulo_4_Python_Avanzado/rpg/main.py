from personaje import personaje 
import random
if __name__ == "__main__":
        turno = 1
        print("Bienvenido al RPG!")
        p1 = personaje("Guerrero", "Ferra", 100, 20, 10)
        p2 = personaje("Guerrero", "Jorge", 100 , 20, 10)
        print("Elija una opcion:\n1. Golpear\n2. Defender\n3. Ver estado\n4. Salir")
        opcion = input("Eleccion: ")
        print(f"\nTurno {turno} comenzando.\n")
        while opcion != "4":
            if opcion == "1":
                P1_danio = random.randint(10, p1.ataque)
                P2_danio = random.randint(10, p2.ataque)
                if random.choice([True, False]):
                    if not p1.esta_vivo():
                        p2.golpear(P2_danio,p1)
                else:
                    if not p2.esta_vivo():
                        p2.defender()    
                if not p1.esta_vivo():
                    p1.golpear(P1_danio,p2)

            elif opcion == "2":
                p1.defender()
                if random.choice([True, False]):
                    if not p2.esta_vivo():
                        p2.defender()
                else:
                    if not p2.esta_vivo():
                        P2_danio = random.randint(10, p2.ataque)
                        p2.golpear(P2_danio,p1)
            elif opcion == "3":
                print(p1)
                print(p2)
            else:
                print("Opción no válida. Intente de nuevo.")

            if not p1.esta_vivo() and not p2.esta_vivo():
                print(f"{p1.nombre} tiene {p1.vida} puntos de vida.")
                print(f"{p2.nombre} tiene {p2.vida} puntos de vida.")
                print(f"\nTurno {turno} finalizado.")
                turno += 1
                print("Continuando al siguiente turno...")
            if p1.esta_vivo():
                print(f"{p1.nombre} ha sido derrotado. {p2.nombre} gana!\nFin del juego.")
                break
            elif p2.esta_vivo():
                print(f"{p2.nombre} ha sido derrotado. {p1.nombre} gana!\nFin del juego.")
                break
            
            print("--------------------------------------")
            print("Turno siguiente:")
            print("Elija una opcion:\n1. Golpear\n2. Defender\n3. Ver estado\n4. Salir")
            opcion = input("Eleccion: ")
            print(f"\nTurno {turno} comenzando.\n")
            
        