#CALCULADORA EM PYTHON
def calculator(n):
	if(n == 1):
		num1 = int(input("Digite o primeiro número: "))
		num2 = int(input("Digite o segundo número: "))
		result = num1 + num2
		print("\nA soma %r + %r é: %r" %(num1,num2, result))

		print("\nDeseja efetuar uma nova operação?")
		m = input("Digite (s) para sim ou (n) para não: ")

		if(m == "s"):
			menu()

	elif(n == 2):
		num1 = int(input("Digite o primeiro número: "))
		num2 = int(input("Digite o segundo número: "))
		result = num1 - num2
		print("\nA subtração %r - %r é: %r" %(num1,num2, result))

		print("\nDeseja efetuar uma nova operação?")
		m = input("Digite (s) para sim ou (n) para não: ")

		if(m == "s"):
			menu()

	elif(n == 3):
		num1 = int(input("Digite o primeiro número: "))
		num2 = int(input("Digite o segundo número: "))
		result = num1 * num2
		print("\nA multiplicação %r * %r é: %r" %(num1,num2, result))

		print("\nDeseja efetuar uma nova operação?")
		m = input("Digite (s) para sim ou (n) para não: ")

		if(m == "s"):
			menu()

	elif(n == 4):
		num1 = int(input("Digite o primeiro número: "))
		num2 = int(input("Digite o segundo número: "))
		result = num1 / num2
		print("\nA divisão %r / %r é: %r" %(num1,num2, result))

		print("\nDeseja efetuar uma nova operação?")
		m = input("Digite (s) para sim ou (n) para não: ")

		if(m == "s"):
			menu()

	else:
		print("\nOPÇÃO INVÁLIDA!\nPOR FAVOR INSIRA UMA OPÇÃO VÁLIDA.\n")
		menu()


def menu():
	print("\n")
	print("-------------------PYTHON CALCULATOR-------------------")
	print("\n")
	print("( 1 ) - SOMA")
	print("( 2 ) - SUBTRAÇÃO")
	print("( 3 ) - MULTIPLICAÇÃO")
	print("( 4 ) - DIVISÃO")
	print("\n")

	n = int(input("Escolha o número da operação que deja efetuar: "))
	calculator(n)


menu()
