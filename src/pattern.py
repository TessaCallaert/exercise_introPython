
# Print the pattern

#for i in range(1,6):
#    for j in range(1, i+1):
#        print("*", end = " ") #default is normaal gezien een enter waardoor we een nieuwe lijn beginnen nu veranderen we de default worden door een spatie 
#    print()


#for i in range(5,1,-1):
#    for j in range(1, i):
#        print("*", end = " ")
#    print()

#a = 6
#for i in range(1, a):
#    print("*" * i)

#alternatieve en kortere manier om patroon te maken 

a = 6
for i in range(1, a):
    b = ("* " * i)
    b = b[:-1]
    print(b)
for i in range(a-2, 0, -1):
    c = ("* " * i)
    c = c[:-1]
    print(c)

#spaties op het einde verwijderen 