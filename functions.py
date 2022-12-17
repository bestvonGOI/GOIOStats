import numpy as np
import os.path
import requests as rs
import csv
import re
import pprint



def dltable(webadr,tablename):
    csv_url=webadr
    res=rs.get(url=csv_url)
    open(tablename,'wb').write(res.content)
    return 0

def readtable(tablename,category):
    reader = csv.DictReader(open(tablename))
    temp=list(reader)
    out={}
    for i in range(0,len(temp)):
        out[temp[i][category]]=temp[i]
    return out

def parse_input_file(tfile):
    with open(tfile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        lines=list(spamreader)
    return lines
