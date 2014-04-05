int numelem = 3;

void add_ptr_vectors(float * a, float * b, float * res, int num) {
    int i;
    for (i=0; i<num; i++) {
        res[i] = a[i] + b[i];
    }
}

void add_arr_vectors(float a[], float b[], float res[], int num) {
    int i;
    for (i=0; i<num; i++) {
        res[i] = a[i] + b[i];
    }
}