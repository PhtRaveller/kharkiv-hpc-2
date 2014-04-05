#include <stdlib.h>
#include <stdio.h>

int main() {
    int * a;
    int b[] = {1,2,3};
    int num, i;
    for (i=0; i<3; i++) {
        printf("b[%i]=%i ", i, b[i]);
    }
    puts("\nEnter the number of elements in a dynamic array: ");
    scanf("%i", &num);
    a = (int*) malloc(num * sizeof(int));
    if (a==NULL) exit(1);
    for (i=0; i<num; i++) {
        a[i] = i;
        printf("a[%i]=%i ", i, a[i]);
    }
    puts("");
    free(a);
}