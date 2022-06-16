x = input("number: ")  ##input() is always a str so we have to change its type

print(type(x))

x = int(x)

print(type(x))

###

a = int(input("Enter a num "))  #same effect as "x" but fewer lines.

print(type(a))


if a < 10:
    print("less than 10")
if a >= 10:
    print("greater than or equal to 10")


####

while a <= 20:
    a = a+1
    print(a)
print("a equals", a)
#This terminates with a=21 because when python sees a=20 in the "<=20"
#condition, it still meets the conditions of that loop which include the
#instruction of a=a+1. If it's only <, it ends at 20.
