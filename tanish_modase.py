# -*- coding: utf-8 -*-
"""Tanish Modase.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yQKPydHIRT3O-IlspXOlL4Bdu_KZm8j1
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/tanishmodase18/vois/main/cars.csv")
data

"""# 1. Can you find that there has been an improvement in mpg over the years ?"""

plt.bar(data['year'], data['mpg'])
plt.xlabel('Year')
plt.ylabel('Miles per Gallon')

"""Answer ==> There is an improvement in mpg over the years

# 2. Does cubic inches of a vehicle affect the vehicle's time to reach 60 Miles per hour?
"""

plt.bar(data['cubicinches'], data['time-to-60'])
plt.xlabel('Cubic inches')
plt.ylabel('time-to-60')

"""Answer ==> YES, Vehicle's time to reach 60 miles per hour decreases with increase in Cubic inches.

# 3. Does a specific country prefer vehicles with more horsepower ?
"""

plt.bar(data['brand'], data['hp'])
plt.xlabel('Country')
plt.ylabel('HorsePower')

"""Answer ==> US prefers vehicles with more horsepower.

# 4. How does horsepower affect the average of the vehicle ?
"""

plt.bar(data['hp'], data['mpg'])
plt.grid()
plt.xlabel('HorsePower')
plt.ylabel('Miles per Gallon')

"""Answer ==> Average of vehicle decreases with increase of horsepower.

# 5. How does the cubic inches affect the average of the vehicle ?
"""

plt.bar(data['cubicinches'], data['mpg'])
plt.grid()
plt.xlabel('Cubic Inches')
plt.ylabel('Miles per Gallon')

"""Answer ==> Average of vehicle decreases with increase of cubic inches.

# 6. What is the effect of the number of cylinders on the mpg ?
"""

plt.bar(data['cylinders'], data['mpg'])
plt.grid()
plt.xlabel('Cylinders')
plt.ylabel('Miles per Gallon')

"""Answer ==> MPG first increases and then decreases with increase number of cylinders.

# 7. What relation between cubic inches , number of cylinders and horsepower can you observe from the data ?
"""

plt.bar(data['cylinders'], data['cubicinches'])
plt.xlabel('Cylinders')
plt.ylabel('Cubic Inches')

plt.bar(data['cylinders'], data['hp'])
plt.xlabel('Cylinders')
plt.ylabel('HorsePower')

"""Answer ==> Cubic Inches and horsepower increases with increase in number of cylinders.

# 8. How much proportion of the total records is occupied by vehicles with 8 cylinders ?
"""

cylinder_type = [4,8,6,5,3]
a = data['cylinders'].value_counts()
plt.pie(a, explode=[0,0.2,0,0,0], labels=cylinder_type, autopct='%0.1f%%', shadow=True, startangle=180)
plt.show()

len(data)

"""Answer ==> Vehicles with 8 cylinder = 76, Total records = 261,
           Proportion = (76/261)*100
                      = 29.1 %
"""
