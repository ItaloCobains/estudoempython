contador_letras = lambda lista: [len(x) for x in lista]

lista_animal = ['cachorro', 'gato', 'elefante']

print(contador_letras(lista_animal))

soma = lambda a, b: a + b

print(soma(5, 20))

calculadora = {
    'soma': lambda a, b: a+b,
    'sub': lambda  a, b: a-b,
    'multi': lambda a, b: a*b,
    'div': lambda a, b: a/b
}

print(type(calculadora))
soma = calculadora['soma']
multipli = calculadora['multi']
print(soma(10, 5))
print(multipli(10, 2))
