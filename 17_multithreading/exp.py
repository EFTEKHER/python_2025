import math

def ee(n,x):
    sum=0
    s="1"
    for i in range(n):
        sum+=((pow(i,x)/math.factorial(i)))
        s+=f"+x^{i+1}/{i+1}!"
    print(s)    
    return sum


if __name__ == "__main__":
    n=int(input("Enter the number of terms: "))
    x=int(input("Enter the value of x: "))
    print(f"e^{x} is approximately equal to: {ee(n,x)}")    
        
        