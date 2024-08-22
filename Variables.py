#Variables

#todo en minusculas y _
my_variable = "My Variable String"
print(my_variable)

my_int_variable = 177
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#concatenacion de variables en print
print(my_variable, my_int_variable, my_bool_variable)


#int a string 
my_int_variable2 = str(my_int_variable)
print(my_int_variable2)
print(type(my_int_variable2))

#len() es para contar los caracteres
print(len(my_variable))

#variables en una linea  (NO RECOMENDABLE)
name, surname, age = "Homero", "Jesus", 21
print("Mi primer nombre es:", name, ". Mi segundo nombre es:" ,surname, ". Mi edad es:" ,age)

#pedir datos al usario
fist_name = input("What is your name?")
print(fist_name)

#se puede cambiar el tipo de la variable sin nigun problema
address = "Mi direccion"
print(address)
print(type(address))
address = True
print(address)
print(type(address))
address = 768
print(address)
print(type(address))
address = 3.14
print(address)
print(type(address))

