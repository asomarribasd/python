

#class TextoTest:
def CrearArchivo(NombreArchivo):
	archivo=open(NombreArchivo, 'w')
	archivo.close()

def InsertarTexto(Texto, NombreArchivo):
	archivo=open(NombreArchivo, 'a')
	archivo.write(Texto)
	archivo.close

def LeerTexto(NombreArchivo):
    archi=open(NombreArchivo,'r')
    linea=archi.readline()
    print ('Inicia la lectura linea a linea')
    while linea!="":
        print (linea)
        linea=archi.readline()
    print ('Termino Lectura - Cerrar puntero a Archivo.')
    archi.close()

CrearArchivo('miarchivo.txt')
InsertarTexto('Mi primera linea\n', 'miarchivo.txt')
InsertarTexto('Mi segunda linea\n', 'miarchivo.txt')
InsertarTexto('Mi primera otra linea\n', 'miarchivo.txt')
InsertarTexto('Mi ultima linea linea\n', 'miarchivo.txt')
LeerTexto('miarchivo.txt')