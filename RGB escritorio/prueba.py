import requests
try:
	import json
except:
	import simplejson as json

serie = "Genius Einstein"
url = "http://206.189.239.59/get_seriejson/"+serie+"/"
r = requests.get(url) #descarga archivi json
datos = r.text #se pasa el archivo json a datos
#info = json.loads(datos)

#url = "http://206.189.239.59/get_categorias/"
#r = requests.get(url)
#data = r.text
#datos = json.loads(data)
print(datos)
