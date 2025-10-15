from typing import List
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator==0:
            return ""
        if numerator==0:
            return "0"
        res=""
        if (numerator<0)^(denominator<0):
            res+="-"
        num,den=abs(numerator),abs(denominator)
        res+=str(num//den)
        rem=num%den
        if rem==0:
            return res
        res+="."
        rem_map={}
        idx=len(res)
        while rem!=0:
            if rem in rem_map:
                res=res[:rem_map[rem]]+"("+res[rem_map[rem]:]+")"
                break
            rem_map[rem]=idx
            rem*=10
            res+=str(rem//den)
            idx+=1
            rem=rem%den
        return res