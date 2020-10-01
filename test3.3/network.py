# -*- coding: utf-8 -*

class foot:

    def foot_1(self):
        self.over = 42;


f = foot()
f.foot_1()
print(f.over)


class A:
    def hello(self):
        print('ab')

    def hello2(cls):
        print('cd')


class B(A):
    def hello(self):
        A.hello(self)
        self.sound = '12'


c = B()
c.hello()
print(c.sound)


class Testiterator:
    value = 0

    def next(self):
        self.value += 1
        if self.value > 10: raise StopIteration()
        return self.value

    def _iter_(self):
        return self


test = Testiterator()
test.next()
test.next()
print(test.value)


def flatten(nest):
    for sublist in nest:
        for element in sublist:
            yield element


nest = [[1, 2], [3, 4], [3]]

for num in flatten(nest):
    print(num)


def flatten2(nest):
    try:
        try:
            nest + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nest:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nest


a = flatten2(['12', 'avc'])
print(list(a))


def repeat(value):
    while True:
        new = (yield value)
        if new is not None: value = new


r = repeat(42)
print(r.__next__())
print(r.send( 'this is a'))