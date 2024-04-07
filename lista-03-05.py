''' 
 lista 03 - questão 05
 Um hotel de luxo deseja automatizar seu sistema de reservas. 
 Eles possuem três tipos de suítes: Standard, Luxo e Presidencial. 
 Cada tipo de suíte tem uma quantidade limitada de noites que pode ser reservada a um preço diferente. 
 O hotel definiu as seguintes regras: 
   1. Suíte Standard: Custa R$ 250 por noite, limite de 15 noites. 
   2. Suíte Luxo: Custa R$ 500 por noite, limite de 10 noites. 
   3. Suíte Presidencial: Custa R$ 1200 por noite, limite de 7 noites. 
 Além disso, se o cliente desejar ficar 5 noites ou mais, ele recebe um desconto de 10% no 
 valor total, independentemente do tipo de suíte escolhida. 
 Escreva um programa que peça ao usuário para escolher o tipo de suíte, a quantidade de noites e 
 informe o valor total da estadia. 
 Se a quantidade de noites informada for maior que o limite disponível, informe ao usuário e 
 finalize o sistema.
 '''
while True:
   tipo_suite = 0
   quantidade_de_noites = 0
   standard = ('Standard',250, 15)
   luxo = ('Luxo',500, 10)
   presidencial = ('Presidencial', 1200, 7)
   suites = [standard, luxo, presidencial]
   
   print('Escolha o tipo de suíte dentre as opções ou digite -1 para sair:')
   print('1 - Standard')
   print('2 - Luxo')
   print('3 - Presidencial')
   try:
      tipo_suite = int(input())
      if tipo_suite == -1:
         break
      if tipo_suite < 1 or tipo_suite > 3:
         print('Valor Inválido. O tipo de suíte deve ser um número inteiro entre 1 e 3!')
         continue
      quantidade_de_noites = int(input('Digite a quantidade de noites: '))   
      valor_total = suites[tipo_suite - 1][1] * quantidade_de_noites 
      if quantidade_de_noites > suites[tipo_suite - 1][2]:
         print(f'Valor de noites acima do limite de {suites[tipo_suite - 1][2]} noites')
         break
      if quantidade_de_noites > 5:
         valor_total = valor_total * 0.9
      print(f'Valor total da estadia: R${valor_total:.2f}')
   except ValueError:
      print('Valor Inválido. O tipo de suíte e a quantidade de noites deve ser um número inteiro!')
      continue
   
   
   
  