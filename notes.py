A = {1,2,3,4}
B = {3,1,6,7,9}
C = {4,1,6,7,9}
D = 2 #int
E = 2.8 #float
F = 1j #complex





print("La cardinalidad del conjunto A = {0} es {1}".format(A,len(A)))


print(A)
print(B)
print(A.union(B))
print(A.intersection(B))
print(A - B)

for i in range(1,37):  
 if i%2==0:
  print(i)  
  
z = float(D)
y = int(E)
v = complex(D)

print(z)
print(y)
print(v)
print(type(v))

#Variables de valor entero
x = 9
y = 64895
z = -325
print(x)
print(y)
#Esto te permite sumar dos variables directamente
print(y + z) 
#Variables con punto decimal
x = 1.10
y = 1.0
z = -35.59
print(x)
print(y - z)
#Variables con potencias
x = 35e3
y = 12e4
z = -87.7e100
#Variables con números imaginarios
x = 5j
y = 3 + 7j
z = 9 - 5j
print(x)
print(y + z)
x = 4
y = 3.1416
z = 6 - 9j
print(type(x))
print(type(y))
print(type(z))
#Conversión de datos
x = 1 # int
y = 2.8 # float
z = 1j # complex
#convertir int a float:
a = float(x)
#convertir float a int:
b = int(y)
#convertir int a complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c)) 



#OPCION2 !!!!!!!!!! NO FUNCIONA
print("OPCION2")
A=[1,2,3,4,5,2,3,4,7,9,5]
b=[]
for i in A:
    for 
    if i not in b:
        print(0)
    else:
        print(1)
        
        
A = (1,2,3,1)
b = len(A) != len(set(A))
print(int(b))







#EJERCICIO3 UNION 
print("EJERCICIO3")

sample_set = [11, 12, 13, 14]
list_of_num = [10, 11, 12, 13, 14, 15, 16]
# Iterate over all elements of list and
for elem in list_of_num:
    # add each element to the set
    sample_set.add(elem)
print(sample_set)




EJERCICIO4
print("=====EJERCICIO4=====")
A4 = [2, -3, 0, 1]
B4 = [-3, 4, 2, 5]
C4 = list(set(B4) - set(A4))
print(C4)