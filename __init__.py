print('*'*40)
print('Seja muito bem vindo ao jogo de adivinhar... ')
print('*'*40)
numeroSecreto = 45
chute = int(input('Adivinhe meu número secreto: '))

if (numeroSecreto == chute):
    print('Uau... Acertou meu número secreto! ')
else:
    print('Puts... Você não acertou meu número secreto!! ')