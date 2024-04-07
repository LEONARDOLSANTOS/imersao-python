# lista 03 - questão 01
# Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa e mostre uma
# mensagem com a sua descrição (Solteiro, Casado, Viúvo, Divorciado). Mostre uma
# mensagem de erro, se necessário.
resposta_usuario = ''

while True:
   print('Entre com primeira letra estado civil.')
   resposta_usuario = input('ou "sair" para encerrar: ').upper()
   if resposta_usuario == 'C':
      print("Casado")
   elif resposta_usuario == 'S':
      print("Solteiro")
   elif resposta_usuario == 'V':
      print("Viúvo")
   elif resposta_usuario == 'D':
      print("Divorciado")
   elif resposta_usuario == 'SAIR':
      break
   else:
      print("Entrada inválida!")

