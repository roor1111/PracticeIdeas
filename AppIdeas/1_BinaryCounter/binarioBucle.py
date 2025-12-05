#Contadorbinario con bucle (primera práctica para entender [])
baseTwo = str(input("Give me the binary code (max 8 characters):"))
binaryReversed = baseTwo[::-1] #Con esto genero la misma cadena que se ha introducido por teclado 
power = 0
Total = 0
for caracter in binaryReversed:
    if caracter == "1":
        Total = Total + (2**power)
    power += 1
print(Total)