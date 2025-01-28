import pandas as pd
import numpy as np
import sys
from datetime import date
import random
data = pd.read_csv(r'F:\دانشگاه\نمونه گیری1\project\city_day.csv')

''' روش خوشه ای دو مرحله ای'''

# میانگین داده های شاخص NO

''' # 1 '''
# specific data in a specific timeline
Data = []
count = 0
count2 = 0
sum1 = 0
count4 = 0
no = []
Sum1 = 0
sample1 = []
for i in data.groupby(data['Date']):
    Data.append(i)
for i in Data:
    count += 1
for i in range(count):
    if Data[i][0] >= '2019-02-00' and Data[i][0] <= '2019-03-00':
        for j in data['NO'].groupby(Data[i][1]['City']):
            no.append(j)

# sum of values
for i in no:
    count2 += 1
for i in range(count2):
    if no[i][0] == 'Bengaluru':
        for j in no[i][1]:
            count4 += 1
            if count4 <= 10:
                sample1.append(j)
                sum1 += j
                Sum1 += j ** 2

SUM1 = sum1/10
print(SUM1, ': مقدار وای بار اس یک دات')


''' # 2 '''
# specific data in a specific timeline
Data2 = []
count3 = 0
count5 = 0
sum2 = 0
count6 = 0
no2 = []
Sum2 = 0
sample2 = []
for i in data.groupby(data['Date']):
    Data2.append(i)
for i in Data2:
    count3 += 1
for i in range(count3):
    if Data2[i][0] >= '2019-04-00' and Data2[i][0] <= '2019-05-00':
        for j in data['NO'].groupby(Data2[i][1]['City']):
            no2.append(j)

# sum of values
for i in no2:
    count5 += 1
for i in range(count5):
    if no2[i][0] == 'Bengaluru':
        for j in no2[i][1]:
            count6 += 1
            if count6 <= 10:
                sample2.append(j)
                sum2 += j
                Sum2 += j ** 2

SUM2 = sum2/10
print(SUM2, ': مقدار وای بار اس دو دات')

''' # 3 '''
# specific data in a specific timeline
Data3 = []
count7 = 0
count8 = 0
sum3 = 0
count9 = 0
no3 = []
Sum3 = 0
sample3 = []
for i in data.groupby(data['Date']):
    Data3.append(i)
for i in Data3:
    count7 += 1
for i in range(count7):
    if Data3[i][0] >= '2019-07-00' and Data3[i][0] <= '2019-08-00':
        for j in data['NO'].groupby(Data3[i][1]['City']):
            no3.append(j)

# sum of values
for i in no3:
    count8 += 1
for i in range(count8):
    if no3[i][0] == 'Bengaluru':
        for j in no3[i][1]:
            count9 += 1
            if count9 <= 10:
                sample3.append(j)
                sum3 += j
                Sum3 += j ** 2
SUM3 = sum3/10
print(SUM3, ': مقدار وای بار اس سه دات')

# total average
average = (SUM1 + SUM2 + SUM3)/3
print(average, ': میانگین دو مرحله ای داده های شاخص NO')

# S2B
S2B = ((SUM1 ** 2 + SUM2 ** 2 + SUM3 ** 2) - 3 * (average ** 2))/2
print(S2B, ': مقدار S2B')

# S2j
S21 = (Sum1 - (10 * (SUM1 ** 2)))/9
S22 = (Sum2 - (10 * (SUM2 ** 2)))/9
S23 = (Sum3 - (10 * (SUM3 ** 2)))/9

# variance of the average
part1 = (1 - (3/12)) * S2B/3
part2 = (1 - (1/3)) * S21/10
part3 = (1 - (1/3)) * S22/10
part4 = (1 - (1/3)) * S23/10
variance = part1 + ((part2 + part3 + part4)/36)
print(variance, ': مقدار وارانس میانگین برای شاخص NO')


''' run to text file '''
with open(r"F:\دانشگاه\نمونه گیری1\project\nemooneh2_project.txt", 'w') as file:
    sys.stdout = file
    print('the method', '\n NO')
    print('\nand the sample of 3 month and 10 days from 2019', '\n and the city of Bengaluru')
    print('\nfor the date between 2019-02-00 and 2019-03-00 the sample is:', sample1)
    print('\nthe sum of them is :', sum1)
    print('\nthe sum of the square is :', Sum1)
    print('\ny bar s 1 dot:', SUM1)
    print('\nfor the date between 2019-04-00 and 2019-05-00 the sample is:', sample2)
    print('\nthe sum of them is :', sum2)
    print('\nthe sum of the square is :', Sum2)
    print('\ny bar s 2 dot:', SUM2)
    print('\nfor the date between 2019-07-00 and 2019-08-00 the sample is:', sample3)
    print('\nthe sum of them is :', sum3)
    print('\nthe sum of the square is :', Sum3)
    print('\ny bar s 3 dot:', SUM3)
    print('\ny bar c :', average)
    print('\nthe calculation of variance:\n')
    print('S2B:', S2B)
    print('\nS2j:\n')
    print('S21:', S21)
    print('\nS22:', S22)
    print('\nS23:', S23)
    print('\nvariance of the average :', variance)




