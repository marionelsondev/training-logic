#include <stdio.h>

int main () {
    float num1, num2, product;
    char operator;

    printf("Enter the first number: \n");
    scanf("%f", &num1);

    printf("Enter the operation you want to use: \n");
    scanf(" %c", &operator);

    printf("Enter the second number: \n");
    scanf("%f", &num2);
        
    switch (operator) {
    case '*':
        product = num1 * num2;
        break;
    case '/':
        if (num2 != 0) {
            product = num1 / num2;
        } else {
            printf("Error: Division by zero is not allowed.\n");
            return 1;
        }
    case '+':
        product = num1 + num2;
        break;
    case '-':
        product = num1 - num2;
        break;
    default:
        printf("Invalid operator. \n");
        return 1; 
    }

    printf("%.2f %c %.2f = %.2f.\n", num1, operator, num2, product);
    return 0;
}