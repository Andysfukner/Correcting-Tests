#Programa para saber quais materiais preciso levar para a sala de aula

def funcao():
    if lesson in cards and lesson in documentos:
        print('\nPrecisa de cards e documento impresso')
    elif lesson in cards:
        print('\nPrecisa de cards')
    elif lesson in documentos:
        print('\nPrecisa de documento impresso')
    else:
        print('\nNão precisa cards ou documentos\n')

while True:
    book = int(input("\nQual o livro do aluno? "))
    while True:
        if book < 1 or book > 5:
            print(f"\nnão temos o Book {book}")
            book = int(input("Qual o livro do aluno? "))
        else:
            break
        
    lesson = int(input("Qual lesson será realizada? "))

    if book == 1:
        cards = [2, 7, 8, 14, 15, 17, 23, 25, 26, 29]
        documentos = [11, 14, 17, 20, 23]

    elif book == 2:
        cards = [14, 18, 26, 28, 30]
        documentos = [12, 20]

    elif book == 3:
        cards = [6, 16, 18, 20]
        documentos = [8, 18, 22]

    elif book == 4:
        cards = [14]
        documentos = [8, 16, 28]

    elif book == 5:
        cards = [6, 14, 18, 22, 24]
        documentos = [2, 8, 16, 20, 26, 28]
        
    funcao()

    sair = input('Deseja sair? (s/n) ')
    print('=' * 80)
    if sair == "s".lower():
        break
