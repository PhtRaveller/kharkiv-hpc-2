#include <stdio.h>

int func(int * valptr) {
    return 2 * (*valptr);
}

int main() {
    int i = 10;
    int *iptr;
    iptr = &i;
    printf("Value of number pointed by iptr: %i\n", *iptr);
    *iptr += 5;
    printf("Value of number pointed by iptr after addition: %i\n", *iptr);
    printf("Value of i after addition: %i\n", i);
    printf("Value, returned from function: %i\n", func(iptr));
    printf("Value, returned from function: %i\n", func(&i));
}