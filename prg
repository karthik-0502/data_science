#2 list the num taht one is even and another one is odd
even_list = []
odd_list = []
x = int(input("enter the value: "))
result = x%2
if result == 0:
    even_list.append(x)
    print("it is an even number")
else:
    odd_list.append(x)
    print("it is an odd number")
    


