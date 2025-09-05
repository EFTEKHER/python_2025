def fun( x,y):
    if(x==0):
        return y
    return fun(x-1,x+y)


if __name__ == "__main__":
    print(fun(4,3))