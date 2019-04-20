
import requests

try:
	import json
except:
	import simplejson as json

def traer_activo(idtmdb):
	 resp = requests.get('http://206.189.239.59/get_activo/'+str(idtmdb)+'/')
	 resp = resp.text
	 return resp

def traer_titulo(idtmdb):
	 resp = requests.get('http://206.189.239.59/get_titulo/'+str(idtmdb)+'/')
	 resp = resp.text
	 return resp

def traer_genero(idtmdb):
	 resp = requests.get('http://206.189.239.59/get_genero/'+str(idtmdb)+'/')
	 resp = resp.text
	 return resp

def traer_estreno(idtmdb):
	 resp = requests.get('http://206.189.239.59/get_estreno/'+str(idtmdb)+'/')
	 resp = resp.text
	 return resp

def traer_url(idtmdb):
	 resp = requests.get('http://206.189.239.59/get_url/'+str(idtmdb)+'/')
	 resp = resp.text
	 return resp

def traer_thumbnail(idtmdb):
	 resp = requests.get('http://206.189.239.59/get_thumbnail/'+str(idtmdb)+'/')
	 resp = resp.text
	 return resp

def traer_fanart(idtmdb):
	 resp = requests.get('http://206.189.239.59/get_fanart/'+str(idtmdb)+'/')
	 resp = resp.text
	 return resp

def traer_sinopsis(idtmdb):
	 resp = requests.get('http://206.189.239.59/get_sinopsis/'+str(idtmdb)+'/')
	 resp = resp.text
	 return resp

def existe(idtmdb):
	 resp = requests.get('http://206.189.239.59/existe/'+str(idtmdb)+'/')
	 resp = resp.text
	 return resp

def write_titulo(idtmdb,titulo):
	r = requests.get('http://206.189.239.59/write_titulo/'+str(idtmdb)+'/'+str(titulo)+'/')
	print(r.text)
	
def write_sinopsis(idtmdb,sinopsis):	
	r = requests.get('http://206.189.239.59/write_sinopsis/'+str(idtmdb)+'/'+str(sinopsis)+'/')
	print(r.text)
	
def write_estreno(idtmdb,date):
	r = requests.get('http://206.189.239.59/write_estreno/'+str(idtmdb)+'/'+str(date)+'/')
	print(r.text)
	
def write_genero(idtmdb,genero):
	r = requests.get('http://206.189.239.59/write_genero/'+str(idtmdb)+'/'+str(genero)+'/')
	print(r.text)
	
def write_thumbnail(idtmdb,thumbnail):
	r = requests.get('http://206.189.239.59/write_thumbnail/'+str(idtmdb)+'/'+str(thumbnail)+'/')
	print(r.text)
	
def write_fanart(idtmdb,fanart):
	r = requests.get('http://206.189.239.59/write_fanart/'+str(idtmdb)+'/'+str(fanart)+'/')
	print(r.text)

def agrega_idtmdb(idtmdb):
    r = requests.get('http://206.189.239.59/agrega_idtmdb/'+str(idtmdb)+'/')
    print(r.text)                 
#resp = existe(13)
#print(resp)