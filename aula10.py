from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %b %d')
    print (data_atual_str)
    
def trabalhando_com_tome():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))
    
def trabalhando_com_datetime():
    data_atual = datetime.now()
    print (data_atual.strftime('%A/%B/%Y'))
    print (data_atual.strftime('%c'))
    print (data_atual.weekday())
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)    



if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_tome()
    trabalhando_com_datetime()
    