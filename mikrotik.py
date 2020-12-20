import routeros_api
import os
import datetime, pathlib
dt = datetime.datetime.now()
fecha = str(dt.year)+'-'+str(dt.month)+'-'+str(dt.day)
destino = os.path.join("C:/Users/jose_/Documents/TRABAJO ARANET/BACKUPS",fecha)
os.mkdir(destino)

"""
array = ['','','']

for i in array:
"""
connection = routeros_api.RouterOsApiPool('192.168.10.16', username='admin', password='', plaintext_login=True)
api = connection.get_api()

backupmikrotik = api.get_resource('/system/backup')
backupmikrotik.save(name="hola")
