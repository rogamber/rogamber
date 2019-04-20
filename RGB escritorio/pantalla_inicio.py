from Tkinter import *
import requests
import servitools
import tmdb
import dbtools
from PIL import Image
#import ver_thumbnail

def consulta_tmdb():
	api_key="2cd2538742da5dcb2d3e0a381a537689&language=es-ES"
	id_movie = idtmdb.get()
	info = tmdb.traer_infopeli(id_movie , api_key)
	name = tmdb.traer_titulo(info)
	titulo.set(name)
	txtsinopsis.delete(1.0,END)
	desc = tmdb.traer_desc(info)
	txtsinopsis.insert(END, desc)
	date = tmdb.traer_date(info)
	estreno.set(date)
	FanArt = tmdb.traer_fanArt(info)
	fanart.set(FanArt)
	poster = tmdb.traer_thumbnail(info)
	thumbnail.set(poster)
	genre = tmdb.traer_genre(info)
	genero.set(genre)

def agregar_DjangoDB():
    name = titulo.get()
    id_movie = idtmdb.get()
    existe = servitools.existe(id_movie) 
    if id_movie != "" and name != "No se encontro Titulo":
        if existe == "False":
            id_movie = idtmdb.get()
            servitools.agrega_idtmdb(id_movie)
            name = titulo.get().encode("utf-8")
            servitools.write_titulo(id_movie,name)
            desc = txtsinopsis.get(1.0,END).encode("utf-8")
            servitools.write_sinopsis(id_movie,desc)
            date = estreno.get().encode("utf-8")
            servitools.write_estreno(id_movie,date)
            genre = genero.get().encode("utf-8")
            servitools.write_genero(id_movie,genre)
            FanArt = fanart.get().encode("utf-8")
            servitools.write_fanart(id_movie,FanArt)
            poster = thumbnail.get().encode("utf-8")
            servitools.write_thumbnail(id_movie,poster)
            #print(desc)
            #print("La pelicula se agregara a Django")

        else:	
            print("Pelicula ya existe en Django, Solo se actualizaran los datos")
            name = titulo.get().encode("utf-8")
            servitools.write_titulo(id_movie,name)
            desc = txtsinopsis.get(1.0,END).encode("utf-8")
            servitools.write_sinopsis(id_movie,desc)
            date = estreno.get().encode("utf-8")
            servitools.write_estreno(id_movie,date)
            genre = genero.get().encode("utf-8")
            servitools.write_genero(id_movie,genre)
            FanArt = fanart.get().encode("utf-8")
            servitools.write_fanart(id_movie,FanArt)
            poster = thumbnail.get().encode("utf-8")
            servitools.write_thumbnail(id_movie,poster) 
    else:
        print(name+" No se agregara ningun dato")        

def ver_thumbnail():
    url_imagen = thumbnail.get()# El link de la imagen
    imagen_temp = "temp.jpg" # El nombre con el que queremos guardarla
    imagen = requests.get(url_imagen).content
    with open(imagen_temp, 'wb') as handler:
         handler.write(imagen)
    image = Image.open("./temp.jpg")
    image.save('thumbnail.png')
    image.show()
    image.close()
    #ver_thumbnail()
    

def agregar_DBLocal():
    pass    

root = Tk()
ventana1=Frame(root, width=1000, height=500)
ventana1.pack()




lblidtmdb = Label(ventana1, text="Id_tmdb:", fg="black", font=("Arial",12))
lblidtmdb.grid(row=0,column=0,sticky="w",padx=10,pady=10)
lbltitulo = Label(ventana1, text="Titulo:", fg="black", font=("Arial",12))
lbltitulo.grid(row=1,column=0,sticky="w",padx=10,pady=10)
lblcategoria = Label(ventana1, text="Categoria:", fg="black", font=("Arial",12))
lblcategoria.grid(row=2,column=0,sticky="w",padx=10,pady=10)
lblsinopsis = Label(ventana1, text="Sinopsis:", fg="black", font=("Arial",12))
lblsinopsis.grid(row=3,column=0,sticky="w",padx=10,pady=10)
lblestreno = Label(ventana1, text="Estreno:", fg="black", font=("Arial",12))
lblestreno.grid(row=4,column=0,sticky="w",padx=10,pady=10)
lblgenero = Label(ventana1, text="Genero:", fg="black", font=("Arial",12))
lblgenero.grid(row=5,column=0,sticky="w",padx=10,pady=10)
lblfanart = Label(ventana1, text="Fanart:", fg="black", font=("Arial",12))
lblfanart.grid(row=6,column=0,sticky="w",padx=10,pady=10)
lblthumbnail = Label(ventana1, text="Thumbnail:", fg="black", font=("Arial",12))
lblthumbnail.grid(row=7,column=0,sticky="w",padx=10,pady=10)

idtmdb = StringVar()
txtboxidtmdb = Entry(ventana1, textvariable=idtmdb, width=10, text="", fg="black", font=("Arial",12))
txtboxidtmdb.grid(row=0,column=1,sticky="w",padx=10,pady=10)

titulo = StringVar()
txtboxtitulo = Entry(ventana1, textvariable=titulo, width=60,text="", fg="black", font=("Arial",12))
txtboxtitulo.grid(row=1,column=1,sticky="w",padx=10,pady=10)

categoria = StringVar()
txtboxcategoria = Entry(ventana1, textvariable=categoria,  width=60,text="", fg="black", font=("Arial",12))
txtboxcategoria.grid(row=2,column=1,sticky="w",padx=10,pady=10)

sinopsis = StringVar()
txtsinopsis = Text(ventana1, width=60,height=10, font=("Arial",12))
txtsinopsis.grid(row=3,column=1,sticky="w",padx=10,pady=10)
#scrollvert = Scrollbar(ventana1, command=txtsinopsis.yview)
#scrollvert.grid(row=3,column=2,sticky="nsew")
#txtsinopsis.config(yscrollcommand=scrollvert.set)

estreno = StringVar()
txtboxestreno = Entry(ventana1, textvariable=estreno, width=4, text="", fg="black", font=("Arial",12))
txtboxestreno.grid(row=4,column=1,sticky="w",padx=10,pady=10)

genero = StringVar()
txtboxgenero = Entry(ventana1, textvariable=genero, width=60, text="", fg="black", font=("Arial",12))
txtboxgenero.grid(row=5,column=1,sticky="w",padx=10,pady=10)

fanart = StringVar()
txtboxfanart = Entry(ventana1, textvariable=fanart,  width=60,text="", fg="black", font=("Arial",12))
txtboxfanart.grid(row=6,column=1,sticky="w",padx=10,pady=10)

thumbnail = StringVar()
txtboxthumbnail = Entry(ventana1, textvariable=thumbnail, width=60,text="", fg="black", font=("Arial",12))
txtboxthumbnail.grid(row=7,column=1,sticky="w",padx=10,pady=10)

bntconsultarTMDB = Button(ventana1, text="Consulta TMDB", command=consulta_tmdb)
bntconsultarTMDB.grid(row=4,column=2)

bntverthumbnail = Button(ventana1, text="Ver Thumbnail", command=ver_thumbnail)
bntverthumbnail.grid(row=5,column=2)

bntagregarDjangoDB = Button(ventana1, text="Agregar DjangoDB", command=agregar_DjangoDB)
bntagregarDjangoDB.grid(row=6,column=2)

bntagregarDBLocal = Button(ventana1, text="Agregar DBLocal", command=agregar_DBLocal)
bntagregarDBLocal.grid(row=7,column=2)

root.mainloop()
