##encoding=latin1

## Pedimos al usuario un numero y lo registramos en una variable
num = (int) (input("Dame un número: "))

## Vemos si el modulo entre 2 del número es igual a 0
if num%2==0 :
    ## Es par
    print(str(num) + " es par")
    # Sino 
else:
    ## Es impar
    print(str(num) + " es impar")