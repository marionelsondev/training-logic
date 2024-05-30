#include <stdio.h>

int main () {
    int num;
    
    printf("Enter the number: \n");
    scanf("%d", &num);

    if (num % 2 == 0) {
        printf("The number is even.\n");
    }
    else {
        printf("The number is odd.\n");
    }
    printf("Chosen number: %d\n", num);
    return 0;
}