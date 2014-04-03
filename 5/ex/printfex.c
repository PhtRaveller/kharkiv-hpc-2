#include <stdlib.h>
#include <stdio.h>

int main() {
    int i = 100;
    int j = -25;
    float f = 100.2;
    printf("Simple int: i=%i, j=%i\n", i, j);
    printf("Padded int: i=% i, j=% i\n", i, j);
    printf("int with sign: i=%+i, j=%+i\n", i, j);
    printf("Floating point: %f\n", f);
    printf("Floating point in scientific notation: %e\n", f);
    printf("Floating point in scientific notation with given number of digits after .: %.5e\n", f);
    printf("Floating point padded and with given number of digits after .: %15.5f\n", f);
}
