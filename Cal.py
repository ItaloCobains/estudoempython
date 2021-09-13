class Calculadora:   
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b

    def multi(self):
        return self.valor_a * self.valor_b

    def div(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10, 3)
    print(calculadora.valor_a)
    print(calculadora.soma())
    print(calculadora.sub())
    print(calculadora.div())
    print(calculadora.multi())

# print(soma(1, 2))
# print(soma(3, 4))
# print(sub(4, 8))
# print(multi(4, 4))
# print(div(4, 2))
