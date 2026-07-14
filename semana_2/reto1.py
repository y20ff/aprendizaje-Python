"""
el codigo debe analizar nombres y debe conetener (un nombre de ingreso , total de vocales (imprimirlas en pantalla )
cantidad de consonantes , si la cantidad de letras es impar o par 
debe contener los siguientes requisitos;
minimos tres funciones separadas , listas, operador % .
"""

memoria=[]

def total_v():
    nombre=""
    contador=0
    vocales=""
    nombre= input ("ingrese un nombre : ")
    for i in nombre:
        if i.lower()in "aeiou":
            contador += 1
            vocales += i + ","

    memoria.append(nombre)
    
    print(f"tu cantidad de vocales son :  {contador} ")
    print(f"las vocales de tu nombre son : {vocales}")
total_v() 


def cantidad_C(memoria):
    contador= 0 
    consonates= ""
    for nombre  in memoria  :
        print(nombre)
        for letra in nombre:
            if letra.lower() not in "aeiou" and letra != " ":
                contador += 1
                consonates += letra +","
    
    print(f"tu cantidad de consonantes son : {contador} y tus consonates son :{consonates}")

cantidad_C(memoria)

def par_impar(memoria):
    par=[]
    impar=[]
    for nombre in memoria:
      if len(nombre) % 2 == 0 :
           par.append(nombre)
           print("tu nombre contiene una cantidad de caracteres par")
         
      else :
          impar.append(nombre)
          print("tu nombre contiene una cantidad impar de caracteres")
          
par_impar(memoria)