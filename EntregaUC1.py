print("=====EJERCICIOS OBLIGATORIOS=====")

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


#EJERCICIO3 UNION No funciona cuando parantesis no es de punta
print("=====EJERCICIO3=====")
sample_set = {2, -3, 0, 1}
list_of_num = {-3, 4, 2}

for elem in list_of_num:
    # add each element to the set
    sample_set.add(elem)
print("C=", sample_set)



print("=====EJERCICIO4=====")
A4 = [2, -3, 0, 1]
B4 = [-3, 4, 2, 5]
C4 = []

for item in B4:
  if item not in A4:
    C4.append(item)
print("C=",C4)



print("=====EJERCICIO5=====")
A5 = [0, 2, 3]
B5 = [-1, 1]
#C5 = [(a, b) for a in A5 for b in B5]
#Bu boylesi niye calismiyor?
C5 = []
for a in A5:
    for b in B5:
        C5.append(a+b)
print("C= " + str(C5))



#=====EJERCICIOS OPCIONALES=====

#EJERCICIO 1

A10 = [2, -3, 0, 1]

for i in A10:
    if i == [i+1]
    print (curr_el)
        
#EJERCICIO2

#EJERCICIO3

#EJERCICIO4

#EJERCICIO5