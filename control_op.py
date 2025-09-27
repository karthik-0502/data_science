def control_op(a,b,ops):
   
    if ops == "add":
        print(a+b)
    elif ops == "sub":
        print(a-b)
    elif ops == "mul":
        print(a*b)
    elif ops == "div":
        print(a/b)
    else:
        print("invalid operation")

    
control_op(5,2,"mul")
