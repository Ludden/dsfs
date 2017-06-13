from __future__ import division
import random

import matplotlib.pyplot as plt
import math
from collections import Counter

from ch04.VectFunc import shape, get_column, make_matrix
from ch05.Stats import correlation
from ch06.Prob import inverse_normal_cdf


def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points, bucket_size=10, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()


random.seed(0)
uniform = [200 * random.random() - 100 for _ in range(10000)]
normal = [57 * inverse_normal_cdf(random.random())
          for _ in range(10000)]


# plot_histogram(uniform, 10, "Uniform histogram")
# plot_histogram(normal, 10, "Normal histogram")

def random_normal():
    """returns a random draw from standard normal distribution"""
    return inverse_normal_cdf(random.random())


def correlation_matrix(data):
    _, num_columns = shape(data)

    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_columns, num_columns, matrix_entry)


xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("Very different joint distributions")
plt.show()

print correlation(xs, ys1)
print correlation(xs, ys2)
