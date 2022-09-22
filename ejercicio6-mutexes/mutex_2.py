import threading
from time import sleep 
import pytube   

mutex = threading.Lock()

def crito(url, id):
    global x;
    x = x + id
    videos= pytube.YouTube(str(url))
    #_____videos guardados en el archivo ejercicio5/videos_____
    videos.streams.first().download("C:/Users/BZM/Documents/cuatri 13/concurrente/corte 1/ejercicio5/videos")
    print("download successful (id)= ", id)
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

class Hilo(threading.Thread):
    def __init__(self, url, id):
        threading.Thread.__init__(self)
        self.url=url
        self.id=id
        
    def run(self):
        mutex.acquire()
        #sleep(3-self.id)
        crito(self.url, self.id)
        #print("valor:", self.id)
        mutex.release()


hilos = [Hilo("https://www.youtube.com/watch?v=LICMmzOqLoE",1),
                    Hilo("https://www.youtube.com/watch?v=Jqs5EaAaueA",2),
                    Hilo("https://www.youtube.com/watch?v=qGf6QFB_rEI",3),
                    Hilo("https://www.youtube.com/watch?v=Qzw6A2WC5Qo",4),
                    Hilo("https://www.youtube.com/watch?v=VuGzJVKtW6g",5),
                    Hilo("https://www.youtube.com/watch?v=Z5NoQg8LdDk",6),
                    Hilo("https://www.youtube.com/watch?v=9sTQ0QdkN3Q",7),
                    Hilo("https://www.youtube.com/watch?v=q2I0ulTZWXA",8),
                    Hilo("https://www.youtube.com/watch?v=GofHQmlJCG0",9),
                    Hilo("https://www.youtube.com/watch?v=05wXNKzOkRM",10)]
x=1;
for h in hilos:
    h.start()