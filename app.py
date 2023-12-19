# divisão por dois números

numero1 = float(input('Entre com o primeiro número: '))
numero2 = float(input('Entre com o segundo número: '))
try:
    resultado = numero1 / numero2
    print("O resultado é: ", resultado)
except ValueError:
    print('Valor inválido')
except ZeroDivisionError:
    print('Não e possível dividir por zero')
input('Pressione enter para sair')
