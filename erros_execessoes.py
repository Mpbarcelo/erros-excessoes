def calcular_media(valores):
    tamanho = 0  
    soma = 0  
    for valor in valores:  
        soma += valor  
        tamanho += 1  
    if tamanho > 0:
        media = soma / tamanho  
        return media
    else:
        return 0  

valores = []

while True:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular a média: ')
    if valor.lower() == 'ok':
        break
    try:
        valor = float(valor)  
        valores.append(valor)  
    except ValueError:
        print('Por favor, insira um número válido.')

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {:.2f}.'.format(valores, media))
