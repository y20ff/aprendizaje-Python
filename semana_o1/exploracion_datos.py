# esquema 
# definir variables 
# pedir nombre del usario 
# contar la cantidad de caracteres del nombre 
# calcular el valor ASCII de cada letra 
# calcular el valor binario del cada letra 
#calcular la cantidad de vocales y consonantes de la palabra 
# total de letras 
# total de vocales 
# total de consonantes 

# variables 
# name = (str) 
# total_de_vocales = (int) 
# total_de_consonantes = (int) 
# total_de_letras = (int) 

# funcion
nombre=input("ingrese su nombre ")

def cantidad_de_letras(nombre):
    total=(len(nombre))
    print(total)
    def vocales_y_consonantes(nombre):
        cv=0
        cc=0

        for letra in nombre:   # la linea determina lo que hay dentro del bucle 
             if letra in nombre =="":
              continue
             if letra.lower() in "aeiou":
                 cv += 1
                
             else:
                 cc+=1
                 
        print(f"tus cantidad de vocales es: {cv}")#siempre fuera del bucle (evita repeticion)
        print(f"tu cantidad de consonantes es : {cc}")#siempre fuer del bucle 
             
                
    vocales_y_consonantes(nombre)
cantidad_de_letras(nombre)

def binario(nombre):
    final1="" 
    final2="" 
    for letra in nombre:
        if letra == " ":
         continue
    else :
       final1=bin(ord(letra))
       final2=str(ord(letra))
        
    
     
    print(f"tu valor binario es {final1}") 
    print(f"tu valor ASCCI es de {final2}")
            
binario(nombre)



