#include "vector.h"

int main()
{
    using namespace VectorNS;
    VectorInt<4> v;
    v.read();
    v.dump();
    for (int i = 0; i < 4; ++i)
    {
        std::cout << (v[i]) << std::endl;
    }
    std::cout << v.norm() << std::endl;
    return 0;
}