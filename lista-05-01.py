'''
Faça um programa que leia um número indeterminado de valores, correspondentes a idades, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    ○ Mostre a quantidade de idades válidas; 
    ○ Exiba as idades armazenadas;
    ○ Calcule e mostre a média e mediana(*) das idades;
    ○ Calcule e mostre a quantidade de idades acima da média e mediana(*) calculada;
    ○ Exiba a maior e menor idade;
    ○ Calcule e mostre a quantidade de valores abaixo de 18.

    (*) A mediana foi adicionada para treinar o algoritmo.
'''

def media(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma / len(lista)

def mediana(lista):
    lista.sort()
    # se o tamanho da lista for par, retorna a média dos dois valores do meio
    if len(lista) % 2 == 0:
        return (lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2
    # se o tamanho da lista for ímpar, retorna o valor do meio
    else:
        return lista[len(lista) // 2]

idades = []
while True:
    idade_digitada = 0
    idade_digitada = input('Digite uma idade ou -1 para sair:')
    if idade_digitada == '-1':
        break
    try:
        idades.append(int(idade_digitada))
    except ValueError:
        print('Valor Inválido. A idade deve ser um número inteiro!')
        continue
    print(f'A idade {idade_digitada} foi adicionada com sucesso!')
    print('\n'*2)

media_idades = media(idades)
mediana_idades = mediana(idades)
# usando list comprehension para montar a lista de idades maiores que a média
idades_media = [idade for idade in idades if idade >= media_idades]
# usando list comprehension para montar a lista de idades menores que a mediana
idades_mediana = [idade for idade in idades if idade >= mediana_idades]
# usando list comprehension para montar a lista de idades abaixo de 18
idades_menores = [idade for idade in idades if idade < 18]

print(f'Foram digitadas {len(idades)} idades válidas')
print(f'idades: {idades}')
print(f'A média das idades é de {media_idades:.2f}')
print(f'A mediana das idades é de {mediana_idades:.2f}')
print(f'Foram digitadas {len(idades_media)} idades maiores ou igual a média')
print(idades_media)
print(f'Foram digitadas {len(idades_mediana)} idades maiores ou igual a mediana')
print(idades_mediana)
print(f'Foram digitadas {len(idades_menores)} idades abaixo de 18')
print(idades_menores)
print(f'A maior idade é de {max(idades)}')
print(f'A menor idade é de {min(idades)}')


