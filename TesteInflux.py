print('-'*80)

book = int(input("Qual o livro do aluno? "))
lista1 = [1,2]
lista2 = [3, 4, 5]

descontoReading = 0
descontoListening = 0.1

if book in lista1:
  descontoReading = 0.15
else:
  descontoReading = 0.12

def infos():
  listening = float(input("Quantos erros o aluno cometeu no listening test? "))
  reading = float(input("Quantos erros o aluno cometeu no reading test? "))
  composition = float(input("Qual a nota da composition? "))
  return listening, reading, composition 

def contas():
  nota = 8 - (listening * descontoListening) - (reading * descontoReading)  + composition   
  print("%.2f" %nota)

while True:
  if book not in lista1 and book not in lista2:
    print(f'Não temos o livro {book}')
    book = int(input("Qual o livro do aluno? "))
  else:
    break

while True:
  print('-'*80)
  listening, reading, composition = infos()

  print('-'*80)
  contas()
  print('-'*80)

  sair = input("Deseja sair? (s/n) ").lower()
  print('-'*80)
  if sair == "s":
    break