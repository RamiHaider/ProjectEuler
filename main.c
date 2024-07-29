#include <stdio.h>



int main() {
    int addition_of_largest_numbers = 0;

    for (int i = 1; i <= 10000000; i++) {
        for (int j = i-1; j >= 0; j--) {
            if (((j * j - j) % i) == 0) {
                addition_of_largest_numbers += j;
                    break;
            } 
        }
    }
    printf("%d\n", addition_of_largest_numbers);
    return 0;
}

