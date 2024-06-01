#include <stdio.h>
#include <math.h>

int main () {
    int num, prime = 1;

    printf("Enter the number: ");
    scanf("%d", &num);

    if (num <= 1) {
        prime = 0;
    } else {
        for (int divider = 2; divider <= sqrt(num); divider++) {
            if (num % divider == 0) {
                prime = 0;
                break;
                }
            }
        }
        if (prime) {
            printf("%d is a prime number.\n", num);
        } else {
            printf("%d is not a prime number.\n", num);
        }
}