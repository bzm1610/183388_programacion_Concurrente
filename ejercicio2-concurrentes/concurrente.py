import requests
import time
import mysql.connector
import concurrent.futures
import threading
import json

#_____________________________ instalar: pip install mysql-connector-python__________________________________
conexion = mysql.connector.connect(  
    user="root",
    password= "",
    host="localhost",
    database="prueba_concurrente",
    port = "3306"
    )
# investigar sobre la libreria threaing
#instalar extencion live share 

threading_local = threading.local()

def service(url):
    print("url:-- ", url)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)#connection_db)  

def get_service(url):
    #aplicar for
    #data = requests.get('https://pokeapi.co/api/v2/pokemon/')
    resp=requests.get(url)
    #print(data.name)
    print("resp: ", resp) 
    if resp.status_code == 200:
        resp_json= json.loads(resp.text)
        for x in resp_json["results"]:
            #print(x)
            nombre= x["name"]
            print(nombre)
            write_db(nombre)#x.name)
        
    #pass
    #implementar requests
    #consumimr un servicio que descargue por lo menos 5000 registros con requests

def write_db(x):
    print("x=  ",x)
    cursor = conexion.cursor()
    print("insertando: ",x)
    sql = "INSERT INTO pokemons (nombre) VALUES (%s)"
    val = x
    print(val)

    cursor.execute(sql, (val,))

    conexion.commit()
    rows = cursor.fetchall()
    cursor.close()
    #pass
    #Escribir el reponse en una base de datos

if __name__=="__main__":
    url = ['https://pokeapi.co/api/v2/pokemon/']
    print("url pokemon:", url)
    init_time = time.time()
    service(url)
    end_time = time.time() - init_time
    print(end_time)