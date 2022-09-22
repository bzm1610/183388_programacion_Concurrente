import requests
import time
import mysql.connector
import json
#_____________________________ instalar: pip install mysql-connector-python__________________________________
conexion = mysql.connector.connect(  
    user="root",
    password= "",
    host="localhost",
    database="prueba_sincrono",
    port = "3306"
    )
# investigar sobre la libreria threaing
#instalar extencion live share 

def get_service():
    # whit concurrent.futures.ThreadPoolExecutor(mas_workes=5) as executor:
    # executor.map(connection_db)
    #aplicar for
    #print(data.name)
    resp = requests.get('https://pokeapi.co/api/v2/pokemon/')
    print(resp) 
    if resp.status_code == 200:
        resp_json= json.loads(resp.text)
        for x in resp_json["results"]:
            print(x)
            nombre= x["name"]
            write_db(nombre)#x.name)
    #for x in data:
     #   print(x)
      #  write_db(x)#x.name)
        
    #pass
    #implementar requests
    #consumimr un servicio que descargue por lo menos 5000 registros con requests

def write_db(x):
    cursor = conexion.cursor()
    print(x)
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
   #url_sites
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)