#include "func.h"
#define MIN(a,b) ((a)>(b))?(b):(a)
#define ABS(a) (((a)>0)?(a):-(a))

void rec(double * s, char * res, double thresh, int len) {
    for (int i=0; i<len; ++i) {
        for (int j = i; j < len; ++j)
        {
            res[i*len+j] = ABS(s[i]-s[j])<thresh ? 1:0;
        }
    }
}

void rec_blocked(double * s, char * res, double thresh, int len) {
    #pragma omp parallel for
    for (int i = 0; i < len; i+=BLOCK)
    {
        for (int j = i; j < len; j+=BLOCK)
        {
            for (int ii = i; i < MIN(i+BLOCK, len); ++ii)
            {
                for (int jj = j; jj < MIN(j+BLOCK, len); ++jj)
                {
                    res[ii*len+jj] = ABS(s[ii]-s[jj])<thresh ? 1:0;
                }
            }
        }
        
    }
}