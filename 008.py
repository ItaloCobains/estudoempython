from aula7 import Televisao
from Cal import Calculadora
from contador_palavras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = (contador_letras(lista))
    print(f'total de letras por palavras de lista: {total_letras}')
    print(teste())
