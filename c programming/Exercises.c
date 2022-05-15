#include<stdio.h>

int main()
{

int num1;
int num2;

printf("Enter this first number");
scanf("%d", &num1);



printf("Enter the second number");
scanf("%d", &num2);

if(num1 == num2)
{
    printf(" These numbers are equal");

}
else{

    printf("%d and %d are not equal", num1, num2);
}

   return 0;
   }