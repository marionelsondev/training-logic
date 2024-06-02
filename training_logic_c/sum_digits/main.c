#include <stdio.h>

int main () {
    int num, sum = 0;

    printf("Enter the number: \n");
    scanf("%d", &num);

    if (num < 0) {
        printf("Couldn't add the digits because the number is negative, please try again. \n");
    } else {
        while(num > 0) {
            sum += num % 10;
            num = num / 10;
        }
        printf("The sum of digits is: %d\n", sum);
    }
    return 0;
}