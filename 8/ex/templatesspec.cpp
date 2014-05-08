#include <iostream>

template<typename T>
void mfunc(T arg) {
    std::cout << "I'm general template" << std::endl;
}

template<>
void mfunc<float>(float arg) {
    std::cout << "I'm template specialization for float" << std::endl;
}

template<>
void mfunc<>(float* arg) {
    std::cout << "I'm template specialization for float*" << std::endl;
}

template<typename T>
void mfunc(T* arg) {
    std::cout << "I'm base template for T*" << std::endl;
}

void mfunc(int arg) {
    std::cout << "I'm plain function" << std::endl;
}

int main()
{
    double d = 1.;
    float f = 1.f;
    int i;
    mfunc(f);
    mfunc(&f);
    mfunc(i);
    mfunc(d);
    return 0;
}