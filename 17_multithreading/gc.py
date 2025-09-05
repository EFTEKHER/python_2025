

def g(a,b):
    lcm=0
    x=1
    if(b>a):
        a,b=b,a
        m=max(a,b)
        while(1):
          if(m%a==0 and m%b==0):
                lcm=m
                break
          m+=1
        
    else:
        a,b=a,b
        m=max(a,b)
        while(1):
          if(m%a==0 and m%b==0):
                lcm=m
                break
          m+=1
    return lcm  


if __name__ == "__main__":
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("lcm of two numbers is: ",g(a,b))   