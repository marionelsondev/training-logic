#include <stdio.h>

int main () {

    int num, sumAll = 0, sumAmount = 0;

    while(1) {
        printf("Enter a number (negative to stop): \n");
        int valueValidation = scanf("%d", &num); 

        if (valueValidation != 1){
            printf("Oops, it looks like something went wrong. Maybe you entered an invalid value. Please try again.\n");
            break;
        }    

        if (num >= 0) {
            sumAll += num;
            if (num > 0) {
                sumAmount++;
            }
        } else if (num < 0){
            printf("You ended the program by entering a negative number. We are processing the obtained results...\n");
            printf("This shouldn't take long...\n");
            printf("%d positive numbers that were entered.\n", sumAmount);
            printf("The total sum of the entered numbers is: %d\n", sumAll);
            break;
        }
    }

    return 0;
}