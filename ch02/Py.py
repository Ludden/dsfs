from __future__ import division
from collections import Counter
import random
from functools import partial


def double(x):
    return x * 2


def apply_to_one(f):
    return f(1)


my_double = double
x = apply_to_one(my_double)
print (x)

y = apply_to_one(lambda x: x + 4)
print (y)


def another_double(x): return 2 * x


def sum_and_product(x, y):
    return (x + y), (x * y)


c = Counter([0, 1, 2, 0])

even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]

square_dict = {x: x * x for x in range(5)}

increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]

random.seed(10)
print [random.random() for _ in range(10)]
random.seed(10)
print [random.random() for _ in range(10)]

print random.sample(range(100), 5)


def exp(base, power):
    return base ** power


two_to_the = partial(exp, 2)
print two_to_the(3)

square_of = partial(exp, power=2)
print square_of(3)


def double(x):
    return 2 * x


xs = [1, 2, 3, 4]
twice_xs1 = [double(x) for x in xs]
twice_xs2 = map(double, xs)
list_doubler = partial(map, double)
twice_xs3 = list_doubler(xs)


def multiply(x, y):
    return x * y


products = map(multiply, [1, 2], [4, 5])
print products

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipped1 = zip(list1, list2)
print zipped1

unzipped = zip(*zipped1)
print unzipped


def doubler(f):
    def g(x):
        return 2 * f(x)

    return g


def f1(x):
    return x + 1


g = doubler(f1)
print g(3)


def magic(*args, **kwargs):
    print "unnamed args:", args
    print "keyword args: ", kwargs


magic(1, 2, key="word", key2="word2")


def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1, 2]
z_dict = {"z": 3}
print other_way_magic(*x_y_list, **z_dict)
