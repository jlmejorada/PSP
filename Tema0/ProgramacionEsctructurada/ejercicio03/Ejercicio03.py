## enconding=latin1

## Creamos una variable suma
suma=0

## Pedimos un n�mero y lo registramos
num=(int) (input("Dame un numero positivo: "))

## Mientras no se introduzca un n�mero negativo
while num>0:
    ## Sumamos el n�mero introducido
    suma+=num
    ## Pedimos otro n�mero
    num=(int) (input("Dame otro numero positivo: "))

## Mostramos por pantalla el resultado
print("La suma de los numeros da " + str(suma))
