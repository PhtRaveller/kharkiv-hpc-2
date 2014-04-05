#include "vector.h"

extern int numelem;

int main() {
    int i;
    float a[] = {74.,12.,136.};
    float b[] = {3.,14.,13.};
    float c[numelem];
    add_ptr_vectors(a,b,c,numelem);
    for (i=0; i<numelem; i++) {
        printf("%f ", c[i]);
    }
    puts("");
    add_arr_vectors(a,b,c,numelem);
    for (i=0; i<numelem; i++) {
        printf("%f ", c[i]);
    }
    numelem++;
    puts("");
}