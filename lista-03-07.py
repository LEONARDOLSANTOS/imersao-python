''' 
 lista 03 - questão 07
   Uma operadora de telefonia móvel deseja oferecer planos personalizados para seus
   clientes. Eles oferecem três tipos de planos com diferentes franquias de minutos e
   internet:
      ● Plano Básico: 100 minutos e 5GB de internet por R$ 50.
      ● Plano Intermediário: 300 minutos e 10GB de internet por R$ 80.
      ● Plano Avançado: 500 minutos e 20GB de internet por R$ 120.
   Caso o cliente ultrapasse a franquia de minutos, será cobrado R$ 1 por minuto
   adicional. Se ultrapassar a franquia de internet, será cobrado R$ 10 por GB adicional.
   Escreva um programa que peça ao usuário para escolher um plano, informar quantos
   minutos e quantos GB ele utilizou no mês. O programa deve calcular e mostrar o valor
   total da fatura.
'''
# PLANO = ['NOME',franquia minutos,franquia internet,valor franquia]
PLANO_BASICO = ['Plano Básico',100,5,50]
PLANO_INTERMEDIARIO = ['Plano Intermediário',300,10,80]
PLANO_AVANCADO = ['Plano Avançado',500,20,120]
PLANOS = [PLANO_BASICO, PLANO_INTERMEDIARIO, PLANO_AVANCADO]

while True:
   tipo_franquia = 0
   minutos_consumidos = 0
   internet_consumida = 0
   valor_total = 0.0
   adicional_minutos = 0
   adicional_internet = 0

   print('\n'*5)
   print('Digite o tipo de franquia ou digite -1 para sair:')
   print('1. Plano Básico: 100 minutos e 5GB de internet por R$ 50.')
   print('2. Plano Intermediário: 300 minutos e 10GB de internet por R$ 80.')
   print('3. Plano Avançado: 500 minutos e 20GB de internet por R$ 120.')
   try:
      tipo_franquia = int(input())
      if tipo_franquia == -1:
         break
      if tipo_franquia < 1 or tipo_franquia > 3:
         print('Valor Inválido. O tipo de franquia deve ser um número inteiro entre 1 e 3!')
         continue
      print('Digite a quantidade de minutos:')
      minutos_consumidos = int(input())
      print('Digite a quantidade de internet:')
      internet_consumida = int(input())
      # calculo franquia de minutos
      if minutos_consumidos > PLANOS[tipo_franquia - 1][1]:
         adicional_minutos = minutos_consumidos - PLANOS[tipo_franquia - 1][1]
         valor_total = valor_total + adicional_minutos * 1.0
      # calculo franquia de internet
      if internet_consumida > PLANOS[tipo_franquia - 1][2]:
         adicional_internet = internet_consumida - PLANOS[tipo_franquia - 1][2]
         valor_total = valor_total + adicional_internet * 10.0
      # calculo valor total
      valor_total = valor_total + PLANOS[tipo_franquia - 1][3]
      print(f'Valor total da franquia {PLANOS[tipo_franquia - 1][0]} é de R${valor_total:.2f}')

   except ValueError:
      print('Valor Inválido. O tipo de sessão deve ser um número inteiro!')
      continue
#endwhile

   
   
  