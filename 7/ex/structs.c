#include <stdio.h>
#include <math.h>

struct Point {
    float x,y;
};

typedef struct Point Point;

float distance(Point f, Point s) {
    float dx = f.x-s.x;
    float dy = f.y-s.y;
    return sqrt(dx*dx+dy*dy);
}

Point add(Point * f, Point * s) {
    Point res = {.x=(f->x+s->x), .y=(f->y+s->y)};
    return res;
}

int main() {
    struct Point f = {0.f, 1.f};
    struct Point s = {1.f, 0.f};
    float dist = distance(f,s);
    struct Point sum = add(&f,&s);
    printf("Distance between (%.3f,%.3f) and (%.3f,%.3f) is %f\n", f.x, f.y, s.x, s.y, dist);
    printf("Vestor sum is (%.3f,%.3f)\n", sum.x, sum.y);
}