## encoding=latin1

## Pedimos un número y lo guardamos en una variable
num1 = (int) (input("Dame un número: "))

## Pedimos otro número
num2 = (int) (input("Dame otro número: "))

## Vemos si el primer número es menor que el segundo
if num1<num2:
    ## Lo imprimimos
    print(str(num1) + " < " + str(num2))
    ## Si no
else:
    ## Lo imprimimos
    print(str(num2) + " < " + str(num1))