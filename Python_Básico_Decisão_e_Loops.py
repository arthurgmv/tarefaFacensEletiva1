# Soma de dois números: Peça ao usuário para inserir dois números e exiba a soma desses números
while True:
    try:
        num1 = int(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro.")

while True:
    try:
        num2 = int(input("Digite outro número: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro.")

soma = num1 + num2
print(f'A soma destes números é: {soma}')


# Par ou Ímpar: Escreva um programa que peça ao usuário para inserir um número inteiro e verifique se o número é par ou ímpar, exibindo a resposta.
while True:
    try:
        num = int(input("Digite um número: "))
        if num % 2 != 0:
            print(f'Este número: {num} é ímpar.')
        else:
            print(f'Este número: {num} é par.')
        break
    except ValueError:
        print("Por favor, digite um número inteiro.")


# Maior de três: Peça ao usuário para inserir três números e determine qual é o maior entre eles usando a estrutura de decisão if.
while True:
    try:
        num1 = int(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro.")

while True:
    try:
        num2 = int(input("Digite um segundo número: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro.")

while True:
    try:
        num3 = int(input("Digite um terceiro número: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro.")

if num1 > num2 and num1 > num3:
    print(f"O número {num1} é o maior dos três.")
elif num2 > num1 and num2 > num3:
    print(f"O número {num2} é o maior dos três.")
else:
    print(f"O número {num3} é o maior dos três.")


# Contagem de 1 a 10: Escreva um programa que use um loop for para imprimir os números de 1 a 10 na tela.
for num in range(1, 11):
    print(num)


# Tabuada de um número: Solicite um número ao usuário e exiba a tabuada desse número (de 1 a 10) usando um loop.
num = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')


# Verificação de idade: Peça ao usuário para inserir sua idade. Se a idade for maior ou igual a 18, exiba "Maior de idade", caso contrário, exiba "Menor de idade".
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")


# Soma de números pares de 1 a 100: Use um loop for para calcular a soma de todos os números pares de 1 a 100 e exiba o resultado.
soma = 0

for num in range(2, 101, 2):
    soma += num

print(f'A soma de todos os números pares de 1 a 100 é: {soma}')
