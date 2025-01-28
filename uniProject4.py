import pandas as pd
import numpy as np
import sys
from datetime import date
import random
data = pd.read_csv(r'F:\دانشگاه\نمونه گیری1\project\city_day.csv')

''' روش سیستماتیک '''

# میانگین داده های شاخص NO

# variables
Data = []
count = 0
count2 = 0
count4 = 0
no = []
sample2 = []
sample3 = []
m = 2
sys1 = [3]
sys2 = [10]
summation1 = 3
summation2 = 10
y3 = []
y10 = []
sum_y3 = 0
sum_y10 = 0

# specific data in a specific timeline
for i in data.groupby(data['Date']):
    Data.append(i)
for i in Data:
    count += 1
for i in range(count):
    if Data[i][0] >= '2019-00-00' and Data[i][0] <= '2020-00-00':
        for j in data['NO'].groupby(Data[i][1]['City']):
            no.append(j)

for i in no:
    count2 += 1
for i in range(count2):
    if no[i][0] == 'Bengaluru':
        for j in no[i][1]:
            count4 += 1
            sample3.append(j)
for k in range(2 * 10):
    sample2.append(k)

a = count4 / 36

# creation of samples
for k in sample2:
    if k == 3:
        for i in range(17):
            summation1 += 20
            sys1.append(summation1)
    if k == 10:
        for i in range(17):
            summation2 += 20
            sys2.append(summation2)

# y3 and y10 samples
for i in sys1:
    y3.append(sample3[i-1])
for i in sys2:
    y10.append(sample3[i-1])

# summations
for i in y3:
    sum_y3 += i
for i in y10:
    sum_y10 += i

# average
ave_y3 = sum_y3/18
ave_y10 = sum_y10/18

# total average
total_ave = (ave_y3 + ave_y10)/2

# variance of the average
part1 = (ave_y3 - total_ave) ** 2
part2 = (ave_y10 - total_ave) ** 2
variance = (part1 + part2)/(9/20)

# run to text file
with open(r"F:\دانشگاه\نمونه گیری1\project\nemooneh2_project4.txt", 'w') as file:
    sys.stdout = file
    print('systematic method')
    print('\nfor calculation of NO metric')
    print('\nfor Bengaluru city over period of one year from 2019 to 2020')
    print('a =', a)
    print('m = ', m)
    print('\n1 to ma sample is:', sample2)
    print('\ntwo values 3 and 10 are chosen.')
    print('\nthe sample list of 3 is:', sys1)
    print('\nand the values are:', y3)
    print('\nthe sum of values:', sum_y3)
    print('\nso the average for y3 is:', ave_y3)
    print('\nthe sample list of 10 is:', sys2)
    print('\nand the values are:', y10)
    print('\nthe sum of values:', sum_y10)
    print('\nso the average for y10 is:\n', ave_y10)
    print('\nthe total average is:', total_ave)
    print('\nand the variance of the average:', variance)


