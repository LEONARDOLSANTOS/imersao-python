''' 
 lista 03 - questão 03
 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-
 Domingo, 2- Segunda, etc.). Exibir mensagem “Valor Inválido” caso um número
 inesperado for informado.
 '''
dia_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
numero_dia_da_semana = 0

while True:
   print('Entre com um número correspondente ao dia da semana.')
   numero_dia_da_semana = int(input('ou "0" para encerrar: '))
   if numero_dia_da_semana == 0:
      break
   elif numero_dia_da_semana < 1 or numero_dia_da_semana > 7:
      print("Valor Inválido. Número correspondente ao dia da semana deve ser valor entre 1 e 7!")
      continue
   print(f'Dia da semana: {dia_da_semana[numero_dia_da_semana - 1]}')
