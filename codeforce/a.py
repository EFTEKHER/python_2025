##for codeforce make a snippet
def solve():
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        if a%2==1 and  b%2==0 and a<b:
            print(2)
        elif a%2==0 and b%2==0 and a>b:
            print(3)
        elif a%2==0 and b%2==0 and a<b:
            print(2)    
        elif a%2==1 and b%2==1:
            print(-1)
        elif a%2==0 and b%2==1 and a>b:
            print(-1)     

if __name__ == "__main__":
    solve()                   