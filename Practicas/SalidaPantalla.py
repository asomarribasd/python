x = 'foo'
x
#So the name x is attached to 'foo' string. When you call for example repr(x) the iterpreter puts 'foo' instead of x and then calls repr('foo').

repr(x)

x.__repr__()

#repr actually calls a magic method __repr__ of x, which gives the string containing the representation of the value 'foo' assigned to x. So it returns 'foo' inside the string "" resulting in "'foo'". The idea of repr is to give a string which contains a series of symbols which we can type in the interpreter and get the same value which was sent as an argument to repr.

eval("'foo'")
#When we call eval("'foo'"), it's the same as we type 'foo' in the interpreter. It's as we directly type the contents of the outer string "" in the interpreter.

#eval('foo')

str(x)

x.__str__()

#str is just the string representation of the object (remember, x variable refers to 'foo'), so this function returns string.

str(5)
#String representation of integer 5 is '5'.

str('foo')
#And string representation of string 'foo' is the same string 'foo'.



# Salida formateada a texto
print (str(1.0/7.0))
# repr es la evaluacion a texto de un objeto, notese que no truca
print (repr(1.0/7.0))


#Texto se puede formatear en columnas, y aplicar alineaciones
for x in range(1, 15):
	print ('Potencias'.ljust(10), 'Centro'.center(10), repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
    # Note trailing comma on previous line indica que se despliegan en columnas

# Otra maenra es crear un formato, y enviar los datos a desplegar en cada bracket 
for x in range(1,11):
    print ('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))






#zfill me ayuda a rellenar con zeros a la izquierda para que un monto tenga siempre el mismo numero de digitos
print ('12'.zfill(5))
print ('-3.14'.zfill(7))
print ('3.14159265359'.zfill(5))


# Pasando parametros a un texto, cada bracket se refiere a una variable y puede contener un formato
print 'We are the {} who say "{}!"'.format('knights', 'Ni')


# El numero indica la pocioncion del parametro a desplegar
print '{0} con {1}'.format('pan', 'mermelada')
print '{1} con {0}'.format('pan', 'mermelada')

# tambien se les puede poner nombre a los parametros
print 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')
# Mezclar methodos es poco frecuente pero posible
print 'Las aventuras de {0}, {1}, y {heroe}.'.format('Juan', 'Jose', heroe='Yo')

# tambien podemos incluir el formato dentro del bracket
import math
print 'El valor de PI es {}.'.format(math.pi)
print 'El valor de PI es {!r}.'.format(math.pi)
# con : separamos el indentificador del parametro de su formato
print 'El {texto} de PI es {0:.3f}.'.format(math.pi, texto='valor')



tabla = {'Jose': 1949, 'Juan': 1821, 'Maria': 1917}
for name, phone in table.items():
     print '{0:10} ==> {1:10d}'.format(name, phone)





