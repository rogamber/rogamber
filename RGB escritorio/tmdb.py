import requests
try:
	import json
except:
	import simplejson as json

def traer_infopeli(id_movie , api_key):
	ide = str(id_movie)
	url = "https://api.themoviedb.org/3/movie/"+ide+"?api_key="+api_key
	payload = "{}"
	response = requests.request("GET", url, data=payload)
	datos = response.text
	#xbmc.log(datos.encode('utf-8'), xbmc.LOGNOTICE)
	info = json.loads(datos)
	return info

def traer_genre(info):
	try:
		generos = info["genres"]
	except:
		  generos = []
	
	genre = ""
	cont = 0
	for i in generos:
		genre += (generos[cont]["name"]).encode('utf-8')+" , "
		cont = cont+1
	genre = genre[0:len(genre)-3]
	#genre = "[COLOR magenta]Genero: [/COLOR]"+"[COLOR yellow]"+genre+"[/COLOR]"	
	return genre    

def traer_desc(info):
	try:
		dat = info['overview'].encode('utf-8')
	except:
		  dat = ""	

	return dat

def traer_date(info):
	try:
	   date = info['release_date'].encode('utf-8')
	   date = date[0:len(date)-6]
	except:
		  date = ""

	return date	

def traer_fanArt(info):
	try:
	   fanArt = info['backdrop_path'].encode('utf-8')
	   fanArt = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"+fanArt
		
	except:
		  fanArt = "" 	
	return fanArt

def traer_thumbnail(info):
	try:
	    thumbnail = info['poster_path'].encode('utf-8')
	    thumbnail = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"+thumbnail
	except:
	    thumbnail = ""
	return thumbnail	

def traer_categoria(info):
	try:
	   categoria = info['adult']
	except:
		  categoria = ""
	return categoria	

def traer_titulo(info):
	titulo = "No se encontro Titulo"
	try:
	   titulo = info['title'].encode('utf-8')
	except:
		  pass

	return titulo


#api_key="2cd2538742da5dcb2d3e0a381a537689&language=es-ES"
#id_tmdb = "299536"
#info = traer_infopeli(id_tmdb,api_key)
#print(info)
#desc = info['overview'].encode('utf-8')
#addon_log(desc) 