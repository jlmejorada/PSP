## encoding=latin1

## Pedimos un n�mero y lo guardamos en una variable
num1 = (int) (input("Dame un n�mero: "))

## Pedimos otro n�mero
num2 = (int) (input("Dame otro n�mero: "))

## Vemos si el primer n�mero es menor que el segundo
if num1<num2:
    ## Lo imprimimos
    print(str(num1) + " < " + str(num2))
    ## Si no
else:
    ## Lo imprimimos
    print(str(num2) + " < " + str(num1))