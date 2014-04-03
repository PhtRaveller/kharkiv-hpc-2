#include <stdlib.h>
#include <stdio.h>

int get_double(int a) {
    return 2 * a;
}

void print_val(int val) {
    printf("I'm printing function. val=%i\n", val);
}

int main() {
    int val = 5;
    print_val(val);
    printf("Result is %i\n", get_double(val));
}