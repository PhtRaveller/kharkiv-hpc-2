#include <stdio.h>
#include <math.h>

struct Point {
    float x,y;
    float distance(Point p);
    Point add(Point p);
};

float Point::distance(Point p) {
    float dx = this->x-p.x;
    float dy = this->y-p.y;
    return sqrt(dx*dx+dy*dy);
}

Point Point::add(Point p) {
    Point res = {.x=(x+p.x), .y=(y+p.y)};
    return res;
}

int main() {
    struct Point f = {0.f, 1.f};
    struct Point s = {1.f, 0.f};
    float dist = f.distance(s);
    struct Point sum = f.add(s);
    printf("Distance between (%.3f,%.3f) and (%.3f,%.3f) is %f\n", f.x, f.y, s.x, s.y, dist);
    printf("Vestor sum is (%.3f,%.3f)\n", sum.x, sum.y);
}