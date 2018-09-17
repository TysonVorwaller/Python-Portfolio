import math

def pythagoras_theorem(ap=1,bp=1):
	a=float(ap)
	b=float(bp)
	c=a*a+b*b
	c=math.sqrt(c)
	print("the third side is",c)



#pythagoras_theorem(3,4)

def add_numbers(x,y):
    num1= x
    print("num1= x " , num1)
    num2= y
    print("num2 = y ", num2)
    num3= int(num1)+int(num2)
    return num3

x=input("enter a number")
y=input("enter a number")
num4 = add_numbers(x,y)
print(num4)

#get name function
def get_name(name):
    input_name = name
    input_name=input_name.lower()
    input_name=input_name.title()

    print("the name you entered was", name)

    #verify name
    input("is this correct yes or no ")

print"this is our function"
    

