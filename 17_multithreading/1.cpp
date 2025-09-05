/*
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
      
        
int main()
{
    int arr[]={3,4,1,2,5,6,4,10,7,10,8};  
    
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
    {
        for (int j = i+1; j < sizeof(arr)/sizeof(arr[0]); j++)
        {
           if(arr[i]==arr[j])
           {
                arr[j]=-1;
           }
        }
       
        
    }

    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
    {
        if(arr[i]==-1)
        {
            continue;
        }
        cout<<arr[i]<<" ";
    }
return 0;
}
