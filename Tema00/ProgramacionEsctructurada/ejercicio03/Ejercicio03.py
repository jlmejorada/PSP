## enconding=latin1

## Creamos una variable suma
suma=0

## Pedimos un número y lo registramos
num=(int) (input("Dame un numero positivo: "))

## Mientras no se introduzca un número negativo
while num>0:
    ## Sumamos el número introducido
    suma+=num
    ## Pedimos otro número
    num=(int) (input("Dame otro numero positivo: "))

## Mostramos por pantalla el resultado
print("La suma de los numeros da " + str(suma))
