import requests
import threading
import time
import mysql.connector
import json
import pytube

#1
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
#C:\Users\BZM\Documents\cuatri 13\concurrente\corte 1\ejercicio4\videos
#2
conexion = mysql.connector.connect(  
    user="root",
    password= "",
    host="localhost",
    database="prueba_sincrono",
    port = "3306"
    )

def get_servicesBD():
    resp = requests.get('https://pokeapi.co/api/v2/pokemon/')
    print(resp) 
    if resp.status_code == 200:
        resp_json= json.loads(resp.text)
        for x in resp_json["results"]:
            print(x)
            nombre= x["name"]
            write_db(nombre)#x.name)


def write_db(x):
    cursor = conexion.cursor()
    #print(x)
    sql = "INSERT INTO pokemons (nombre) VALUES (%s)"
    val = x
    print(val)

    cursor.execute(sql, (val,))
    conexion.commit()
    rows = cursor.fetchall()
    cursor.close()
    
    
#3
def get_services(x=0):
    
    print(f'Data input = {x}')
    time.sleep(100)
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
 
if __name__ == '__main__':
    x=0
    for x in range(0,50):
        th1 = threading.Thread(target=get_services, args=[x])#subpreceso que viaq en esta target
        th1.start()
    th2 = threading.Thread(target= get_servicesBD)
    th2.start()
    th3 = threading.Thread(target=get_service_video)
    th3.start()
       #descargar 5 videos
       #escribir base  de datos 2000 registros
       #generar una solicitud a randomuser de por lo menos 50 usuariosde maniera asincrona