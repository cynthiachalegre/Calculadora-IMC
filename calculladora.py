altura = float(input("Informe sua altura em metros: "))
peso = float(input("Informe seu peso em Kg: "))
 
imc = peso / altura**2
 
print("Seu IMC é: %.4f" % imc)
 
if imc < 18.5:
    print("Seu IMC está abaixo do peso.")
elif imc < 24:
	print("Seu IMC indica peso normal.")
elif imc < 30:
	print("Seu IMC indica sobrepeso.")
else:
	print("Seu IMC indica obesidade.")
 
exit()