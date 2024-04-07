''' 
 lista 03 - questão 02
 Escreva um algoritmo que receba o código correspondente ao cargo de um funcionário
 de uma escola e seu salário atual. Mostre o valor do novo salário, com aumento,
 conforme tabela abaixo: 
 Código  Cargo       Aumento
   1     Secretário  45%
   2     Tesoureiro  35%
   3     Professor   25%
   4     Coordenador 15%
   5     Diretor     Não tem aumento
 '''
codigo_cargo = ''
salario_atual = 0

while True:
   print('Entre o código correspondente ao cargo de um funcionário')
   codigo_cargo = int(input('ou "0" para encerrar: '))
   if codigo_cargo == 0:
      break
   elif codigo_cargo < 1 or codigo_cargo > 5:
      print("Código deve ser valor entre 1 e 5!")
      continue
   salario_atual = float(input('Entre com valor do salario atual: '))
   if codigo_cargo == 1:
      salario_atual = salario_atual + (salario_atual * 0.45)
   elif codigo_cargo == 2:
      salario_atual = salario_atual + (salario_atual * 0.35)
   elif codigo_cargo == 3:
      salario_atual = salario_atual + (salario_atual * 0.25)
   elif codigo_cargo == 4:
      salario_atual = salario_atual + (salario_atual * 0.15)
   elif codigo_cargo == 5:
      salario_atual = salario_atual + (salario_atual * 0)
   print(f'O novo salário é de R${salario_atual:.2f}.')
