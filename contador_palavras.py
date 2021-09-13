def contador_letras(lista__palavras):
    contador = []
    for x in lista__palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

def teste():
    print("test")

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))
