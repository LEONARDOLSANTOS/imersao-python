''' 
 lista 03 - questão 04
 Em uma cidade, a prefeitura deseja classificar os motoristas com base em suas infrações
 de trânsito no último ano. O objetivo é criar um programa de reeducação para os
 motoristas que cometem infrações. Para isso, eles definiram as seguintes categorias:
  a) Motorista Exemplar: Não cometeu nenhuma infração.
  b) Motorista Atento: Cometeu até 3 infrações.
  c) Motorista Desatento: Cometeu entre 4 e 6 infrações.
  d) Motorista Perigoso: Cometeu mais de 6 infrações.
 Escreva um programa que peça ao usuário para inserir o número de infrações que
 cometeu no último ano e informe em qual categoria ele se encaixa.
 Exemplo Entrada Exemplo Saída
   5 Categoria: Motorista Desatento
 '''
numero_infracao = 0
while True:
   print('Entre com número de infrações que cometeu no último ano')
   numero_infracao = int(input('ou "-1" para encerrar: '))
   if numero_infracao == -1:
      break

   if numero_infracao == 0:
      print('Categoria: Motorista Exemplar')
   elif numero_infracao <= 3:
      print('Categoria: Motorista Atento')
   elif numero_infracao <= 6:
      print('Categoria: Motorista Desatento')
   elif numero_infracao > 6:
      print('Categoria: Motorista Perigoso')

  