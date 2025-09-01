#/*
code written by Eftekher Ali Efte from Bangladesh 
 email:eftekherali2000@gmail.com
pursuing computer science and engingeering in Ruet 
*/
#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>
#include<stdlib.h>
#define ull unsigned long long int
#define ll long long int
#include<ctype.h> 
using namespace std;
 

int funct(int x[],int i)
{
    int s=x[i];
    if(i>0){
        s+=funct(x,i-1);
    }
    printf("%d",s);
    return s;   
}
        
int main()
{
int y[]={1,3,2,8};
funct(y,2);

        
return 0;
}
