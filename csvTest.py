"""
Hostel: 0
SJT: 1
TT: 2
MB: 3
SMV: 4
CDMM: 5
Library: 6
"""
import csv
import sys

f = open('data.csv', 'rb')
reader = csv.reader(f)
for row in reader:
  print len(row)
f.close()