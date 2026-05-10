print("Swapping of two numbers\ninput num_1 and num_2\nwe are using 4 types of methods")
#+------------------------------------------------------------+
#METHOD-1: Using a Temp variable:

num_1=float(input("Enter num_1:")) 
num_2=float(input("Enter num_2:"))
Temp=num_1
num_1=num_2
num_2=Temp
print(num_1,num_2)
#+------------------------------------------------------------+
#METHOD-2: Using a Tuple:

num_1=float(input("Enter num_1:"))
num_2=float(input("Enter num_2:"))
num_1,num_2=num_2,num_1
print(num_1,num_2)
#+------------------------------------------------------------+
#METHOD-3: Using addition and subtraction:

num_1=float(input("Enter num_1:"))
num_2=float(input("Enter num_2:"))
num_1=num_1+num_2
num_2=num_1-num_2
num_1=num_1-num_2
print(num_1,num_2)
#+------------------------------------------------------------+
#METHOD-4: Using XOR:

num_1=int(input("Enter num_1:"))
num_2=int(input("Enter num_2:"))
num_1=num_1^num_2
num_2=num_1^num_2
num_1=num_1^num_2
print(num_1,num_2)
#+------------------------------------------------------------+1
input()