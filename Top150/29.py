def sss(list1):
    list1.sort()
    x=[]    
    for i in range(len(list1)):
        if i>0 and list1[i]==list1[i-1]:
            continue
        s,l=i+1,len(list1)-1
        while(s<l):
            su=list1[i]+list1[s]+list1[l]
            if su>0:
                l-=1
            elif su<0:
                s+=1
            else:
                x.append([list1[i],list1[s],list1[l]])
                while s<l and list1[s]==list1[s+1]:
                    s+=1
                while s<l and list1[l]==list1[l-1]:
                    l-=1
                s+=1
                l-=1    
    return x


if __name__=="__main__":
    print(sss([-1,0,1,2,-1,-4]))
