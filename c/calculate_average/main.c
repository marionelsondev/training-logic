#include <stdio.h>

int main () {
    float num1, num2, num3, total, average;

    printf("Enter the first number: ");
    scanf("%f", &num1);

    printf("Enter the second number: ");
    scanf("%f", &num2);

    printf("Enter the third number: ");
    scanf("%f", &num3);

    total = num1 + num2 + num3;
    average = total / 3.0;

    printf("The average is: %.2f\n", average);

    return 0;
}