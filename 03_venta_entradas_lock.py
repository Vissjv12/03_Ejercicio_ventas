import threading
import time


ENTRADAS_INICIALES = 5


class Taquilla:
    def __init__(self, entradas):
        self.entradas = entradas
        self.ventas_realizadas = 0
        self.lock = threading.Lock()

    def vender_sin_lock(self, cliente):
        if self.entradas > 0:
            entradas_leidas = self.entradas
            time.sleep(0.1)
            self.entradas = entradas_leidas - 1
            self.ventas_realizadas += 1
            print(f"{cliente} compro una entrada")
        else:
            print(f"{cliente} entradas agotadas")

    def vender_con_lock(self, cliente):
        with self.lock:
            if self.entradas > 0:
                entradas_leidas = self.entradas
                time.sleep(0.1)
                self.entradas = entradas_leidas - 1
                self.ventas_realizadas += 1
                print(f"{cliente} compro una entrada")
            else:
                print(f"{cliente}  entradas agotadas")


def ejecutar_ventas(metodo_venta):
    taquilla = Taquilla(ENTRADAS_INICIALES)
    vender = metodo_venta(taquilla)

    hilo_ana = threading.Thread(target=vender, args=("Ana",))
    hilo_bruno = threading.Thread(target=vender, args=("Bruno",))
    hilo_carla = threading.Thread(target=vender, args=("Carla",))
    hilo_diego = threading.Thread(target=vender, args=("Diego",))
    hilo_elena = threading.Thread(target=vender, args=("Elena",))
    hilo_fernando = threading.Thread(target=vender, args=("Fernando",))
    hilo_gabriela = threading.Thread(target=vender, args=("Gabriela",))
    hilo_hugo = threading.Thread(target=vender, args=("Hugo",))

    hilo_ana.start()
    hilo_bruno.start()
    hilo_carla.start()
    hilo_diego.start()
    hilo_elena.start()
    hilo_fernando.start()
    hilo_gabriela.start()
    hilo_hugo.start()

    hilo_ana.join()
    hilo_bruno.join()
    hilo_carla.join()
    hilo_diego.join()
    hilo_elena.join()
    hilo_fernando.join()
    hilo_gabriela.join()
    hilo_hugo.join()

    print(f"Ventas registradas: {taquilla.ventas_realizadas}")
    print(f"Entradas restantes: {taquilla.entradas}")
    return taquilla


def main():
    print("Sin lock")
    sin_lock = ejecutar_ventas(lambda taquilla: taquilla.vender_sin_lock)
    print(
        "Resultado:",
        sin_lock.ventas_realizadas + sin_lock.entradas == ENTRADAS_INICIALES,
    )

    print("\nCon Lock")
    con_lock = ejecutar_ventas(lambda taquilla: taquilla.vender_con_lock)
    print(
        "Resultado:",
        con_lock.ventas_realizadas + con_lock.entradas == ENTRADAS_INICIALES,
    )


if __name__ == "__main__":
    main()
