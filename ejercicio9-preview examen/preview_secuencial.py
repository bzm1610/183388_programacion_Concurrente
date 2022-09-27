import threading
import time
import requests

mutex = threading.Lock()

def crito(data):
    for url, id in data:  
        resp = requests.get(url)
        if resp.status_code == 200:
            print("url successful id: "+str(id)+" url: "+str(url))
        else:
            print("Error")



hilo = [("https://www.youtube.com/watch?v=LICMmzOqLoE",1), ("https://www.youtube.com/watch?v=Jqs5EaAaueA",2),
            ("https://www.youtube.com/watch?v=qGf6QFB_rEI",3), ("https://www.youtube.com/watch?v=Qzw6A2WC5Qo",4),
            ("https://www.youtube.com/watch?v=VuGzJVKtW6g",5), ("https://www.youtube.com/watch?v=Z5NoQg8LdDk",6),
            ("https://www.youtube.com/watch?v=9sTQ0QdkN3Q",7), ("https://www.youtube.com/watch?v=q2I0ulTZWXA",8),
            ("https://www.youtube.com/watch?v=GofHQmlJCG0",9), ("https://www.youtube.com/watch?v=eJnQBXmZ7Ek",10),
            ("https://www.youtube.com/watch?v=UOUBW8bkjQ4",11), ("https://www.youtube.com/watch?v=8mn-FFjIbo8",12),
            ("https://www.youtube.com/watch?v=r_9Kf0D5BTs",13), ("https://www.youtube.com/watch?v=ywvRgGAd2XI",14),
            ("https://www.youtube.com/watch?v=92XVwY54h5k",15), ("https://www.youtube.com/watch?v=Pmv8aQKO6k0",16),
            ("https://www.youtube.com/watch?v=mDyxykpYeu8",17), ("https://www.youtube.com/watch?v=LHCob76kigA",18),
            ("https://www.youtube.com/watch?v=7gwO8-oqwFw",19), ("https://www.youtube.com/watch?v=w8KQmps-Sog",20),
            ("https://www.youtube.com/watch?v=Ek0SgwWmF9w",21), ("https://www.youtube.com/watch?v=R8OOWcsFj0U",22),
            ("https://www.youtube.com/watch?v=G_sBOsh-vyI",23), ("https://www.youtube.com/watch?v=4PkcfQtibmU",24),
            ("https://www.youtube.com/watch?v=TPE9uSFFxrI",25)]

while True:
    init_time = time.time()
    crito(hilo)
    end_time = time.time() - init_time
    print("tiempo :", end_time)
    time.sleep(240)