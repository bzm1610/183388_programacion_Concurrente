import pytube
import requests
import threading
import time

def get_service_video():
    
    print("vide 1")
    videos= pytube.YouTube("https://www.youtube.com/watch?v=LICMmzOqLoE")
    videos.streams.first().download("C:/Users/BZM/Documents/cuatri 13/concurrente/corte 1/ejercicio4/videos")
    print("vide 2")
    videos= pytube.YouTube("https://www.youtube.com/watch?v=Jqs5EaAaueA")
    videos.streams.first().download("C:/Users/BZM/Documents/cuatri 13/concurrente/corte 1/ejercicio4/videos")
    print("vide 3")
    videos= pytube.YouTube("https://www.youtube.com/watch?v=qGf6QFB_rEI")
    videos.streams.first().download("C:/Users/BZM/Documents/cuatri 13/concurrente/corte 1/ejercicio4/videos")
    print("vide 4")
    videos= pytube.YouTube("https://www.youtube.com/watch?v=Qzw6A2WC5Qo")
    videos.streams.first().download("C:/Users/BZM/Documents/cuatri 13/concurrente/corte 1/ejercicio4/videos")
    print("vide 5")
    videos= pytube.YouTube("https://www.youtube.com/watch?v=VuGzJVKtW6g")
    videos.streams.first().download("C:/Users/BZM/Documents/cuatri 13/concurrente/corte 1/ejercicio4/videos")
    

if __name__ == '__main__':
    th = threading.Thread(target=get_service_video)
    th.start()