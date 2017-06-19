#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ref: Data Cleaning with Python - MoMA's Artwork Collection
# http://bit.ly/2sjjdlR

import pandas
artworks_100 = pandas.read_csv("https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv")
# alternative way:
# artworks_100 = pandas.read_csv("/Users/lleiou/Google Drive/Python/openaccess/MetObjects.csv")
artworks_100.head(10)







# about large file, like the csv file in this problem...
# type the following code in termial:
# curl -O https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv
