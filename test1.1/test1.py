from random import randint

list(range(1,10))
L=[]
for x in range(1,20):
    L.append(x*x)

print(L)

print([x * x for x in range(1, 11) if x % 2 == 0])

print([a+b for a in 'abc' for b in 'xyz'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
   print(k,'=',v)

print([k +'=' + v for k , v in d.items()])

print([x for x in range(1,11) if (x%2==0)])

print([x if x%2==0 else -x for x in range(1,10)])

x = 'abc'
y = 123
print(isinstance(x, str))
print(isinstance(y, str))

g = (x * x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g = (x * x for x in range(10))

for n in g:
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o=odd()
print(next(o))
print(next(o))

print("\n")

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(5):
       print(n)

