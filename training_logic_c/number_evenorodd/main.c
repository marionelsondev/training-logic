#include <stdio.h>

int main () {
    int num;
    
    do {
        printf("Enter a positive number: \n");
        scanf("%d", &num);
        if (num <= 0) {
            printf("Invalid number, you entered a value less than or equal to zero, please try again.\n");
        }
    } while (num <= 0);

    for (int i = 1; i <= num; i++) {
        if (i % 2 == 0) {
            printf("The number '%d' is even.\n", i);
        } else {
            printf("The number '%d' is odd.\n", i);
        }   
    }
    return 0;
}