# Intento de traductor de binario a base 10
#EL numero entra como STR para poder recoger los caracteres de este 
number = str(input("Binario a traducir(máximo 8 caracteres): ")); 
total = 0;
one = {number[-1]}
two = {number[-2]}
four = {number[-3]}
eight = {number[-4]}
sixteen = {number[-5]}
thirtyTwo = {number[-6]}
SixtyFour = {number[-7]}
hundredTwenty = {number[-8]}
if one == "1":
    total +=1;
if two == "1":
    total +=2;
if four == "1":
    total +=4;
if eight == "1":
    total +=8;
if sixteen == "1":
    total +=16;
if thirtyTwo == "1":
    total +=32;
if SixtyFour == "1":
    total += 64;
if hundredTwenty == "1":
    total += 128;
print("the total is:",total);