print('''==========================================
|     *** Area Calculator Program***|
------------------------------------------
|            Shape code list:            |
|            (R) Rectangle               |
|            (T) Trapezoid               |
|            (P) Parallelogram           |
|            (C) Circle                  |
------------------------------------------''')
Shape = input("Select Code [R,T,P,C]: ")
if Shape == "R" :
  print("You selected R = Rectangle")
  print('''
=======================================
          Area of Rectangle
=======================================
  Inputs width and height in cm. or m.''')
  Type = int(input('Select a unit code 1 (cm.) or 2 (m.): '))
  if Type == 1 :
    Type = "cm2"
  elif Type == 2 :
    Type = "m2"
  width = int(input("Enter width : "))
  height = int(input("Enter height : "))
  Area = width*height
  print('''========================================
             Area = %d %s
========================================''' %(Area,Type))
elif Shape == "T":
  print("You selected T = Trapezoid")
  print('''
=======================================
          Area of Trapezoid
=======================================
  Inputs width and height in cm. or m.''')
  Type = int(input('Select a unit code 1 (cm.) or 2 (m.): '))
  if Type == 1 :
    Type = "cm2"
  elif Type == 2 :
    Type = "m2"
  a = int(input("Enter parallel side(a) : "))
  b = int(input("Enter parallel side(b) : "))
  height = int(input("Enter height : "))
  Area = 1/2*a+b*height
  print('''========================================
            Area = %d %s
========================================''' %(Area,Type))
elif Shape == "P":
  print("You selected P = Parallelogram")
  print('''
=======================================
           Area of Parallelogram
=======================================
  Inputs width and height in cm. or m.''')
  Type = int(input('Select a unit code 1 (cm.) or 2 (m.): '))
  if Type == 1 :
    Type = "cm2"
  elif Type == 2 :
    Type = "m2"
  base = int(input("Enter base : "))
  height = int(input("Enter height : "))
  Area = base*height
  print('''========================================
             Area = %d %s
========================================''' %(Area,Type))
elif Shape == "C":
  print("You selected C = Circle")
  print('''
=======================================
           Area of Circle
=======================================
  Inputs width and height in cm. or m.''')
  Type = int(input('Select a unit code 1 (cm.) or 2 (m.): '))
  if Type == 1 :
    Type = "cm2"
  elif Type == 2 :
    Type = "m2"
  radius = int(input("Enter radius : "))
  Area = 22/7*radius**2
  print('''========================================
             Area = %d %s
========================================''' %(Area,Type))
else :
  print('''You selected %s is Invalid shape code!
Please try again.''' % Shape)