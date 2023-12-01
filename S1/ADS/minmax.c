#include<stdio.h>
int a[100],i=0,n;
void min();
void max();
void main()
{
int ch;
printf("enter array limit");
scanf("%d",&n);
printf("enter array elements");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
while(1)
{
printf("\n 1.minimum element");
printf("\n 2.maximum elemnt");
printf("\n enter your choice");
scanf("%d",&ch);
switch(ch)
{
case 1:min();
       break;
case 2:max();
       break;
deafult: printf("\n invalid choice");
}
}
}
void min()
{
int small;
for(i=0;i<n;i++)
{
if(a[i]<a[i-1])
{
small=a[i];
}
}
printf("%d",small);
}
void max()
{
int large;
for(i=0;i<n;i++)
{
if(a[i]>a[i-1])
{
large=a[i];
}
}
printf("%d",large);
}
