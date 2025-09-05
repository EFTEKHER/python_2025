def xi(li,a,b):
    count=0
    li.sort()
    li=set(li)
    li=list(li)
    n=len(li)
    for i in range(n):
        for j in range(i+1,n):
            if(li[i]+li[j]>=a and li[i]+li[j]<=b):
                count+=1
                print((li[i],li[j]))
    return count

if __name__ == "__main__":
    li=[3,4,1,2,5,6,4,7,10,8]
    print("Number of pairs whose sum lies in the range is: ",xi(li,5,10))            