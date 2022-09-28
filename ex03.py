n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
print('[1] para SOMA (+).')
print('[2] para SUBTRAÇÃO (-).')
print('[3] para MULTIPLICAÇÃO (*).')
print('[4] para DIVISÃO (/).')
print('[5] para POTENCIAÇÃO (**).')

operacao = int(input("Digite a opção desejada: "))

if operacao == 1:
    print('A SOMA entre {} e {} é igual a {}.'.format(n1, n2, n1 + n2))
elif operacao == 2:
    print('A SUBTRAÇÃO entre {} e {} é igual a {}.'.format(n1, n2, n1 - n2))
elif operacao == 3:
    print('A MULTIPLICAÇÃO entre {} e {} é igual a {}.'.format(n1, n2, n1 * n2))
elif operacao == 4:
    print('A DIVISÃO entre {} e {} é igual a {}.'.format(n1, n2, n1 / n2))
else:
    print('A POTENCIAÇÃO entre {} e {} é igual a {}.'.format(n1, n2, n1 ** n2))
