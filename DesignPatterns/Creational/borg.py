
# Clase Borg
class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state

#Clase heredando Borg
class YourBorg(Borg):
    pass

if __name__ == '__main__':
    #Se instancian dos objetos
    rm1 = Borg()
    rm2 = Borg()

    #Ambos comparten un mismo estado, por tanto un cambio lso afecta a todos
    rm1.state = 'Idle'
    rm2.state = 'Running'
    # rm1: Running
    # rm2: Running

    # Por tanto la salida es la misma
    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    # Nuevamente si cambia uno cambio el otro.
    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    # rm1: Zombie
# rm2: Zombie
    # Los id nos muestan que son objetos direntes, no es que son  referencias
    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))
    # rm1 id: 140732837899224
    # rm2 id: 140732837899296

    #Aun al instanciar un obejetgo heredado, la base cambia el estado y por eso todos los objetos cambian
    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))
# rm1: Init
# rm2: Init
# rm3: Init

### OUTPUT ###




