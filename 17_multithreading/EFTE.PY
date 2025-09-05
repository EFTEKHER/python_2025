def sub(s):
   a=s[0]
   b=s[1]
   c=s[2]
   x=""
   x+=a
   x+=b
   x+=c
   n=int(x)
   
   if(n>=0 and n<=127):
       print("Class A")
   elif(n>=128 and n<=191):
       print("Class B")
   elif(n>=192 and n<=223):
       print("Class C")
   elif(n>=224 and n<=239):
       print("Class D")
   elif(n>=240 and n<=255):
       print("Class E")

if __name__ == "__main__":
    
    
    sub("192.168.0.1")