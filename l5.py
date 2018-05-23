#!/usr/bin/env python3
import pickle
from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = pickle.loads(urlopen(url).read())

for line in data:
    print("".join([i[0] * i[1] for i in line]))