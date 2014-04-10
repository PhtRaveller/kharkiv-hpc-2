#include <stdio.h>
#include <math.h>

class Point {
    public:
        Point (float x=0.f, float y=0.f) : x (x), y(y) {};
        float distance(Point p);
        Point add(Point p);
        float get_x() {return x;}
        float get_y() {return y;}
        float set_x(float val) {x = val;}
        float set_y(float val) {y = val;}
    private:
        float x,y;
};

float Point::distance(Point p) {
    float dx = x-p.get_x();
    float dy = y-p.get_y();
    return sqrt(dx*dx+dy*dy);
}

Point Point::add(Point p) {
    Point res(x+p.get_x(),y+p.get_y());
    return res;
}

int main() {
    Point f(0.f, 1.f);
    Point s(1.f, 0.f);
    float dist = f.distance(s);
    Point sum = f.add(s);
    printf("Distance between (%.3f,%.3f) and (%.3f,%.3f) is %f\n", f.get_x(), f.get_y(), s.get_x(), s.get_y(), dist);
    printf("Vestor sum is (%.3f,%.3f)\n", sum.get_x(), sum.get_y());
}