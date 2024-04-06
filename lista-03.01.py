# lista 03 - questão 01
resposta_usuario = ''

while True:
   print('Entre com primeira letra estado civil.')
   resposta_usuario = input('ou "sair" para encerrar: ').upper()
   print(resposta_usuario)
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
      print("nao aceito")


