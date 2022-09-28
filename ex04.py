  peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / altura ** 2
if imc > 18.5:
    print('Seu IMC é de {}, e está menor que 18,5. Você está abaixo do peso!'.format(imc)
elif imc > 18.5 and imc < 25:
