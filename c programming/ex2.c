#include <stdio.h>

int main()
{
char grade;

printf("Enter your grade :");
scanf("%s", &grade);

switch(grade)
{
case 'E':
printf("Excellent !");
break;
case 'V':
printf("Very good");
break;
case 'G':
printf("Good !");
break;
case 'A':
printf("Average");
break;
case 'F':
printf("YOU FAILED ");

break;
default:
printf("Please enter a valid grade");
break;


}

    return 0;
}