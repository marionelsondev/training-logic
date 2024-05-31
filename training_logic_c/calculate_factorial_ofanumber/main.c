#include <stdio.h>

int main () {
    int num;
    unsigned long long numfact = 1;
    do {
        printf("Enter a positive whole number:\n");
        scanf("%d", &num);
        if (num < 0) {
            printf("Invalid number. Try again.\n");
        };
    } while (num < 0);
    if (num == 0) {
        printf("The factorial of 0 is: 1.");
    } else {
        for (int diffcount = num; diffcount > 1; diffcount--) {
            numfact *= diffcount;
        }
        printf("The factorial of %d is %I64u.\n", num, numfact);
    }
    return 0;
}