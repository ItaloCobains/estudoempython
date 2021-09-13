
class ERROR(Exception):
    pass

class InputError(ERROR):
    def __init__(self, message):
        self.message = message
        


while True:
    try:
        x = int(input('entre com um nuemro de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota n pode ser maior q 10') 
        elif x - 0:
            raise InputError('Nota n poder ser menor q 0')   
        break
    except ValueError:
        print('valor invalido, digite apensa numeros')
    except InputError as ex:
        print(ex)    


