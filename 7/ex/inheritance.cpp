#include <stdio.h>

class Parent {
public:
    Parent(int x=1, int y=2, int z=3) : pub (x), pro(y), pri(z) {};
    friend int get_hidden(Parent p, bool priv);
    int pub;
protected:
    int pro;
private:
    int pri;
};

class Child : public Parent {
public:
    int get(bool get_protected);
};

int Child::get(bool get_protected) {
    return get_protected ? pro : pri;
};

int get_hidden(Parent p, bool priv) {
    return priv ? p.pri : p.pro;
}

int main() {
    Parent pr;
    Child ch;
    printf("Protected value is %i\n", ch.get(true));
    printf("Private value is %i\n", ch.get(false));
    printf("Private value in pr is %i\n", get_hidden(pr, true));
    printf("Protected value in pr is %i\n", get_hidden(pr, false));
    printf("Private value in ch is %i\n", get_hidden(ch, true));
    printf("Protected value in ch is %i\n", get_hidden(ch, false));
}