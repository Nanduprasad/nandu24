#include <stdio.h>
int main(void) 
{
	int i,n=2,array[50],sum=0,avg;
	for(i=0;i<n;i++)
	{
		scanf("%d",&array[i]);
	
	}
	for(i=0;i<n;i++)
	{
		sum=sum+array[i];
	}
	avg=sum/n;
	printf("%d",sum);
}
