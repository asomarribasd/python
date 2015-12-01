

# typical try catch
try: 
    z=10/0
    print 'Esto no se ejecuta'
except:
    print 'Se produjo un error'
finally:
    print 'Siempre se ejecuta'



# if you add a type after the except is going to be evaluated, if it match then I will fall in that exception.
lista1=['juan','ana','carlos']
try: 
    print lista1[0]
    z=10/0
except IndexError:
    print 'El elmento que busca esta fuera de los limites de la lista'
except ZeroDivisionError:
    print 'No se puede dividir un numero entre cero, no es permitida'
else:
	print 'No se que paso!'


