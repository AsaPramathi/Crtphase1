#PRIME OR NOT
'''def is_prime():
    num=int(input("enter a number:"))
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break            
is_prime()'''


#prime or not
'''def is_prime():
    f=1
    num=int(input("enter a number:"))
    for i in range(2,num):
        if num%i==0:
            f=0
            break
    if f==0:
        print("not prime")
    else:
        print("prime")
             
is_prime()'''

#average
'''def average(a,b,c):
    avg=(a+b+c)/3
    print(avg)
average(30,40,50)'''



#LOGIN_INFO
'''def login():
    f=1
    while f!=0:
        name=input("enter your name:")
        pw=input("enter your password:")
        if name==pw:
            print("logged in successfully")
            f=0
            break 
        else:
            print("enter correct details")
    
login()'''

#login info
'''def login():
    
    while True:
        name=input("enter your name:")
        pw=input("enter your password:")
        if name==pw:
            print("logged in successfully")
            
            break 
        else:
            print("enter correct details")
    
login()'''

#CHECK
def check(n):
    if n%10==5:
        return (n**2)
    elif n%10==3:
        return (n**3)
    elif n%10==6:
        return (n-1)
    else:
        return (n/2)
    
a=check(27)
print(a)
    
    
    
