num1=20
num2=4

print("La suma es: ",(num1+num2))
print("La resta es: ",(num2-num2))
print("La multiplicacion es: ",num1*num2)
print("La division es: ",num1/num2)
print("La division exacta es: ",num1//num2)
print("La potencia es: ",num1**num2)

#Concatenacion en python

texto1="hola"
texto2="mundo"
textofinal = texto1 + " " + texto2

print(textofinal)
print("El saludo es: %s %s" %(texto1,texto2))
saludofinal = "Saludo {} {}".format(texto1,texto2)
print(saludofinal)

saludofinal2="Saludo 2: {y} {x}".format(x=texto1,y=texto2)
print(saludofinal2)

