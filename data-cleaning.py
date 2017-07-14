#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pandas API Ref:
# http://bit.ly/2s4qB0O

# ref: Data Cleaning with Python - MoMA's Artwork Collection
# http://bit.ly/2sjjdlR

import pandas
data = pandas.read_csv("https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv")
# alternative way:
# artworks_100 = pandas.read_csv("/Users/lleiou/Google Drive/Python/openaccess/MetObjects.csv")
sample = artworks_100.head(10)
# data
sample["Repository"].value_counts()
data["Culture"].value_counts()


# about large file,  like the csv file in this problem...
# type the following code in termial:
# curl -O https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv

# some articles on the same data set:
# http://sqlservercode.blogspot.com/2017/02/importing-metropolitan-museum-of-arts.html
# https://www.springboard.com/blog/ggplot2-in-r-tutorial/
# https://avital.ca/notes/exploring-met-museums-openaccess-dataset

l = [12,3,3,4,5,5,6,6]

from collections import Counter
counts = Counter(l)
counts["3"]

def count(l):
    result = {}
    for item in l:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

count(l)


# help(pd.Series.loc)




from pandas import DataFrame
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

frame
f = lambda x: x.max() - x.min()

In [119]: frame.apply(f)
Out[119]:
b    1.133201
d    1.965980
e    2.829781
dtype: float64
