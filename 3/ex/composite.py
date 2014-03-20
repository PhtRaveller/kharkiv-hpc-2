#!/usr/bin/python

import operator

class Expression(object):
    def get_value(self):
        pass

class Value(Expression):
    def __init__(self, expr):
        self.value = float(expr)
    def get_value(self):
        return self.value

class Operation(Expression):
    def __init__(self):
        self.components = []
        self.oper = None
    def get_value(self):
        result = self.components[0].get_value()
        for c in self.components[1:]:
            result = self.oper(result, c.get_value())
        return result
    def set_type(self, oper):
        self.oper = oper
    def add_component(self, component):
        self.components.append(component)

def factory(expr):
    if '+' in expr:
        optype = '+'
        oper = operator.add
    elif '-' in expr:
        optype = '-'
        oper = operator.sub
    elif '*' in expr:
        optype = '*'
        oper = operator.mul
    elif '/' in expr:
        optype = '/'
        oper = operator.div
    else:
        res = Value(expr)
        return res
    res = Operation()
    res.set_type(oper)
    for e in expr.split(optype):
        res.add_component(factory(e))
    return res

if __name__ == '__main__':
    import sys
    expr = sys.argv[1]
    o = factory(expr)
    print "Value is {}".format(o.get_value())
    print o.components
    for c in o.components:
        print c.get_value()