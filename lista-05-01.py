'''
Faça um programa que receba um e-mail e verifique se ele é válido. Obs: Para um e-mail ser válido considerar se possui “@”.
'''
import re

email = input('Digite seu e-mail: ')

if email.find('@') == -1:
    print('E-mail inválido! - Regra usando find')
else:
    print('E-mail válido! - Regra usando find')

regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'    

if re.search(regex_email, email):
    print('E-mail válido! - usando expresao regular completa')
else:
    print('E-mail inválido! - usando expresao regular completa')

if '@' in email:
    print('E-mail válido! - usando @')
else:
    print('E-mail inválido! - usando @')



