# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
from pyspark.sql import SparkSession
from random import random

def function(num):
    x = 2 * random() - 1
    y = 2 * random() - 1
    return x ** 2 + y ** 2 <= 1

if __name__ == "__main__":
    spark = SparkSession.builder.appName("EstimatePi").getOrCreate()
    if len(sys.argv) > 1:
        partitions = int(sys.argv[1])
    else:
        partitions = 2
    n = 100_000 * partitions
    count = spark.sparkContext.parallelize(range(1, n + 1), partitions). \
        map(function).reduce(lambda x, y: x + y)
    print(f"Pi is roughly {4.0 * count / n}")
    spark.stop()
