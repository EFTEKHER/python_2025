
def addBinary( a ,b):
        m=max(len(a),len(b))
        a=a.zfill(m)
        b=b.zfill(m)
        c=0
        reversed_a=a[::-1]
        reversed_b=b[::-1]
        sum=""
        for i in range(m):
            x=int(reversed_a[i])+int(reversed_b[i])+c
            if x==0:
                sum+="0"
                c=0
            elif x==1:
                sum+="1"
                c=0
            elif x==2:
                sum+="0"
                c=1
            else:
                sum+="1"
                c=1
        if c==1:
            sum+="1"
        print(sum[::-1])
if __name__=="__main__":
    addBinary("1010","1101")