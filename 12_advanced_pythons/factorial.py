def factorial(n):
    if n == 0:
        return 1
    else:
        x= n * factorial(n-1)
        return x




if __name__ == "__main__":
    print(factorial(5))  # Output: 120
     # Output: 1    