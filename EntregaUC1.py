#=====EJERCICIOS OBLIGATORIOS=====

#EJERCICIO1
print("=====EJERCICIO1=====")
A=[1, -1, 3]
x=[-1]

for element in x:
    if element in A:
        print("b=1")
    else:
        print("b=0")


#EJERCICIO2 INTERSECCION pregunta que significa : en el i
print("=====EJERCICIO2=====")
A2 = [2, -3, 0, 1]
B2 = [-3, 4, 2]
C2 = []

for i in A2:
    for y in B2:
        if y == i:
            C2.append(i)
            
print("C=", C2)

#o tambien se puede hacer asi
#C2=A2 & B2
#print("C=",C2)


#EJERCICIO3 UNION No funciona cuando parantesis no es de punta
print("=====EJERCICIO3=====")
sample_set = {11, 12, 13, 14}
list_of_num = {10, 11, 12, 13, 14, 15, 16}

for elem in list_of_num:
    # add each element to the set
    sample_set.add(elem)
print("C=", sample_set)

#o tambien se puede hacer asi
#C3=A3 | B3
#print("C=",C3)


#EJERCICIO4
print("=====EJERCICIO4=====")
A4 = [2, -3, 0, 1]
B4 = [-3, 4, 2, 5]
C4 = []

for item in B4:
  if item not in A4:
    C4.append(item)
print("C=",C4)


#EJERCICIO5
print("=====EJERCICIO5=====")



#=====EJERCICIOS OPCIONALES=====

#EJERCICIO 1

        
#EJERCICIO2

#EJERCICIO3

#EJERCICIO4

#EJERCICIO5