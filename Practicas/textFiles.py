

#class TextoTest:
def CrearArchivo(NombreArchivo):
	archivo=open(NombreArchivo, 'w')
	archivo.close()

def InsertarTexto(NombreArchivo, Texto ):
	archivo=open(NombreArchivo, 'a')
	archivo.write(Texto)
	archivo.close

def LeerTextoPorLinea(NombreArchivo):
    # Abro el Archivo
    archivo=open(NombreArchivo,'r')
    linea=archivo.readline()
    print ('Inicia la lectura linea a linea')
    while linea!="":
        print (linea)
        # Notemos que durante la iteracion el puntero permanece abierto
        linea=archivo.readline()
    print ('Termino Lectura - Cerrar puntero a Archivo.')
    # Cierro el archivo 
    archivo.close()


def LeerTextoALista(NombreArchivo):
	# Abro el Archivo
    archivo=open(NombreArchivo,'r')
    # Lo leo a una lista de texto (cada item contiene una linea del archivo)
    lineas=archivo.readlines()
    # Cierro el archivo seguidamente
    archivo.close()
    # puedo trabajar el contenido del archivo que se encuentra en la lista en memoria.
    for linea in lineas:
        print linea

def LeerArchivoConObjetoLinea(NombreArchivo)
    archivo = open(NombreArchivo)
    try:
        for line in archivo:
            print line,
    finally:
        f.close()


CrearArchivo('miarchivo.txt')
InsertarTexto('Mi primera linea\n', 'miarchivo.txt')
InsertarTexto('Mi segunda linea\n', 'miarchivo.txt')
InsertarTexto('Mi otra linea\n', 'miarchivo.txt')
InsertarTexto('Mi ultima linea linea\n', 'miarchivo.txt')
LeerTextoPorLinea('miarchivo.txt')
