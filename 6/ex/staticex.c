#include <stdio.h>

void func() {
    static int i = 0;
    int j = 0;
    i += 5;
    j += 5;
    printf("i=%i, j=%i\n", i, j);
}

int main() {
    printf("First call to func:\n");
    func();
    printf("Second call to func:\n");
    func();
}