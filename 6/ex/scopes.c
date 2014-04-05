#include <stdio.h>

int global_var = 142;

int main() {
    int local_var = 5;
    printf("Value of global variable is %i\n", global_var);
    printf("Value of local variable inside function is %i\n", local_var);
    {
        int local_var = 10;
        printf("Value of local variable inside nested block is %i\n", local_var);
    }
    printf("Value of local variable inside function after nested block is %i\n", local_var);
}