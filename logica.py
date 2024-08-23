a = input("introduce valor 1:")
print(a)

b = input("introduce valor 2: ")
print(b)

c = input("introduce valor 3: " )
print(c)

if (a>b and a>c):
    print("el valor 1 es el mayor:","y es el siguiente:",a)
else:
    if (b>a and b>c):
     print("el valor 2 es el mayor:","y es el siguiente:",b)
    else:
       if (c>a and c>b):
          print("el valor 3 es el mayor ","y es el siguiente:",c)
       else:
          if (a==0 and b==0 and c==0):
             print("los 3 valores puestos son 0")