#include <stdio.h>

int c = 131;

class Cl {
    public:
        int c;
        Cl() {c = 0;};
        Cl(int val) {c = val;};
        int get_c(bool glob);
};

int Cl::get_c(bool glob) {
    //:: is used for name resolution
    return glob ? ::c : c; //ternary operator
}

int main() {
    Cl cl;
    printf("Global c is %i\n", cl.get_c(true));
    printf("Class local c is %i\n", cl.get_c(false));
}