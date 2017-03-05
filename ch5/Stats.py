from __future__ import print_function
from __future__ import division
from collections import Counter

import math
from matplotlib import pyplot as plt

from ch4.VectFunc import sum_of_squares

num_friends = [100, 49, 41, 40, 25, 1, 4, 7, 4, 3, 3, 5, 6, 7, 5, 4, 34, 6, 47, 74, 3, 32, 2, 54, 6, 3, 2, 3, 2, 1, 2, 3, 5, 6, 7, 8, 2, 2, 3, 2, 2, 3, 2, 2, 1,
               1, 1, 3, 32, 32, 34, 1, 1, 3, 2, 3, 38, 98, 9, 3, 2, 10, 4, 5, 6, 7, 3, 2, 3, 3]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of friend counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
# plt.show()

num_points = len(num_friends)
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
largest_value = sorted_values[-1]


def mean(x):
    return sum(x) / len(x)


def median(x):
    s_vals = sorted(x)
    if len(s_vals) % 2 == 1:
        return s_vals[len(s_vals) // 2]
    else:
        return (s_vals[len(s_vals) // 2] + s_vals[len(s_vals) // 2 + 1]) / 2


def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]


def data_range(x):
    return max(x) - min(x)


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def std_dev(x):
    return math.sqrt(variance(x))


def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


print('mean:', mean(num_friends))
print('med:', median(num_friends))
print('q10:', quantile(num_friends, 0.1))
print('q25:', quantile(num_friends, 0.25))
print('q75:', quantile(num_friends, 0.75))
print('q90:', quantile(num_friends, 0.9))
print('mode:', mode(num_friends))
print('range:', data_range(num_friends))
print('variance:', variance(num_friends))
print('stddev:', std_dev(num_friends))
print('interquartile range:', interquartile_range(num_friends))
