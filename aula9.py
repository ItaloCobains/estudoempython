import shutil
def escrever_arquivo(nome_e_local, texto):
    arquivo = open(nome_e_local, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close
    
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    
def media_notas(nome_arquivos):
    arquivo = open(nome_arquivos, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        #print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivos(nome_arquivos):
    shutil.copy(nome_arquivos, 'C:/Users/italo/Documents/cursos/python')
    
def move_arquivos(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/italo/Documents/cursos/python')

                
if __name__ == '__main__':
    #escrever_arquivo('primeira linha.\n')
    #aluno = 'cesar,0,10,5,5\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('texto1.txt')
    # lista_media = media_notas('notas.txt')
    # lista_media = str(lista_media)
    # escrever_arquivo('C:/Users/italo/Documents/cursos/Notas_atualizadas.xls', lista_media)
    #copia_arquivos('C:/Users/italo/Documents/cursos/Notas_atualizadas.txt')
    move_arquivos('C:/Users/italo/Documents/cursos/Notas_atualizadas.txt')
    
    