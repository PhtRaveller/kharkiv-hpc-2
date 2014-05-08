#include <iostream>

template<class T>
T * add_vectors(T * f, T * s, int dim) {
    T * result = new T[dim];
    for (int i = 0; i < dim; ++i)
    {
        result[i] = f[i] + s[i];
    }
    return result;
}

int main() {
    float ffloat[5] = {1.f,2.f,1.f,3.f,7.f};
    float sfloat[5] = {2.f,7.f,3.f,5.f,9.f};
    int fint[5] = {1,2,1,3,7};
    int sint[5] = {2,7,3,5,9};
    float * resfloat = add_vectors(ffloat,sfloat,5);
    int * resint = add_vectors(fint,sint,5);
    for (int i = 0; i < 5; ++i)
    {
        std::cout << resfloat[i] << std::endl;
    }
    for (int i = 0; i < 5; ++i)
    {
        std::cout << resint[i] << std::endl;
    }
    delete[] resfloat;
    delete[] resint;
}