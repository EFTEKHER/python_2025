def x(n):
    for i in range(n):
        for j in range(n,i,-1):
            print(" ",end="")
        
        for j in range(2*i+1):
            print(chr((65+(j%2))),end="")
        print()
        
        

def xx(n):
    x=0
    for i in range(n):
        x=0
        for j in range(n,i,-1):
            x+=1
            print(x,end="")
        print()

if __name__ == "__main__":
    n=int(input("Enter the number of rows: "))
    x(n)
    xx(n)