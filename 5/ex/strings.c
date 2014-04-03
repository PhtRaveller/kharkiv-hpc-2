#include <stdlib.h>
#include <stdio.h>

int main() {
    char buff[] = "This is a string\n";
    printf("%s", buff);
    printf("Part of a string as an integer: %i\n", buff[0]);
    printf("Part of a string as a char: %c\n", buff[0]);
    exit(0);
}