#include <stdio.h>
 int main(void) 
{
	int x,y,prod;
	scanf("%d%d",&x,&y);
	prod=x*y;
	if(prod%2==0)
	{
		printf("even");	
	}
	else
	{
		printf("odd");
	}
	
}
