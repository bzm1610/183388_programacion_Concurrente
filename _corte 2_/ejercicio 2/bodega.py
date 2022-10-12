from threading import Thread 
import threading
import time, random
import queue

bodega = queue.Queue(maxsize=20)
mutex_C = threading.Lock()
mutex_P = threading.Lock()

class Productor(Thread):
    def __init__(self, array1):
        Thread.__init__(self)
        self.array1 = array1

    def run(self):
        while True:
            if not bodega.full():
                print("agregando..." )
                mutex_P.acquire()
                array1 = random.randint(0, 20)
                bodega.put(array1)
                print("Se agrego un nuevo intem: " + str(array1))
                print("En bodega: ",str(list(bodega.queue)))
                mutex_P.release()
                time.sleep(5)


class Consumidor(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        while True:
            if bodega.empty() == False:
                time.sleep(10)
                print("consumiendo..." )
                mutex_C.acquire()
                #array2 = random.randint(0, 5)
                bodega.get()
                mutex_C.release()
                print("Se consumio un nuevo intem ")# + str(array2))
                #print("En bodega: ",str(list(bodega.queue)))    
 
 
 
def main():
    prductor=[]
    
    hilo_productor = Productor(prductor)
    hilo_consumidor = Consumidor()

    hilo_productor.start()
    hilo_consumidor.start()


main()