def gene(c):
    if (len(c)==1):
        return [c]
    results=[]
    for i in range(len(c)):
        x = c[i]
        rem=c[:i]+c[i+1:]
        for p in gene(rem):
            results.append(x+p)
    return results

if __name__ == "__main__":
    c = "abc"
    print(gene(c))