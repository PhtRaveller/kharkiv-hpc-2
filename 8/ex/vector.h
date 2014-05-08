#include <iostream>
#include <stdlib.h>
namespace VectorNS {

template<typename T=float, int N=8>
class Vector {
public:
   Vector() {dim = N; values = new T[N];};
   Vector(T* vals) {values = vals;};
   ~Vector() {delete[] values;};
   void read();
   void dump();
   T norm() {};
   Vector<T> operator+(Vector<T> v) {};
   T operator[](int i) {return values[i];};
protected:
    int dim;
    T * values;
};

template<int N>
class VectorInt : public Vector<int, N> {
public:
    int norm();
    VectorInt<N> operator+(const VectorInt<N>& v);
};

template<typename T, int N>
void Vector<T,N>::read() {
    for (int i = 0; i < dim; ++i)
    {
        std::cin >> values[i];
    }
}

template<typename T, int N>
void Vector<T,N>::dump() {
    for (int i = 0; i < dim; ++i)
    {
        std::cout << values[i] << " ";
    }
    std::cout << std::endl;
}

template<int N>
int VectorInt<N>::norm() {
    int res = 0;
    for (int i = 0; i < this->dim; ++i)
    {
        res += abs(this->values[i]);
    }
    return res;
}
}