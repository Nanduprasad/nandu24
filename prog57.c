#include <stdio.h>
int main(void) 
{
int x,y,temp;
scanf("%d %d",&x,&y);
printf("\n before swapping:");
printf("\nx=%d",x);
printf("\ny=%d",y);
temp=x;
x=y;
y=temp;
printf("\n after swapping:");
printf("\nx=%d",x);
printf("\ny=%d",y);
return 0;
}
