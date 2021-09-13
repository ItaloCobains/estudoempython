class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
        
        
    def diminuir_canal(self):
        if self.ligada:
            self.canal -= 1
        
        
if __name__ == "__main__":
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)            
    televisao.power()
    print(televisao.ligada)
    televisao.power()
    print(f'canal {televisao.canal}')
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print(f'canal {televisao.canal}')
    televisao.diminuir_canal()
    print(f'canal {televisao.canal}')




















# class Calculadora:   
#     def soma(self, valor_a, valor_b):
#         return valor_a + valor_b

#     def sub(self, valor_a, valor_b):
#         return valor_a - valor_b

#     def multi(self, valor_a, valor_b):
#         return valor_a * valor_b

#     def div(self, valor_a, valor_b):
#         return valor_a / valor_b


# calculadora = Calculadora()

# print(calculadora.soma(1, 3))
# print(calculadora.sub(1, 3))
# print(calculadora.multi(1, 3))
# print(calculadora.div(1, 3))
