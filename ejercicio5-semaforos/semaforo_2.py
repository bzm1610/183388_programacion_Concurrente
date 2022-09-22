from threading import Thread, Semaphore
from turtle import st
import pytube

semaforo = Semaphore(1)

def dowland_video(url,id):
    videos= pytube.YouTube(str(url))
    videos.streams.first().download("C:/Users/BZM/Documents/cuatri 13/concurrente/corte 1/ejercicio5/videos")
    print("download successful (id)= ", id)

class Hilo(Thread):
    def __init__(self, url, id):
        Thread.__init__(self)
        self.url=url
        self.id=id

    def run(self):
        semaforo.acquire()
        dowland_video(self.url,self.id)
        semaforo.release()

threads_semaphore = [Hilo("https://www.youtube.com/watch?v=LICMmzOqLoE",1),
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
for t in threads_semaphore:
    t.start()