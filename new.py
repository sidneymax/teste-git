calculado = print("Selecione uma das opções abaixo: "
"> 1 - Soma "
"> 2 - Subtração "
"> 3 - Multiplicação "
"> 4 - Divisão")

calculo = float(input("Insira uma das opções acima com o número para efetuar o cálculo:"))

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite um segundo número:"))

soma = num1 + num2 
subtracao = num1 - num2 
multiplicacao = num1 * num2
divisao = num1 / num2

if calculo == 1:
    print(f"Seu resultado para a soma é igual a: {soma}")

elif calculo ==2:
    print(f"Seu resultado para a Subtração é igual a: {subtracao}")

elif calculo ==3:
    print(f"Seu resultado para a Multiplicação é igual a: {multiplicacao}")

elif calculo ==4:
    print(f"Seu resultado para a Divisão é igual a: {divisao}")

else:
    print("Por favor insira um número válido")
