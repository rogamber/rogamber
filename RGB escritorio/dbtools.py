import sqlite3
import tmdb
import urllib2
import requests
from bs4 import BeautifulSoup

def buscar_pelicula(id_tmdb):
	existe = True
	try:
	   bd = sqlite3.connect("dbRGBTV.db")
	   cursor = bd.cursor()
	   sentencia = "SELECT * FROM PELICULAS WHERE ID_TMDB LIKE ?"
	   cursor.execute(sentencia, [id_tmdb])
	   pelicula = cursor.fetchall()
	   bd.close()
	   if pelicula == []:
		  existe = False
	   else:
		  print("La pelicula ya existe en la base de datos")	  
	except sqlite3.OperationalError as error:
	   print("Error al abrir:", error)
	return existe

def grabar_pelicula(id_tmdb , api_key):
	info = tmdb.traer_infopeli(id_tmdb , api_key)
	desc = tmdb.traer_desc(info)
	genero = tmdb.traer_genre(info)
	estreno = tmdb.traer_date(info)
	adult = tmdb.traer_categoria(info)
	titulo = tmdb.traer_titulo(info)
	
	thumbnail = tmdb.traer_thumbnail(info)
	fanart = tmdb.traer_fanArt(info)
	bd = sqlite3.connect("dbRGBTV.db")
	bd.text_factory = str
	cursor = bd.cursor()
	sentencia = "INSERT INTO PELICULAS(ID_TMDB,TITULO,SINOPSIS,GENERO,ESTRENO,ADULT,THUMBNAIL,FANART) VALUES (?,?,?,?,?,?,?,?)"
	datos = [id_tmdb,titulo,desc,genero,estreno,adult,thumbnail,fanart]
	cursor.execute(sentencia , datos) 
	bd.commit()
	bd.close()


def actualizar_pelicula(id_tmdb,api_key):
	info = tmdb.traer_infopeli(id_tmdb , api_key)
	desc = tmdb.traer_desc(info)
	genero = tmdb.traer_genre(info)
	estreno = tmdb.traer_date(info)
	adult = tmdb.traer_categoria(info)
	titulo = tmdb.traer_titulo(info)	
	thumbnail = tmdb.traer_thumbnail(info)
	fanart = tmdb.traer_fanArt(info)
	bd = sqlite3.connect("dbRGBTV.db")
	bd.text_factory = str
	cursor = bd.cursor()
	sentencia = "UPDATE PELICULAS SET THUMBNAIL = ? WHERE ID_TMDB = ?"
	datos = [thumbnail,id_tmdb]
	cursor.execute(sentencia,datos)
	sentencia = "UPDATE PELICULAS SET FANART = ? WHERE ID_TMDB = ?"
	datos = [fanart,id_tmdb]
	cursor.execute(sentencia,datos) 
	bd.commit()
	cursor.close()
	bd.close() 

def makeRequest(url, headers=None):
		try:
		   if headers is None:
							 headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
							 req = urllib2.Request(url,None,headers)
							 response = urllib2.urlopen(req)
							 data = response.read()
							 response.close()
							 return data
		except:
			  print("Error en URL")
			


def traer_items(url):
	data = None
	data = makeRequest(url, headers=None)
	return data
	

def actualiza_datos_DjangoDB(idtmdb , api_key):
	info = tmdb.traer_infopeli(idtmdb , api_key)
	sinopsis = tmdb.traer_desc(info)
	genero = tmdb.traer_genre(info)
	estreno = tmdb.traer_date(info)
	adult = tmdb.traer_categoria(info)
	titulo = tmdb.traer_titulo(info)	
	thumbnail = tmdb.traer_thumbnail(info)
	fanart = tmdb.traer_fanArt(info)
	r = requests.get('http://206.189.239.59/write_titulo/'+str(idtmdb)+'/'+str(titulo)+'/')
	print(r.text)
	r = requests.get('http://206.189.239.59/write_sinopsis/'+str(idtmdb)+'/'+str(sinopsis)+'/')
	print(r.text)
	r = requests.get('http://206.189.239.59/write_estreno/'+str(idtmdb)+'/'+str(estreno)+'/')
	print(r.text)
	r = requests.get('http://206.189.239.59/write_genero/'+str(idtmdb)+'/'+str(genero)+'/')
	print(r.text)
	r = requests.get('http://206.189.239.59/write_thumbnail/'+str(idtmdb)+'/'+str(thumbnail)+'/')
	print(r.text)
	r = requests.get('http://206.189.239.59/write_fanart/'+str(idtmdb)+'/'+str(fanart)+'/')
	print(r.text)

def traer_titulo_BDLocal(idtmdb):
	#Se actualizan los datos con la base Sqlite local
	bd = sqlite3.connect("dbRGBTV.db")
	bd.text_factory = str
	cursor = bd.cursor()
	sentencia = "SELECT TITULO FROM PELICULAS WHERE ID_TMDB=?"
	datos = [idtmdb]
	titulo = cursor.execute(sentencia,datos)
	titulo = titulo.fetchone()
	titulo = titulo[0]
	#print(titulo)
	#bd.commit()
	#cursor.close()
	#bd.close() 
