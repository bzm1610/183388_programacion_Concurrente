import threading
import time
import random

estadoFilosofo = None
candados = []
CANTIDAD_FILOSOFOS = 0
MAXIMO_INTENTOS_FALLIDOS = 10 
RAFAGA_COMER = 0
TOTAL_TIEMPO_COMER = 0   

ESTADO_FILOSOFEANDO = "F"
ESTADO_HAMBRIENTO = "H"
ESTADO_COMIENDO = "C"
ESTADO_SATISFECHO = "S"
ESTADO_MUERTO = "M"

mutex = threading.Lock()

def agarrarPalillos(id_filosofo):
    #"""Trata de tomar los palillos izquierdo y derecho (en ese orden) 
    # y devuelve True si ha podido adquirir ambos y False de lo contrario"""

    palillo_izq = candados[id_filosofo]
    palillo_der = candados[(id_filosofo - 1) % CANTIDAD_FILOSOFOS]

    palillo_izq.acquire()

    if palillo_der.acquire(blocking=False):
        return True
    else:
        palillo_izq.release()
        return False


def liberarPalillos(id_filosofo):
    #"""Liberación de los palillos adyacentes al filosofo"""
    candados[id_filosofo].release()
    candados[(id_filosofo - 1) % CANTIDAD_FILOSOFOS].release()


def iniciarSimulacion(id_filosofo):
    #"""Función que va ejecutar cada filosofo(hilo)"""

    intentos_fallidos = 0
    tiempo_comiendo = 0

    while tiempo_comiendo < TOTAL_TIEMPO_COMER:
        if agarrarPalillos(id_filosofo):
            # Limpiar los intentos, ya que ya ha terminado de comer
            intentos_fallidos = 0

            # Acción de comer
            tiempo_comer = min(RAFAGA_COMER, TOTAL_TIEMPO_COMER - tiempo_comiendo)
            tiempo_comiendo += tiempo_comer
            ttiempo_comer=TOTAL_TIEMPO_COMER
            print(f"[+] Filosofo {id_filosofo+1} comiendo [{tiempo_comer} seg.] del tiempo total a comer [{ttiempo_comer}]")
            time.sleep(tiempo_comiendo)
            liberarPalillos(id_filosofo)

            # Filosofar
            estadoFilosofo[id_filosofo] = ESTADO_FILOSOFEANDO
            tiempo_filosofar = random.uniform(0, 2)
            print(f"[*] Filosofo {id_filosofo+1} filosofando[{tiempo_filosofar:.2f} seg.]")
            time.sleep(tiempo_filosofar)
        else:
            estadoFilosofo[id_filosofo] = ESTADO_HAMBRIENTO
            intentos_fallidos += 1

            if intentos_fallidos >= MAXIMO_INTENTOS_FALLIDOS:
                estadoFilosofo[id_filosofo] = ESTADO_MUERTO
                print(f"[-] Filosofo {id_filosofo+1} muerto por inanición")
                return
            
            tiempo_reintentar = random.uniform(0, 3)
            print(f"[ ] Filosofo {id_filosofo+1} esperando tenedores"
                  f" Intento {intentos_fallidos} [{tiempo_reintentar:.2f} seg.]")
            time.sleep(tiempo_reintentar)

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id
        
    def run(self):
        mutex.acquire()
        #sleep(3-self.id)
        iniciarSimulacion(self.id)
        #print("valor:", self.id)
        mutex.release()

if __name__ == '__main__':

    # Establecer los argumentos leídos por línea de comandos
    CANTIDAD_FILOSOFOS = 8         #Número de filósofos (hilos)
    RAFAGA_COMER = 4               #Ráfaga de comer de los filósofos ()
    TOTAL_TIEMPO_COMER = 6         #Tiempo total que requiere comer un filosofo para estar satisfecho
    MAXIMO_INTENTOS_FALLIDOS = 10    #Cantidad de intentos antes de que el filósofo muera de inanición

    estadoFilosofo = CANTIDAD_FILOSOFOS * [ESTADO_FILOSOFEANDO]

    # Inicialización de candados del palillo
    for _ in range(CANTIDAD_FILOSOFOS):
        candados.append(threading.RLock())
       
    hilos = [Hilo(0), Hilo(1), Hilo(2), Hilo(3), Hilo(4), Hilo(5), Hilo(6), Hilo(7)]
    
    # Iniciar ejecución de los hilos
    for hilo in hilos:
        hilo.start()
        hilo.join()