#include <stdio.h>
#include<conio.h>
int main() {
    // printf("%c",getc(stdin));
    // printf("%c",getch());
    int a=1,b=2,c=3,x;
    printf("%d",a+=(a+=3,5,a));
    x=(a+=3,a);
    printf("%d",x);
    return 0;
}