# x = 3
# y = float(3)
# print(x,y)

# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(values[0])
#     print(values[6])

# x = "this is a thing"
# y= x.split( )
# z = y[0]
#print(y)
#print(z)

# snet = input("counter")
# List = snet.split()
# def counter():
#     print (len(List))

# counter()

# day_of_week = input("what day is it? ")
# if day_of_week == "Friday":
#     print("correct")
# else:
#     print("incorrect")

# x= "test"
# print (f"hello{x}")

# temp = 75
# if temp > 68:
#   print ('warm')
# elif temp == 68 :
#   print ('perfect')
# else:
#   print ('cold')

# dumbahh = int(input("gimme yo numba :"))
# GCF = dumbahh%2
# if GCF == 0:
#  print ('even')
# else:
#  print ('nah thats odd, like your cut')

# base = int(input("bill"))
# qualitacally = int(input("quality. 1=great, 2=good, 3=okay, 4= i hope you burn and suffer and hell"))
# def bill():
#     if qualitacally == (1):
#         final = base + base * .25
#         print (final)
#     elif qualitacally == (2):
#         final = base + base * .20
#         print (final)
#     elif qualitacally == (3):
#         final = base + base * .15
#         print (final)
#     else:
#         final = base
#         print (final)
# bill()



numba = int(input("numbers"))
number = int(input("numbers2"))
if numba > number:
    small = number
else:
    small = numba
greatest = 0
for i in range (2, small +1):
    if numba%i == 0 and number%i == 0:
      greatest = i
print (greatest)