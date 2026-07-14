contactos = {}

def agregar (contactos):
    name = input("escribe el nombre de tu contacto : ")
    num = input("escribe el numero telefonico - <= 10 : ")
    if len(num) > 10:
        print("tu numero contiene mas de diez digitos o no es numero")
        return
    
    if name in contactos:
        print("tu contacto ya existe en nuestra agenda")
        
    contactos[name] = num
    print("tu contacto ha sido guardado")


def buscar (contactos):
    name = input("ingresa el nombre de tu contacto : ")
    if name in contactos:
        print(f"tu conacto es :{name}:{contactos[name]}")
        

    else:
        print(f"{name} no existe en tu agenda ")
        return
    

def eliminar (contactos):
    name= input("ingresa el nombre de tu contacto : ")
    if name in contactos:
        contactos.pop(name)
        print("tu contacto ha sido eliminado correctamente")
    
    else:
        print("tu contacto ya ha sido eliminado o es inexistente")
        return

def menu ():
    while True:
         print("1:Agrega tu contacto")
         print("2:Busca tu contacto")
         print("3:Elimina tu contacto")
         print("4:Salir")

         selection = input("seleciona una de las opciones : ")

         if not selection.isdigit():
             print("por favor ingresa un numero")
             continue
         
         match int(selection):
             case 1:
                 agregar(contactos)
             case 2 : 
                 buscar(contactos)
             case 3 : 
                 eliminar(contactos)
             case 4 :
                 print("Hasta luego 🤝")
                 break
             
menu()