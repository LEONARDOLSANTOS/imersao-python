''' 
 lista 03 - questão 06
 Uma rede de cinemas deseja criar um sistema para controlar a venda de ingressos. Eles possuem três tipos de sessões: Matinê, Vespertina e Noturna. Cada sessão tem um preço diferente. As regras são:
   1. Sessão Matinê: Custa R$ 20.
   2. Sessão Vespertina: Custa R$ 25. 
   3. Sessão Noturna: Custa R$ 30.
  Crianças até 12 anos, estudantes e idosos (65+) têm direito a 50% de desconto em qualquer sessão. 
  Escreva um programa que peça ao usuário para escolher o tipo de sessão e informar a idade. Caso o usuário não seja idoso ou criança, ele deverá informar se é estudante. O programa deve informar o valor total da compra.
'''
matine = ('Matinê',20)
vespertina = ('Vespertina',25)
noturna = ('Noturna',30)
sessoes = [matine, vespertina, noturna]

while True:
   tipo_sessao = 0
   idade = 0
   resposta_estudante = ''
   valor_total = 0
   direito_desconto = False
   print('\n'*5)
   print('Escolha o tipo de Sessão dentre as opções ou digite -1 para sair:')
   print('1. Sessão Matinê: Custa R$ 20.')
   print('2. Sessão Vespertina: Custa R$ 25. ')
   print('3. Sessão Noturna: Custa R$ 30.')
   try:
      tipo_sessao = int(input())
      if tipo_sessao == -1:
         break
      if tipo_sessao < 1 or tipo_sessao > 3:
         print('Valor Inválido. O tipo de Sessão deve ser um número inteiro entre 1 e 3!')
         continue
      idade = int(input('Digite sua idade: '))   
      
      if idade <= 12 or idade >= 65:
         direito_desconto = True
      else:
         while resposta_estudante!= 'S' and resposta_estudante!= 'N':
            print('Estundante? Entre com "S" para sim e "N" para não:')
            resposta_estudante = input().upper()
            if resposta_estudante == 'S':
               direito_desconto = True
               break
            elif resposta_estudante == 'N':
               direito_desconto = False
               break
            else:
               print('Valor Inválido. Resposta deve ser "S" para sim ou "N" para não!')
      valor_total = sessoes[tipo_sessao - 1][1] 
      if direito_desconto:
         valor_total = valor_total - (valor_total * 0.5)
            
      print(f'Valor total da compra: R${valor_total:.2f}')
   except ValueError:
      print('Valor Inválido. O tipo de sessão deve ser um número inteiro!')
      continue
#endwhile

   
   
  