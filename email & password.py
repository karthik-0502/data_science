#take ueser name and password from the user and store it in a dict
#store thre user names and password
#when the user name and password is entered if it  does not exist in the dict ask the user to not login else that user exist 

data = {'ramesh214@gmail.com':[22, 'vizag', 'student', 'ramesh2147'], 'suresh21@gmail.com':[25, 'hyderabad', 'student', 'suresh2147'],
        'subash312@gmail.com':[32, 'ongole', 'employe', 'subash2147']}
user = input("enter the email id: ")
user_password = input('enter the password: ')
if data.get(user)== None:
    print("the user details does not exist")

elif user in data:
    if data[user] == user_password:
        print("your details are present")
        print(data.get(user))
    else:
        print('check your password')
else:
    print('the user details are present')

