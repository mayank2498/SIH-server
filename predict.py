#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 09:14:00 2018

@author: abhik
"""
import pandas as pd

result = pd.read_csv("result.csv")

x= input("lat:")
y= input("lon:")

select = result[result.lat==float(x)]
select = select[select.lon==float(y)]
select = select.drop_duplicates(subset='crop')
select['crop'][:5]