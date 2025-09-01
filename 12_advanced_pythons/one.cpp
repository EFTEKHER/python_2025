// #include <iostream>
// using namespace std;

// class Counter {
//     static int count; // declaration (shared by all objects)
// public:
//     Counter() {
//         count++;
//         cout << "Constructor called. Count = " << count << endl;
//     }
//     ~Counter() {
//         cout << "Destructor called. Count = " << count << endl;
//         count--;
//     }

//     void showValue() const {
//         cout << "Current Count = " << count << endl;
//     }
// };

// // definition of static member (outside the class)
// int Counter::count = 2;

// int main() {
//     Counter a, b;
//     {
//         Counter c;
//     }
//     Counter d;
//     return 0;
// }
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
  int i=-3;
  int j=1;
  int k=0;
  int m= (i+=1) or ((j+=1) && (k+=1));
  cout<<i<<" "<<j<<" "<<k<<" "<<m;
return 0;
}
