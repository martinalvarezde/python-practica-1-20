print("bienvenidos al quest de cualquier cosa")

print("\npara contestar tiene que ingresar la letra de la alternativa en minusculas\n")

print("hacemos un previo aviso de que si su respuesta no se encuentra entre las respuestas validas no se aceptara. gracias")

nombre = input("\ningrese su nombre: ")

#0

print("\n1)Cual es la figura del ajedres que se mueve en L\n")

print("a) peon")

print("b) alfil")

print("c) caballo")

print("d) reina")

R_1 = input("\nTu respuesta:")

while R_1 not in ("a", "b", "c", "d"):

  R_1 = input("\nsi la respuesta no es a, b, c o d no sera valida. ingrese su respuesta nuevamente: ")

if R_1 == "a":

  print("\nel peon se mueve hacia adelante")

elif R_1 == "b":

  print("\nel alfil se mueve en x")

elif R_1 == "d":

  print("\nla reina se mueve en + y x")

else:

  print("\nbuena", nombre, "estubo de ruta")


#1

print("\n2) Cual de estos paises no esta en america\n")

print("a) el salvador")

print("b) chile")

print("c) madagascar")

print("d) brasil")

R_2 = input("\nTu respuesta:")

while R_2 not in ("a", "b", "c", "d"):

  R_2 = input("\nsi la respuesta no es a, b, c o d no sera valida. ingrese su respuesta nuevamente: ")

if R_2 == "a":

  print("\nel salvador esta en mesoamerica")

elif R_2 == "b":

  print("\nchile es el pais mas pulento de america man como no sabias que desepcion")

elif R_2 == "d":

  print("\nbrasil esta al sudamerica")

else:

  print("\nbuena", nombre, "estubo de ruta")


#2

print("\n3) Cual de las sigientes armas no es un fusil\n")

print("a) m4")

print("b) glock19")

print("c) ak-47")

print("d) XCR-M")

R_3 = input("\nTu respuesta:")

while R_3 not in ("a", "b", "c", "d"):

  R_3 = input("\nsi la respuesta no es a, b, c o d no sera valida. ingrese su respuesta nuevamente: ")

if R_3 == "a":

  print("\nla m4 es un fusil muy conosido en los shooters")

elif R_3 == "c":

  print("\nla ak-47 es un fusil tipico de los terroristas")

elif R_3 == "d":

  print("el XCR-M es un fusil no muy conosido asi que te lo perdono")

else:

  print("\nbuena", nombre, "estubo de ruta")


#3

print("\n4) cual de los siguientes vehiculos es un avion\n")

print("a) Hultiminio")

print("b) Shelby Cobra")

print("c) Dodge Viper")

print("d) F-15IA")

R_4 = input("\nTu respuesta:")

while R_4 not in ("a", "b", "c", "d"):

  R_4 = input("\nsi la respuesta no es a, b, c o d no sera valida. ingrese su respuesta nuevamente: ")

if R_4 == "a":

  print("\nel hultiminio es un barco crack")

elif R_4 == "b":

  print("\nel shelby cobra es un vehiculo deportivo antiguo")

elif R_4 == "c":

  print("\nel dondge viper es un vehiculo superdeportivo")

else:

  print("\nbuena", nombre, "estubo de ruta")

#4

print("\n5) porque el platano es curvo\n")

print("a) casualidad")

print("b) porque crese en la direccion del sol")

print("c) por estoro de su semilla")

print("d) porque asi quiso diosito")

R_5 = input("\nTu respuesta:")

while R_5 not in ("a", "b", "c", "d"):

  R_5 = input("\nsi la respuesta no es a, b, c o d no sera valida. ingrese su respuesta nuevamente: ")

if R_5 == "a":

  print("\nnada es casualidad")

elif R_5 == "c":

  print("\nel platano no crese por semilla crack")

elif R_5 == "d":

  print("\ndices que a diosito le gusta doblada")

else:

  print("\nbuena", nombre, "estubo de ruta")


#5

print("\n5) en que se inspiro el creador de tesla al ponerle el nombre a su hija")

print("a) en nada")

print("b) un avion")

print("c) un tanque")

print("d) su empresa")

R_6 = input("\nTu respuesta:")

while R_6 not in ("a", "b", "c", "d"):

  R_6 = input("\nsi la respuesta no es a, b, c o d no sera valida. ingrese su respuesta nuevamente: ")

if R_6 == "b":

  print("\nno man")

elif R_6 == "c":

  print("\nno man")

elif R_6 == "d":

  print("\nno man")

else:

  print("\nbuena", nombre, "estubo de ruta")


#6



#fin

print("\ngracias por jugar", nombre,"\nhasta la proxima")