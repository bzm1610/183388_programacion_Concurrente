import threading
import time
import requests


def crito(url,id):
    print("url successful id: "+str(id)+" url: "+str(url))
    #print("Hilo =" +str(id) )


class Hilo(threading.Thread):
    def __init__(self, url, id):
        threading.Thread.__init__(self)
        self.url=url
        self.id=id
        
    def run(self):
        #mutex.acquire()
        resp = requests.get(self.url)
        if resp.status_code == 200:
            crito(self.url,self.id)
        else:
            print("Error")

while True:
    hilos = [Hilo("https://www.youtube.com/watch?v=LICMmzOqLoE",1), Hilo("https://www.youtube.com/watch?v=Jqs5EaAaueA",2),
            Hilo("https://www.youtube.com/watch?v=qGf6QFB_rEI",3), Hilo("https://www.youtube.com/watch?v=Qzw6A2WC5Qo",4),
            Hilo("https://www.youtube.com/watch?v=VuGzJVKtW6g",5), Hilo("https://www.youtube.com/watch?v=Z5NoQg8LdDk",6),
            Hilo("https://www.youtube.com/watch?v=9sTQ0QdkN3Q",7), Hilo("https://www.youtube.com/watch?v=q2I0ulTZWXA",8),
            Hilo("https://www.youtube.com/watch?v=GofHQmlJCG0",9), Hilo("https://www.youtube.com/watch?v=eJnQBXmZ7Ek",10),
            Hilo("https://www.youtube.com/watch?v=UOUBW8bkjQ4",11), Hilo("https://www.youtube.com/watch?v=8mn-FFjIbo8",12),
            Hilo("https://www.youtube.com/watch?v=r_9Kf0D5BTs",13), Hilo("https://www.youtube.com/watch?v=ywvRgGAd2XI",14),
            Hilo("https://www.youtube.com/watch?v=92XVwY54h5k",15), Hilo("https://www.youtube.com/watch?v=Pmv8aQKO6k0",16),
            Hilo("https://www.youtube.com/watch?v=mDyxykpYeu8",17), Hilo("https://www.youtube.com/watch?v=LHCob76kigA",18),
            Hilo("https://www.youtube.com/watch?v=7gwO8-oqwFw",19), Hilo("https://www.youtube.com/watch?v=w8KQmps-Sog",20),
            Hilo("https://www.youtube.com/watch?v=Ek0SgwWmF9w",21), Hilo("https://www.youtube.com/watch?v=R8OOWcsFj0U",22),
            Hilo("https://www.youtube.com/watch?v=G_sBOsh-vyI",23), Hilo("https://www.youtube.com/watch?v=4PkcfQtibmU",24),
            Hilo("https://www.youtube.com/watch?v=TPE9uSFFxrI",25)]
    
    init_time = time.time()
    for h in hilos:
        h.start()
        h.join()

    end_time = time.time() - init_time
    print("tiempo :", end_time)
    time.sleep(240)