#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
