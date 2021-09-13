arquivo = open('notas.txt', 'r')
lista = [1, 10]
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('Nao e possivel realizar divisao por zero') 
except IndexError:
    print('Erro ao acessar um indecce invalido da lista')
except Exception as ex:
    print(ex)
else:
    print('Execulta quando n ocorre except')
finally:
    print('sempre executa')
    arquivo.close
