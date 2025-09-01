def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        x=fibo(n-1)+fibo(n-2)
        return x


if __name__ == "__main__":
    print(fibo(5))  # Output: 55
   