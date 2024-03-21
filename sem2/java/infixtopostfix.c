#include<stdio.h>
#include<stdlib.h>
void push(char);
int pop();
int priority();
 exp[20];
int top=-1;
void main()
{
int i,length;
length=strlen 
printf("Enter the infix exprestion");
fgets(exp,20,stdin);

 	if(exp[i]=='(')
 	{
		exp[i]=push(); 	
 	}
 	else if(exp[i]>='a'||exp[i]<='z')
 	{
 		exp[i]=pop();
 		printf("%c",&exp);
 		return 
 	}
 	else (exp[i]=='+'||exp[i]=='-'||exp[i]=='*'||exp[i]=='/')
 		{
 	          exp[i]=push();
 		}
 		
 	while(exp[i]=='(')
 	{
 	 if(exp[i]!=')')
 	 {
 	  exp[i]=pop();
 	  printf("%c",&exp);
 	 }
 	}
 	while(priority[top]>=exp[i])
 	{
		if(priority[top]>=exp[i])
		{
		 exp[i]=optr;
		 exp[i]=pop();
		 printf("%c",&optr);
		} 	
		else if(priority[top]<exp[i])
		{
		 exp[i]=push();
		}
 	}
 	
 }
 }
 void push(char c)
 {
 int op;
 return ;
 }
 int pop()
 {
 int optr;
 exp[i]=optr;
 exp[i]=pop();
 return 
 }
 int priority()
 { int act;
 do{
  switch(&act)
  {
   case 1:'+';
   case 2:'_';
   	return 2;
   case 3:'*';
   case 4:'/';
   	return 1;
   	
  }
 }
 }
}
