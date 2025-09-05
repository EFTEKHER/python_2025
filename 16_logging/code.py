def tri(n):
    for i in range(n):
        for j in range(i,n):
            print(' ', end='')
       
        for k in range(i+1):
            print('*', end='')
        print()


def pri(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end='')
        for k in range(2*i+1):
           print(chr(65+k),end='')
        print()


def ul(n):
    for i in range(n):
        for j in range(i):
            print(' ',end='')
            
        for k in range(i,n):
            print('*',end='')
        for m in range(i,n-1):
            print('*',end='')  
        print()          
      
if __name__ == "__main__":
    n = 5
    tri(5)
    pri(5)
    ul(5)