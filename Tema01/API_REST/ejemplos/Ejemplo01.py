#coding: latin1
from pip._vendor import requests

salir = False;
api_url = "https://jsonplaceholder.typicode.com/todos/"


while(salir is False):

    num = int(input("Introduzca el número de id que quiera ver (1-10), con el 0 sales\n"))
    
    if(num>0):
        response = requests.get(api_url+str(num))
        print(response.json())
    elif(num<0):
        print("Opción Incorrecta.\n")
    else:
        salir = True

print("Adiós")